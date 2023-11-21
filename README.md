# vic-kb-shield
`vic-kb-shield` is a replacement VIC-20 keyboard shield controlled by a Raspberry Pi Pico running ZMK.
(No VIC-20 computers were harmed in the process).

[ZMK](https://zmk.dev/) is a popular alternative to [QMK](https://docs.qmk.fm/#/), both open-source
keyboard controller firmware.
*Shield* is [terminology](https://zmk.dev/docs/development/boards-shields-keymaps) from ZMK, meaning a dumb dumb shell of a keyboard that any MCU can connect to and control. Not a fully self-contained keyboard.

The ZMK config for this shield is named `vic_20` and can be found [here](https://github.com/kjeller/zmk-config).

`TODO: Upload KiCad PCB here`

# Keyboard shield and keyboard traces

![Alt text](img/keyboard_pcb.jpg?raw=true "VIC-20 USB keyboard")

![Alt text](img/vic-20-keyboard-trace.png?raw=true "Keyboard trace")

A table derived from the keyboard trace:
```
╔═══╦══════════╦════════╦═══════╦══════════════╦═════════╦══════╦═════════╦══════╦═════════╗
║   ║ 0        ║ 1      ║ 2     ║ 3            ║ 4       ║ 5    ║ 6       ║ 7    ║ 8       ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ A ║ 1        ║ <-     ║ CTRL  ║ RUN/STOP     ║ SPACE   ║ LOGO ║ Q       ║ 2    ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ B ║ 3        ║ W      ║ A     ║ L SHIFT      ║ Z       ║ S    ║ E       ║ 4    ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ C ║ 5        ║ R      ║ D     ║ X            ║ C       ║ F    ║ T       ║ 6    ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ D ║ 7        ║ Y      ║ G     ║ V            ║ B       ║ H    ║ U       ║ 8    ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ E ║ 9        ║ I      ║ J     ║ N            ║ M       ║ K    ║ O       ║ 0    ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ F ║ +        ║ P      ║ L     ║ <            ║ >       ║ :    ║ @       ║ -    ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ G ║ £        ║ *      ║ ;     ║ ?            ║ H SHIFT ║ =    ║ UPARROW ║ HOME ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ H ║ DEL/INST ║ RETURN ║ CRSR  ║ CRSR UP/DOWN ║ F1      ║ F3   ║ F5      ║ F7   ║         ║
╠═══╬══════════╬════════╬═══════╬══════════════╬═════════╬══════╬═════════╬══════╬═════════╣
║ I ║          ║        ║       ║              ║         ║      ║         ║      ║ Restore ║
╚═══╩══════════╩════════╩═══════╩══════════════╩═════════╩══════╩═════════╩══════╩═════════╝
Table generated from: https://www.tablesgenerator.com/text_tables#
```
