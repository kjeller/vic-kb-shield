# code.py is the main entry to the program.
# Author: Karl Strålman

import kb
import kb_map
import time

keyboard = kb.KeyboardImpl(name="VIC-20")

while True:
    keyboard.update()