# ESP32 Color Kit Grande



How to assemble and program the [ThingPulse ESP32 WiFi Color Display Kit Grande](https://thingpulse.com/product/esp32-wifi-color-display-kit-grande/).

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

1. Cut the female pin headers strips to length (12 & 16 pins) and solder them to the connector PCB.
See video tutorial below.
2. OPTIONAL but recommended: solder on/off switch to PCB.
Will be tricky to add later after the display module is attached to the PCB.
3. OPTIONAL: solder Grove connector to PCB.
See "SMD soldering" video tutorial below.
Can easily be added later anytime.
4. Cut the male pin headers strips to length (12 & 16 pins) and solder them to the ESP32 board.
5. Peel off the protective film on one side of the four foam stickers and attach them to the front of the connector PCB in the designated areas ("TAPE").
6. Place the display on a clean surface upside down (as to not scratch it).
7. Feed the two FPC cables of the display module through the cut-outs of the PCB.
Do not insert the cables into the sockets yet.
8. Flip the two pieces over to verify everything fits.
9. Remove the display module again.
10. Remove the remaining protective film from the foam stickers.
11. Feed the FPC cables of the display module through the PCB and attach the display module such that it aligns with the markings on the PCB (while silk screen).

Assembly video
<iframe width="480" height="300" src="https://www.youtube.com/embed/VhBRtyJvOQ0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

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

With all the soldering done we will turn to the Weather Station Touch project.

### Obtain the code

The WiFi Color Kit project is, as all of ThingPulse's open-source code, publicly accessible on GitHub.
Hence, there are two options to download the code:

- Clone the repository with Git: `git clone https://github.com/ThingPulse/esp32-weather-station-touch`
- Download the sources from https://github.com/ThingPulse/esp32-weather-station-touch/archive/master.zip and unpack
  them somewhere to your local file system.

### Open project in Visual Studio Code

- Start the Arduino IDE
- ==File== > ==Open Folder...==
- find and select the `esp32-weather-station-touch` folder from the previous step.

### Configuration & customization

Open the `src/settings.h` file and adjust the two handful of configuration parameters in the "User settings" section at the top.
They are all documented _inside_ the file directly.
Everything should be self-explanatory.
Most importantly you will need to set the OpenWeatherMap API key ([how to get key](../how-tos/openweathermap-key.md)).

### Upload code to device

- Hit the PlatformIO icon on the navigation bar on the left side (alien face).
- Select the ==Platform== > ==Upload Filesystem Image== task. You only need to do this once.
- Select the ==General== > ==Upload and Monitor== task. You do this **every time you change code or configuration**.
