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
        print("Keyboard scan")
        for col in self.key_col:
            for row in self.key_row:
                row.value = False
                time.sleep(0.0001)
                if not col.value: # Check if grounded by row key
                    i = self.key_col.index(col)
                    j = self.key_row.index(row)
                    print("Col #%d, Row #%d" % (i, j))
                
                    #TODO add some sort of timer here to support constant keycode send
                    while not col.value:
                        pass # wait for ungrounded
                    
                    # Get HID keycode for the pressed key
                    key = kb_map.pmap_to_kmap(self.key_row.index(row), self.key_col.index(col)) 
                    if key == None:
                        print("Key not mapped to anything..")
                        continue

                    self.kbd.send(key)
                row.value = True
            
    #TODO
    def update(self):
        # TODO: Get new GPIO pin map read and insert into keyboard scan
        # Note: Consider adding custom keyboard strokes not part of layout. 
        #keyboard_scan()
        print("Update")
