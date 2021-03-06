# KeyboardImpl scans the key matrix and determines if a key is pressed or has been released
# a HID USB keyboard report is then sent to the host device.
#
# Author: Karl Strålman

import usb_hid
from adafruit_hid.keyboard import Keyboard
import digitalio
import kb_map
from kb_hw_map import KeyboardHwLayout

class KeyboardImpl:
    def __init__(self, name="Generic Keyboard", gpio_row=None, gpio_col=None, layout=None):
        self.name = name
        self.kbd = Keyboard(usb_hid.devices) # Setup keyboard HID device
        self.keymap = KeyboardHwLayout(layout) # map layout to hw layout
        
        self.key_row = [] # write
        self.key_col = [] # read

        self.last_keyreport = {} # used for determining between scans
    
        # Setup write pins
        for pin in gpio_row:
            key_pin = digitalio.DigitalInOut(pin)
            key_pin.direction = digitalio.Direction.OUTPUT
            self.key_row.append(key_pin)

        # Setup read pins
        for pin in gpio_col:
            key_pin = digitalio.DigitalInOut(pin)
            key_pin.direction = digitalio.Direction.INPUT
            key_pin.pull = digitalio.Pull.UP
            self.key_col.append(key_pin)

    # Scan keyboard matrixfor keystrokes.
    # A registered keystroke will be send directly to the host USB.
    def keyboard_scan(self):
        scan_matrix = []
        for col in self.key_col:
            for row in self.key_row:
                row.value = False # 0V
                
                if not col.value: # Check if grounded by row key
                    i = self.key_col.index(col)
                    j = self.key_row.index(row)

                    # Ignore keybounce if it occurs (this is highly unlikely to get caught here)
                    if col.value:
                        continue
                    
                    # Get HID keycode for currently pressed key
                    key = self.keymap.get_keycode(self.key_row.index(row), self.key_col.index(col)) 
                    
                    if key == None or key == kb_map.KC_EMPTY:
                        print("Key not mapped to anything..")
                        continue

                    scan_matrix.append(key)
                row.value = True # 5V
        return scan_matrix
    
    # Determine what to do with scanned key matrix
    # Keyevent can either be active or new
    #   active - a key previously activated is depressed and held down
    #   new - a key not previously pressed is depressed
    def check_keyevent(self, scan_matrix):
        diff = []

        # The difference between last scan and current scan are the released keys
        for key in self.last_keyreport:
            if key not in scan_matrix:
                diff.append(key)

        if diff:
            self.kbd.release(*diff)
       
        if scan_matrix:
            try:
                self.kbd.press(*scan_matrix)
            except ValueError:
                print("No more than six regular keys may be pressed simultaneously.")
            self.last_keyreport = scan_matrix

    def update(self):
        scan_matrix = self.keyboard_scan()
        self.check_keyevent(scan_matrix)
        self.old_scan_matrix = scan_matrix
