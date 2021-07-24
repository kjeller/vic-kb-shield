# vic-py-kb
VIC-20 keyboard controlled by Raspberry Pi Pico using CircuitPython.

Keyboard trace of the VIC-20 keyboard:
![Alt text](img/vic-20-keyboard-trace.png?raw=true "Keyboard trace")

How it currently looks:
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

# FDG
- The keyboard case needs an internal holder for the rpi pico (mounted on the screws on the pcb plate)
- Rewrite adafruit hid to enable name change of USB HID device in initial report.
- Layers! (QMK-like)
