# Main entry of vic-py-kb.
#
# Author: Karl Strålman

import kb
import kb_map
import kb_layout
import board

# The logic high or low will be written on gpio_row and be read from gpio_col
# See kb.py keyboard_scan() for the keyboard scan implementation.
gpio_row = [board.GP0, 
            board.GP1, 
            board.GP2, 
            board.GP3, 
            board.GP4, 
            board.GP5, 
            board.GP6, 
            board.GP7, 
            board.GP8]

# Index 0, 1, 2 maps to col 0, 1, 2 etc. in kb_hw_map
gpio_col = [board.GP9, 
            board.GP10,
            board.GP11, 
            board.GP12, 
            board.GP13, 
            board.GP14, 
            board.GP15, 
            board.GP16, 
            board.GP17, 
            board.GP18, 
            board.GP19]

keyboard = kb.KeyboardImpl("VIC-20", gpio_row, gpio_col, kb_layout.vic_20_layout)

while True:
    keyboard.update()