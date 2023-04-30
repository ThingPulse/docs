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

## Sample project

We are working on a fully functional sample project to get you started in no time.
Until that is ready please see the `platformio.ini` file below for reference.
Furthermore, the touch module pin definitions are SDA=23, SCL=22.

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
