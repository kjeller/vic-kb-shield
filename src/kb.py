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

        self.old_scan_matrix = []

        # Last key_event
        self.keyevent = {"key" : 0, "activeTime" : 0}

        # save timestamp for last sent keyreport, will be used to determine persistant keys
        self.last_keyreport = [] 
        self.last_keyreport_time = 0

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
                    print("Col #%d, Row #%d" % (i, j))

                    if col.value:
                        print("Key bounce ignored")
                        continue
                    
                    # Get HID keycode for the pressed key
                    key = kb_map.pmap_to_kmap(self.key_row.index(row), self.key_col.index(col)) 
                    
                    if key == None or key == kb_map.KC_EMPTY:
                        print("Key not mapped to anything..")
                        continue
                    else:
                        print("Keycode" + hex(key))

                    scan_matrix.append(key)
                row.value = True # 5V
        return scan_matrix

    # Determine what to do with scanned key matrix
    # Keyevent can either be active or new
    #   active - a key previously activated is depressed and held down
    #   new - a key not previously pressed is depressed
    def check_keyevent(self, scan_matrix, old_scan_matrix):
        key_report = [] 
        # Check if keystroke was in last keyreport
        while scan_matrix:
            current_keystroke = scan_matrix.pop()

            # Compare timestamps to see if active keystroke
            if current_keystroke in self.last_keyreport:
                now = time.monotonic()
                time_diff = now - self.last_keyreport_time

                print("")
                print("Active time: %f" % self.keyevent["activeTime"])
                print("Time diff:   %f" % time_diff)
                print("Now:         %f" % now)
                print("Last keyrpt: %f" % self.last_keyreport_time)
                print("")
                
                if self.keyevent["activeTime"]  > 0.7:  # TODO Add a constant for this threshold
                    key_report.append(current_keystroke)
              
                # Check if last keystroke of same key was entered recently or not
                # this is to prevent key spam when a user holds down a key, releasing the key 
                # and then pressing the same key
                if time_diff > 0.5:
                    self.keyevent["activeTime"] = 0
                    time_diff = 0
                    continue

                self.keyevent["activeTime"] += time_diff
               
            else: # Check if new keystroke
               key_report.append(current_keystroke)
               self.keyevent["activeTime"] = 0

        if key_report:
            try:
                self.kbd.press(*key_report)
                self.last_keyreport_time = time.monotonic() 
            except ValueError:
                print("No more than six regular keys may be pressed simultaneously.")
            self.kbd.release_all() # send usb hid report with reset buffer
            self.last_keyreport = key_report

    def update(self):
        scan_matrix = self.keyboard_scan()
        self.check_keyevent(scan_matrix, self.old_scan_matrix)
        self.old_scan_matrix = scan_matrix
