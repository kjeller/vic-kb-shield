# Keyboard layout for VIC-20
#
# VIC-20 keyboard layout is not exactly mapped 1:1 to a modern keyboard
# which means some keys e.g. "Run stop" is mapped to the corrsponding key position on a 
# normal keyboard, in this case "Shift".
#
# Author: Karl Strålman

from adafruit_hid.keycode import Keycode as KC

# Unused keycode to be used on keys that I am not sure what to map to,
# e.g. "pi" key and "CRSR"
KC_EMPTY = 0x00

# Keymap that maps keys in a "logical" way to HID keycodes 
# Each row corresponds to a row on the VIC-20 from top to bottom.
vic_20_layout = [
        [KC.ESCAPE, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.MINUS, KC.EQUALS, KC_EMPTY, KC.HOME, KC.DELETE, KC.F1],
        [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LEFT_BRACKET, KC.RIGHT_BRACKET, KC_EMPTY, KC.BACKSPACE, KC.F3],
        [KC.LEFT_SHIFT, KC.CAPS_LOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE, KC.POUND, KC.ENTER, KC.F5],
        [KC.LEFT_CONTROL, KC.COMMAND, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.PERIOD, KC.FORWARD_SLASH, KC.RIGHT_SHIFT, KC.RIGHT_ALT, KC.RIGHT_CONTROL, KC.F7],
        [KC.SPACE]
    ]
