# vic-py-kb
VIC-20 keyboard controlled by Raspberry Pi Pico using CircuitPython.
![Alt text](img/keyboard_no_case.jpg?raw=true "VIC-20 USB keyboard")
# Setup/Installation
1. Donwload Circuitpython 6.3 (or later, make sure that Adafruit HID lib is using the correct version) from https://circuitpython.org/board/raspberry_pi_pico/
2. Move .uf2 file to the RPI Pico and wait for the device to install it
Now Circuitpython should be installed correctly.

3. Download 6.X of Adafruit HID library from here: https://github.com/adafruit/Adafruit_CircuitPython_HID/releases
    e.g. adafruit-circuitpython-hid-6.x-mpy-5.0.1.zip
4. Extract and move adafruit-circuitpython-hid-6.x-mpy-5.0.1/lib/adafruit_hid to /lib on the RPI
5. Move all source files to pico
6. Restart pico
When connected to an OS with USB HID compatibility, vic-py-kb should be recognized as a USB keyboard.
# Keyboard trace
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
# Keymap, Pinmap and key layout..
The keymap maps to the actual USB HID codes that are determined by what keylayout is in use. The pinmap maps the keyboard trace table to key positions that are traceable to gpio pins configured in code.py

# FDG
- The keyboard case needs an internal holder for the rpi pico (mounted on the screws on the pcb plate)
- Rewrite adafruit hid to enable name change of USB HID device in initial report.
- Layers! (QMK-like)
