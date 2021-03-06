# This class maps the VIC-20 pinmap to a keymap. 
# 
# pmap array is used for finding what key is pressed during a scan by mapping ports to pins.
# The gpio map is placed ontop of this array to find out what keycode to send.
#╔═══╦══════════╦════════╦═══════╦══════════════╦═════════╦══════╦═════════╦══════╦═════════╗
#║   ║ 0        ║ 1      ║ 2     ║ 3            ║ 4       ║ 5    ║ 6       ║ 7    ║ 8       ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ A ║ 1        ║ <-     ║ CTRL  ║ RUN/STOP     ║ SPACE   ║ LOGO ║ Q       ║ 2    ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ B ║ 3        ║ W      ║ A     ║ L SHIFT      ║ Z       ║ S    ║ E       ║ 4    ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ C ║ 5        ║ R      ║ D     ║ X            ║ C       ║ F    ║ T       ║ 6    ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ D ║ 7        ║ Y      ║ G     ║ V            ║ B       ║ H    ║ U       ║ 8    ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ E ║ 9        ║ I      ║ J     ║ N            ║ M       ║ K    ║ O       ║ 0    ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ F ║ +        ║ P      ║ L     ║ <            ║ >       ║ :    ║ @       ║ -    ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ G ║ £        ║ *      ║ ;     ║ ?            ║ H SHIFT ║ =    ║ UPARROW ║ HOME ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ H ║ DEL/INST ║ RETURN ║ CRSR  ║ CRSR UP/DOWN ║ F1      ║ F3   ║ F5      ║ F7   ║         ║
#╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
#║ I ║          ║        ║       ║              ║         ║      ║         ║      ║ Restore ║
#╚═══╩══════════╩════════╩═══════╩══════════════╩═════════╩══════╩═════════╩══════╩═════════╝
# Table generated from: https://www.tablesgenerator.com/text_tables#
#
# This is how the keyboard is connected From A-I and 0-8:
#========================
# "Pin number": "Cable Color" = "Port"
#
# 0:	Brown/White   = A
# 1:	Red/White     = B
# 2:	Orange/White  = C
# 3:	Yellow/White  = D
# 4:	Green/White   = E
# 5:	Blue/White    = F
# 6:	Purple/White  = G
# 7:	Gray/White    = H
# 8:	Brown         = 0
# 9:	Red           = 1
# 10:	Orange        = 2
# 11:	Yellow        = 3
# 12:	Green         = 4
# 13:	Blue          = 5
# 14:	Purple        = 6
# 15:	Gray          = 7
# 16:	Black         = 8
#
# 17:	White         = I
# 
# Author: Karl Strålman

class KeyboardHwLayout:
    def __init__(self, kmap):

        # pinmap
        self.pmap = [
            # Col:0            1            2            3            4            5            6            7       8
            [kmap[0][1],  kmap[0][0],  kmap[1][0],  kmap[2][0],  kmap[4][0],  kmap[3][0],  kmap[1][1],  kmap[0][2],  None], # A
            [kmap[0][3],  kmap[1][2],  kmap[2][2],  kmap[3][1],  kmap[3][2],  kmap[2][3],  kmap[1][3],  kmap[0][4],  None], # B
            [kmap[0][5],  kmap[1][4],  kmap[2][4],  kmap[3][3],  kmap[3][4],  kmap[2][5],  kmap[1][5],  kmap[0][6],  None], # C
            [kmap[0][7],  kmap[1][6],  kmap[2][6],  kmap[3][5],  kmap[3][6],  kmap[2][7],  kmap[1][7],  kmap[0][8],  None], # D
            [kmap[0][9],  kmap[1][8],  kmap[2][8],  kmap[3][7],  kmap[3][8],  kmap[2][9],  kmap[1][9],  kmap[0][10], None], # E
            [kmap[0][11], kmap[1][10], kmap[2][10], kmap[3][9],  kmap[3][10], kmap[2][11], kmap[1][11], kmap[0][12], None], # F
            [kmap[0][13], kmap[1][12], kmap[2][12], kmap[3][11], kmap[3][12], kmap[2][13], kmap[1][13], kmap[0][14], None], # G
            [kmap[0][15], kmap[2][14], kmap[3][14], kmap[3][13], kmap[0][16], kmap[1][15], kmap[2][15], kmap[3][15], None], # H
            [None,        None,        None,        None,        None,        None,        None,        None,        kmap[1][14]] # I
        ]

    def get_keycode(self, row, col):
        return self.pmap[row][col]
