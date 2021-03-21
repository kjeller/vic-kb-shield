# Keyboard macros are events that can be triggered from selecting the macro layer,
# using the built-in layer functionality, and pressing a macro key. 
# Macro keyevents allow you to send multiple keystrokes when pressing just one key.
# Macro keyevents are defined in this file whereas the layout (where macro keys are placed) is set in kb_layout
#
# Author: Karl Strålman

# Key macros for entering ANSI color codes (thanks for the idea @martinkauppinen!)
class ANSI:
    BLK = "\e[0;30m" # Black
    RED = "\e[0;31m" # Red
    GRN = "\e[0;32m" # Green
    YEL = "\e[0;33m" # Yellow
    BLU = "\e[0;34m" # Blue
    PUR = "\e[0;35m" # Purple
    CYN = "\e[0;36m" # Cyan
    WHT = "\e[0;37m" # White

class MISC:
    POUND = "£"
    PI = "π"