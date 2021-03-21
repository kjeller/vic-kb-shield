# This class is used to describe a key at an arbritary position.
# It is both used to describe both the pinmap and keymap, and is
# used to map key positions to keycodes or macros depending on what
# currently active layer is used.
#
# Author: Karl Strålman

class Key:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col