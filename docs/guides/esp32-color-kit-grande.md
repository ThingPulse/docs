# ESP32 Color Kit Grande



How to assemble and program the [ThingPulse ESP32 WiFi Color Display Kit Grande](https://thingpulse.com/product/esp32-wifi-color-display-kit-grande/).

!!! warning

    2023-05-01 this guide is very much work in progress.
    It will be updated & extended over the course of the next few weeks.

!!! note

    It is advisable to read these instructions carefully *before* you start soldering.
    In particular please make sure that you have all parts and tools ready.

In addition to the components in the kit you will need:

- [soldering iron](https://thingpulse.com/go/soldering-iron/)
- solder
- tweezers

## Assembling the hardware

There are different ways to skin a cat.
The recipe below is what we think is most sensible for most people.
Read it, take a step back, read it again and see if it makes sense for you, too.
Feel free to adjust it if it does not.

As seen on our product page in the shop the intention is for the ESP32 microcontroller board to be pluggable rather than soldered to the connector PCB.
If you are concerned about the little extra height this adds to the whole assembly, you may of course solder the ESP32 board directly to the connector PCB using the male pin headers.
You might need to cut off the pin headers on the other side of the connector PCB such that they will not touch the display module.

1. Cut the female pin headers to length and solder them to the connector PCB.
See video tutorial below.
2. OPTIONAL but recommended: solder on/off switch to PCB.
Will be tricky to add later after the display module is attached to the PCB.
3. OPTIONAL: solder Grove connector to PCB.
See "SMD soldering" video tutorial below.
Can easily be added later anytime.
4. Cut the male pin headers to length and solder them to the ESP32 board.
5. Peel off the protective film on one side of the four foam stickers and attach them to the front of the connector PCB in the designated areas ("TAPE").
6. Place the display on a clean surface upside down (as to not scratch it).
7. Feed the two FPC cables of the display module through the cut-outs of the PCB.
Do not insert the cables into the sockets yet.
8. Flip the two pieces over to verify everything fits.
9. Remove the display module again.
10. Remove the remaining protective film from the foam stickers.
11. Feed the FPC cables of the display module through the PCB and attach the display module such that it aligns with the markings on the PCB (while silk screen).

General introduction to working with pin headers incl. how to solder them.
[![YouTube pin headers video](https://i.ytimg.com/vi/qz9Ryos1_GY/hqdefault.jpg)](https://youtu.be/qz9Ryos1_GY "Pin Headers - soldering, cutting, male, female, etc.")

Detailed instructions how to solder SMD components.
Recommended for soldering the Grove connector if you have never done any SMD soldering before.
[![YouTube SMD soldering video](https://i.ytimg.com/vi/EW9Y8rDm4kE/hqdefault.jpg)](https://youtu.be/EW9Y8rDm4kE "How To Solder SMD Correctly - Part 1 /SMD Soldering Tutorial")

## Development environment
We will be working with a **PlatformIO** development environment in **Visual Studio Code**.
If you have never worked with PlatformIO please install it as per their [installation instructions](https://platformio.org/install/ide?install=vscode).
Once done, walk through their minial "Getting Started" section.

## Sample project

We are working on a fully functional sample project to get you started in no time.
Until that is ready please see the `platformio.ini` file below for reference.
Furthermore, the touch module pin definitions are SDA=23, SCL=22.

!!! tip

    If you want to follow the development of said sample project, take a look at the `dev` branch on GitHub at https://github.com/ThingPulse/esp32-weather-station-touch/tree/dev

```ini
; PlatformIO Project Configuration File for ThingPulse Color Kit Grande
;
; Documentation: https://docs.thingpulse.com/guides/esp32-color-kit-grande/
;
; Additional PlatformIO options and examples: https://docs.platformio.org/page/projectconf.html

[env:thingpulse-color-kit-grande]
platform = espressif32@~6.1.0
board = esp-wrover-kit
framework = arduino
; Adjust port and speed to your system and its capabilities e.g. "upload_port = COM3" on Windows.
; To list all availble ports you may also run 'pio device list' in the Visual Studio Code terminal window.
upload_port = /dev/tty.wchusbserial54790238451
monitor_port = /dev/tty.wchusbserial54790238451
monitor_speed = 115200
; For your OS & driver combination you might have to lower this to 921600 or even 460800.
upload_speed = 1500000
monitor_filters = esp32_exception_decoder, time
build_flags =
  ; core flags
  -DCORE_DEBUG_LEVEL=3
  -DBOARD_HAS_PSRAM
  -mfix-esp32-psram-cache-issue
  ; TFT_eSPI flags
  ; Below we replicate the flags from TFT_eSPI/User_Setups/Setup21_ILI9488.h.
  ; You can't mix'n match from their .h and -D here.
  -D USER_SETUP_LOADED=1 # 1 => will not load User_Setup.h from TFT_eSPI but rely on the flags defined here
  -D ILI9488_DRIVER=1
  -D TFT_MISO=19
  -D TFT_MOSI=18
  -D TFT_SCLK=05
  -D TFT_CS=15
  -D TFT_DC=2
  -D TFT_RST=4
  -D TFT_BL=32
  ; As we're using OpenFontRender we don't need any of the TFT_eSPI built-in fonts.
  ; Font descriptions at TFT_eSPI/User_Setups/Setup21_ILI9488.h
  -D LOAD_GLCD=0
  -D LOAD_FONT2=0
  -D LOAD_FONT4=0
  -D LOAD_FONT6=0
  -D LOAD_FONT7=0
  -D LOAD_FONT8=0
  -D LOAD_GFXFF=0
  -D SMOOTH_FONT=1
  -D SPI_FREQUENCY=27000000
  ; required if you include OpenFontRender and build on macOS
  -I /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/**
board_build.partitions = no_ota.csv
board_build.filesystem = littlefs
lib_deps =
  bodmer/TFT_eSPI@~2.5.23
  https://github.com/Bodmer/OpenFontRender#96a29bc ; no tags or releases to reference :( -> pin to Git revision
```
