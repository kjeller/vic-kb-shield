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

from kb_key import Key

class KeyboardHwLayout:
    def __init__(self, kmap):

        # keymap
        self.kmap = kmap

        # pinmap
        # Maps key positions based on col and row from keytrace
        self.pmap = [
            # Col:0      1           2           3           4           5           6           7           8
            [Key(0, 1),  Key(0, 0),  Key(1, 0),  Key(2, 0),  Key(4, 0),  Key(3, 0),  Key(1, 1),  Key(0, 2),  None], # A
            [Key(0, 3),  Key(1, 2),  Key(2, 2),  Key(3, 1),  Key(3, 2),  Key(2, 3),  Key(1, 3),  Key(0, 4),  None], # B
            [Key(0, 5),  Key(1, 4),  Key(2, 4),  Key(3, 3),  Key(3, 4),  Key(2, 5),  Key(1, 5),  Key(0, 6),  None], # C
            [Key(0, 7),  Key(1, 6),  Key(2, 6),  Key(3, 5),  Key(3, 6),  Key(2, 7),  Key(1, 7),  Key(0, 8),  None], # D
            [Key(0, 9),  Key(1, 8),  Key(2, 8),  Key(3, 7),  Key(3, 8),  Key(2, 9),  Key(1, 9),  Key(0, 10), None], # E
            [Key(0, 11), Key(1, 10), Key(2, 10), Key(3, 9),  Key(3, 10), Key(2, 11), Key(1, 11), Key(0, 12), None], # F
            [Key(0, 13), Key(1, 12), Key(2, 12), Key(3, 11), Key(3, 12), Key(2, 13), Key(1, 13), Key(0, 14), None], # G
            [Key(0, 15), Key(2, 14), Key(3, 14), Key(3, 13), Key(0, 16), Key(1, 15), Key(2, 15), Key(3, 15), None], # H
            [None,       None,       None,       None,       None,       None,       None,       None,       Key(1, 14)] # I
        ]

    def get_mapped_key(self, key, layer):
        mapped_key = self.pmap[key.row][key.col]
        return self.kmap[layer][mapped_key.row][mapped_key.col]

    def get_keymap(self, map, layer):
        keymap = []
        for key in map:
            mapped_key = self.get_mapped_key(key, layer)
            if mapped_key:
                keymap.append(mapped_key)
        return keymap