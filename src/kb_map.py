# Keymap to hardware pin mappings are configured here.
# The kb_matrix table is the result of mapping pcb traces to pins.
# Pins are then mapped to GPIO ports which are then mapped to a keymap.
#
# FDG: Keyboard layers, would be cool.
#
#
# Author: Karl Strålman

from adafruit_hid.keycode import Keycode as KC
import board

# Unused keycode to be used on keys that I am not sure about
# like "pi" key and "CRSR"
________ = 0x00

# Keymap that maps keys in a "logical" way to HID keycodes 
kmap = 
[
    [KC.ESCAPE, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, _______, ________, ________, ________, ________, KC.F1],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, _______, ________, ________, KC.BACKSPACE, KC.F3],
    [KC.LEFT_SHIFT, KC.CAPS_LOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.J, KC.K, KC.L, ________, ________, ________, KC.ENTER, KC.F5],
    [KC.LEFT_CONTROL, KC.COMMAND, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.PERIOD, ________, KC.RIGHT_SHIFT, KC.RIGHT_ALT, KC.RIGHT_CONTROL, KC.F7],
    [KC.BACKSPACE]
]

# Code beyond this line is not understandable if you don't read kb_matrix document provided in proj root.
#--------------------------------------------

# Maps pinmap to keymap. This array is used for finding what key is pressed during a scan.
# The gpio map is placed ontop of this array to find out what keycode to send.

pmap = [
    [kmap[0][1],  kmap[0][0],  kmap[1][0],  kmap[2][0],  kmap[4][0],  kmap[3][0],  kmap[1][1],  kmap[0][2],  None], # A
    [kmap[0][3],  kmap[1][2],  kmap[2][2],  kmap[3][1],  kmap[3][2],  kmap[2][3],  kmap[1][3],  kmap[0][4],  None], # B
    [kmap[0][5],  kmap[1][3],  kmap[2][4],  kmap[3][3],  kmap[3][4],  kmap[2][5],  kmap[1][5],  kmap[0][6],  None], # C
    [kmap[0][7],  kmap[1][6],  kmap[2][6],  kmap[3][5],  kmap[3][6],  kmap[2][6],  kmap[1][6],  kmap[0][8],  None], # D
    [kmap[0][9],  kmap[1][8],  kmap[2][8],  kmap[3][7],  kmap[3][8],  kmap[2][10], kmap[1][7],  kmap[0][10], None], # E
    [kmap[0][11], kmap[1][10], kmap[2][10], kmap[3][9],  kmap[3][10], kmap[2][12], kmap[1][8],  kmap[0][12], None], # F
    [kmap[0][13], kmap[1][12], kmap[2][12], kmap[3][11], kmap[3][12], kmap[2][14], kmap[1][9],  kmap[0][14], None], # G
    [kmap[0][15], kmap[2][15], kmap[3][14], kmap[3][13], kmap[0][16], kmap[1][15], kmap[2][16], kmap[3][15], None], # H
    [None,        None,        None,        None,        None,        None,        None,        None,        kmap[1][14]] # I
]

def pmap_to_kmap(row, col):
    return pmap[row][col]
