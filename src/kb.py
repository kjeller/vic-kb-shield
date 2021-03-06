import usb_hid
from adafruit_hid.keyboard import Keyboard
import digitalio
import kb_map
import board
import time

# Index 0, 1, 2 maps to row A, B, C and so on.
# The logic high or low will be written on gpio_row and be read from gpio_col
# See kb_map.py for more information regarding this.
gpio_row = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8]

# Index 0, 1, 2 maps to col 0, 1, 2 and so on.
gpio_col = [board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19]

class KeyboardImpl:
    def __init__(self, name="Generic Keyboard", layout=None):
        self.name = name
        self.layout = layout # Unused for now
        self.kbd = Keyboard(usb_hid.devices) # Setup keyboard HID device
        
        self.key_row = []
        self.key_col = []

        self.prev_scan_matrix = {}
        self.last_keyreport = {}

        if layout is None:
            print("Layout is not defined.. using default")
            #TODO what is default
    
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
                    key = kb_map.pmap_to_kmap(self.key_row.index(row), self.key_col.index(col)) 
                    
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
                print("Keycode" + hex(key))
                diff.append(key)

        self.kbd.release(*diff)
       
        if scan_matrix:
            try:
                self.kbd.press(*scan_matrix)
                self.last_keyreport_time = time.monotonic() 
            except ValueError:
                print("No more than six regular keys may be pressed simultaneously.")
            self.last_keyreport = scan_matrix

    def update(self):
        scan_matrix = self.keyboard_scan()
        self.check_keyevent(scan_matrix)
        self.old_scan_matrix = scan_matrix
