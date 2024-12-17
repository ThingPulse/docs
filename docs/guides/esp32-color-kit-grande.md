# ESP32 Color Kit Grande



How to assemble and program the [ThingPulse ESP32 WiFi Color Display Kit Grande](https://thingpulse.com/product/esp32-wifi-color-display-kit-grande/).

[![Color Kit Grande with sample application: weather station](https://thingpulse.com/wp-content/uploads/2022/10/ThingPulse-Color-Kit-Grand-with-sample-application.jpg)](https://thingpulse.com/product/esp32-wifi-color-display-kit-grande/)

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

!!! note

    See the [dedicated chapter below](#operating-the-fpc-connectors) about how to open & close the FPC connectors.

!!! danger

    Handle the delicate display unit and its FPC ribbons with extra care.
    Be sure to NOT sharply bend (i.e. fold), pull or otherwise apply stress to the ribbon cables and their connection to the unit.



| [![](../img/guides/color-kit-grande/1_40female_split.png)](../img/guides/color-kit-grande/1_40female_split.png) | Cut the female pin headers strips to length (12 & 16 pins) and solder them to the connector PCB. |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [![](../img/guides/color-kit-grande/2_power_switch_1.png)](../img/guides/color-kit-grande/2_power_switch_1.png) | OPTIONAL but recommended: solder the on/off switch to PCB. |
| [![](../img/guides/color-kit-grande/3_grove_connector.png)](../img/guides/color-kit-grande/3_grove_connector.png) | OPTIONAL: solder the Grove connector to the PCB. See "SMD soldering" video tutorial below (collapsible section). Can easily be added later anytime. |
| [![](../img/guides/color-kit-grande/4_male_pin_1.png)](../img/guides/color-kit-grande/4_male_pin_1.png) |  Cut the male pin headers strips to length (12 & 16 pins) |
|[![](../img/guides/color-kit-grande/4_male_pins_in_pos.png)](../img/guides/color-kit-grande/4_male_pins_in_pos.png) | Place the male into the already soldered female header pins for better stability |
|[![](../img/guides/color-kit-grande/4_male_pin_esp32_epulse.png)](../img/guides/color-kit-grande/4_male_pin_esp32_epulse.png) | Solder the headers to the ESP32 board. |
| [![](../img/guides/color-kit-grande/5_tapes.png)](../img/guides/color-kit-grande/5_tapes.png) |  Peel off the protective film on one side of the four foam stickers and attach them to the front of the connector PCB in the designated areas ("TAPE"). |
| [![](../img/guides/color-kit-grande/6_display.png)](../img/guides/color-kit-grande/6_display.png) |  Place the display on a clean surface upside down (as to not scratch it). |
| [![](../img/guides/color-kit-grande/7_FPC.png)](../img/guides/color-kit-grande/7_FPC.png)  |  Feed the two FPC cables of the display module through the cut-outs of the PCB. Insert the cables into the sockets. See the [dedicated chapter below](#operating-the-fpc-connectors) on how to correctly open & close the FPC connectors. Carefully(!) fold the display over such that it rests on the (still protected) foam pads and flip the two pieces over to verify everything fits. |
| [![](../img/guides/color-kit-grande/8_programm.png)](../img/guides/color-kit-grande/8_programm.png) |  Now would be a good time to proceed with the [software](#development-environment)/[firmware](#sample-project) installation as per the chapters below. You will want to do this now - rather than at the very end - to verify everything works *before* you attach the display. It will be hard to remove from the foam stickers once attached. |
| [![](../img/guides/color-kit-grande/10_protective.png)](../img/guides/color-kit-grande/10_protective.png)  |  Remove the remaining protective film from the foam stickers. |
| [![](../img/guides/color-kit-grande/11_align.png)](../img/guides/color-kit-grande/11_align.png)  |  Attach the display module such that it aligns with the markings on the PCB (white silk screen). |


<iframe width="480" height="300" src="https://www.youtube.com/embed/AL6-BsUyV6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

??? tip "Expand to show soldering tutorials"

    === "Working with pin headers"
        General introduction to working with pin headers incl. how to solder them.
        <iframe width="560" height="315" src="https://www.youtube.com/embed/qz9Ryos1_GY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

    === "Soldering SMD components"
        Detailed instructions how to solder SMD components.
        Recommended for soldering the Grove connector if you have never done any SMD soldering before.
        <iframe width="560" height="315" src="https://www.youtube.com/embed/EW9Y8rDm4kE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Operating the FPC connectors

The connectors for the two FPC cables (for display and touch module) can be a bit tricky to operate for the inexperienced.
The fact that the two types required here don't work the same does not help.

- The small one for the touch module has a black latch that opens if you gently lift it such that it will protrude from its base in a 90° angle.
- The large one for the display has a locking bar that runs along the full length of the connector.
It needs to be pulled away from its base parallel to the PCB.
*Use two fingers* to pull at the knobs on either end of the bar.

The following pictures indicate the open/closed positions.

| [![](../img/guides/color-kit-grande/FPC-connectors-open-empty.jpg)](../img/guides/color-kit-grande/FPC-connectors-open-empty.jpg) | [![](../img/guides/color-kit-grande/FPC-connectors-closed-empty.jpg)](../img/guides/color-kit-grande/FPC-connectors-closed-empty.jpg) |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [![](../img/guides/color-kit-grande/FPC-connectors-open.jpg)](../img/guides/color-kit-grande/FPC-connectors-open.jpg)             | [![](../img/guides/color-kit-grande/FPC-connectors-closed.jpg)](../img/guides/color-kit-grande/FPC-connectors-closed.jpg)             |

## Development environment
We will be working with a **PlatformIO** (PIO) development environment in **Visual Studio Code** (VS Code).
If you have never worked with PlatformIO, please install it as per their [installation instructions](https://docs.platformio.org/en/latest/integration/ide/vscode.html#installation).

0. [Download](https://code.visualstudio.com/) and install official Microsoft Visual Studio Code. PlatformIO IDE is built on top of it
1. Open VSCode Package Manager
2. Search for the official platformio ide extension
3. Install PlatformIO IDE.

![../img/how-tos/platformio-install.png](../img/how-tos/platformio-install.png)

Now please look at their [quick-start guide](https://docs.platformio.org/en/latest/integration/ide/vscode.html#quick-start):

[![](../img/how-tos/platformio-quickstart.png)](https://docs.platformio.org/en/latest/integration/ide/vscode.html#quick-start)

## The Weather Station Sample Project

With all the soldering done we will turn to the Weather Station Touch project.

### Obtain the code

The Weather Station sample project is, as all of ThingPulse's open-source code, publicly accessible on GitHub.
Hence, there are two options to download the code:

- Clone the repository with Git: `git clone https://github.com/ThingPulse/esp32-weather-station-touch`
- Download the sources from https://github.com/ThingPulse/esp32-weather-station-touch/archive/master.zip and unpack
  them somewhere to your local file system.

### Open project in Visual Studio Code

- Start VS Code
- ==File== > ==Open Folder...==
- Find and select the `esp32-weather-station-touch` folder from the previous step.

### Configuration & customization

Open the `src/settings.h` file and adjust the two handful of configuration parameters in the "User settings" section at the top.
They are all documented _inside_ the file directly.
Everything should be self-explanatory.
Most importantly you will need to set the OpenWeatherMap API key ([how to get key](../how-tos/openweathermap-key.md)).

### Upload the file system to device
- Hit the PlatformIO icon on the navigation bar on the left side (alien face).
- Select the ==Platform== > ==Upload Filesystem Image== task.
You only need to do this once if it succeeds.
Pay attention to the output in the VS Code console that opens.
If it reports any errors like e.g. if it cannot connect to the board or if stops midway, then repeat the process.

![../img/how-tos/platformio-filesystem.png](../img/how-tos/platformio-filesystem.png)

### Upload code to device

- Select the ==General== > ==Upload and Monitor== task.
You do this **every time you change code or configuration**. 

![../img/how-tos/platformio-task-upload.png](../img/how-tos/platformio-task-upload.png)

Alternatively you can also use the quick buttons from the footer:

![../img/how-tos/platformio-upload.png](../img/how-tos/platformio-upload.png)

!!! note

    Should the upload fail, please ensure your system has the necessary drivers for the CH9102 USB to serial converter installed.
    The best place for details and instructions is over at [Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102).

## Writing your own application

Use the code in our sample project as a starting point or reference to build your own application.
In particular, see the configuration in `platformio.ini` and `src/settings.h` for pin assignments.

### Touch interface

The sample application does not currently make use of the touch interface.
However, the code does initialize it to ensure it is wired up correctly (`display.h#initTouchScreen`).
Furthermore, there is a commented out snippet at the end of `loop()` that shows how to obtain touch coordinates.

## Hardware extensions / pin assigment

We designed the connector PCB with extensibility in mind.

- You may plug [any I2C Groove module](https://wiki.seeedstudio.com/Grove_System/) into the connector you soldered to the PCB.
The **SCL/SDA pins are 22 and 23** respectively.
- Many of the broken out pins are available for custom extensions.
**Free pins as follows**.
Please see the [Espressif datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf#page=12) for details on those pins.
    - P2 row: 26, 25, 34, 39, 36, 19, RX, TX, 21
    - P3 row: 13, 12, 33, 14
