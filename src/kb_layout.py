# Keyboard layout for VIC-20
#
# VIC-20 keyboard layout is not exactly mapped 1:1 to a modern keyboard
# which means some keys e.g. "Run stop" is mapped to the corrsponding key position on a 
# normal keyboard, in this case "Shift".
#
# Author: Karl Strålman

from kb_macros import ANSI
from kb_macros import MISC
from kb_key import Key
from adafruit_hid.keycode import Keycode as KC

# Unused keycode to be used on keys that I am not sure what to map to,
# e.g. "pi" key and "CRSR"
# (0x00 is reserved to indicate no event)
__NA__ = 0x00

KC_LAYER_INC_KEY_POS = Key(7, 2) # maps to "CRSR ->/<-" button
KC_MACRO_LAYER = 3

# Toggle keyboard layours by pressing "CRSR"
# Extended key layer is used to press keys not included in original layout
extended_key_layer = [
    [
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F2],
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F4],
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.LEFT_ARROW, KC.DOWN_ARROW, KC.UP_ARROW, KC.RIGHT_ARROW, __NA__, __NA__, __NA__, __NA__, KC.F6],
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F8],
        [__NA__]
    ],
    [
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F9],
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F10],
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F11],
        [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, KC.F12],
        [__NA__]
    ],
]

# The macro key layer is used for firing a keyboard event e.g. send a string of text
macro_key_layer = [
    [__NA__, ANSI.BLK, ANSI.WHT, ANSI.RED, ANSI.CYN, ANSI.PUR, ANSI.GRN, ANSI.BLU, ANSI.YEL, __NA__, __NA__, __NA__, __NA__, MISC.POUND, __NA__, __NA__, __NA__],
    [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, MISC.PI, __NA__],
    [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__],
    [__NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__, __NA__],
    [__NA__]
]

# Keymap that maps keys in a "logical" way to HID keycodes 
# Each row corresponds to a row on the VIC-20 from top to bottom.
vic_20_layout = [
    [   # Layer 0
        [KC.ESCAPE, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.MINUS, KC.EQUALS, KC.INSERT, KC.HOME, KC.DELETE, KC.F1],
        [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LEFT_BRACKET, KC.RIGHT_BRACKET, __NA__, KC.BACKSPACE, KC.F3],
        [KC.LEFT_SHIFT, KC.CAPS_LOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE, KC.POUND, KC.ENTER, KC.F5],
        [KC.LEFT_CONTROL, KC.COMMAND, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.PERIOD, KC.FORWARD_SLASH, KC.RIGHT_SHIFT, KC.RIGHT_ALT, KC.RIGHT_CONTROL, KC.F7],
        [KC.SPACEBAR]
    ],
    [extended_key_layer[0]], # Layer 1
    [extended_key_layer[1]], # Layer 2
    [macro_key_layer[0]]     # Layer 3 (Macro layer)
]