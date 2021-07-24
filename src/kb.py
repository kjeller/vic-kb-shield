# KeyboardImpl scans the key matrix and determines if a key is pressed or has been released
# a HID USB keyboard report is then sent to the host device.
#
# Author: Karl Strålman

import usb_hid
import digitalio
from kb_key import Key
from kb_layout import KC_LAYER_INC_KEY_POS, KC_MACRO_LAYER
from kb_hw_map import KeyboardHwLayout
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

class KeyboardImpl:
    def __init__(self, name="Generic Keyboard", gpio_row=None, gpio_col=None, layout=None, layers=None, macro_layer=None):
        self.name = name
        self.kbd = Keyboard(usb_hid.devices) # Setup keyboard HID device
        self.kbd_layout = KeyboardLayoutUS(self.kbd)
        self.keymap = KeyboardHwLayout(layout) # map layout to hw layout
        
        self.key_row = [] # write
        self.key_col = [] # read

        self.last_keyreport = {} # used for determining between scans
        self.last_scan_matrix = {}

        # Layers 0, 1, 2, 3 where 0 is the default layer 1 & 2 is the extended layers and 3 is the macro layer
        self.current_layer = 0 
    
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
                    # Ignore keybounce if it occurs (this is highly unlikely to get caught here)
                    if col.value:
                        continue

                    # Add scanned keyposition to scan matrix. 
                    # This will be used to map keycode or macro depending on current layer
                    scan_matrix.append(Key(self.key_row.index(row), self.key_col.index(col))) 
                row.value = True # 5V
        return scan_matrix
    
    # The released keys are the difference between last scan and current scan
    def get_diff_scan(self, scan_matrix):
        diff = []
        for key in self.last_scan_matrix:
            if key not in scan_matrix:
                diff.append(key)
        return diff

    def determine_layer(self, diff):
        # Check if layer button is pressed i, increase layer variable
        # TODO shift layer inc key to decrease variable
        if KC_LAYER_INC_KEY_POS in diff: #and KC_LAYER_INC_KEY_POS in diff:
            print("INCREMENT LAYER")
            self.current_layer = (self.current_layer + 1) % KC_MACRO_LAYER 

    # Determine what to do with scanned key matrix
    # Keyevent can either be active or new
    #   active - a key previously activated is depressed and held down
    #   new - a key not previously pressed is depressed
    def check_keyevent(self, scan_matrix, diff):
        if diff:
            mapped_diff = self.keymap.get_keymap(diff, self.current_layer)
            if mapped_diff:
                self.kbd.release(*mapped_diff)
                pass
       
        if scan_matrix:
            mapped_keys = self.keymap.get_keymap(scan_matrix, self.current_layer)
            if mapped_keys:
                try:
                    self.kbd.press(*mapped_keys)
                    pass
                except ValueError:
                    print("No more than six regular keys may be pressed simultaneously.")
            self.last_scan_matrix = scan_matrix

    def update(self):
        scan_matrix = self.keyboard_scan() # scan keyboard and create matrix with pressed keys
        diff = self.get_diff_scan(scan_matrix)
        self.determine_layer(diff) #increase or decrease layer (wrap-around)
        
        # No need to release keys or create key reports when in macro layer
        # since "write()" are sent directly and is self-releasing
        if self.current_layer == KC_MACRO_LAYER:
            print("IN MACRO LAYER WAHOOO")
            for diff_key in diff:
                # TODO Get macro layers to work
                print("Trying to write: ", self.keymap.get_mapped_key(diff_key))
                print("kmap", self.keymap[1][1][0])
                #self.kbd_layout.write(self.keymap.get_mapped_key(diff_key))
                #self.kbd_layout.write("HELLO THERE!")

        self.check_keyevent(scan_matrix, diff)