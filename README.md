# vic-py-kb
VIC-20 keyboard controlled by Raspberry Pi Pico using CircuitPython.

Keyboard trace of the VIC-20 keyboard:
![Alt text](img/vic-20-keyboard-trace.png?raw=true "Keyboard trace")

How it currently looks:
![Alt text](img/keyboard_no_case.jpg?raw=true "VIC-20 USB keyboard")

# Setup/Installation
Install circuitpython on the rpi pico beforehand.

1. Download latest release of the adafruit hid library from here: https://github.com/adafruit/Adafruit_CircuitPython_HID.git
2. Add to lib folder on pico
3. Move all source files to pico
4. Restart pico.
When connected to a OS with USB HID compatibility, vic-py-kb should be recognized as a USB keyboard.

# FDG
- The keyboard case needs an internal holder for the rpi pico (mounted on the screws on the pcb plate)
- Rewrite adafruit hid to enable name change of USB HID device in initial report.
- Layers! (QMK-like)
