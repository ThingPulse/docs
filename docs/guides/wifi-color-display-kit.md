# WiFi Color Display Kit

How to assemble and program the ThingPulse ESP8266 WiFi Color Display Kit. 

---

!!! note

    It is advisable to read these instructions carefully *before* you start soldering. In particular please make sure that you have all parts and tools ready.

In addition to the components in the kit you will need:

- soldering iron
- solder
- insulating/electrical/duct tape
- cutting pliers or desoldering braid to remove the SD card holder

## Preparation

### Material inspection
Here is the list of parts: display module (left), custom PCB (bottom right), WeMos D1 mini Pro (top middle) and the two pin header rows.

![](../img/guides/wifi-color-display-kit/1-components.jpg)

### Dry run assembly
Stack the parts up as shown below without soldering and adjust it until it makes sense.

While you *could* insert the pin headers into the D1 mini like in the picture consider this: if you turned them upside down and inserted them with the longer end from underneath the D1 mini, this would allow you to later add an extension shield on top (there's a picture below). If you do not need that flexibility and want to place the pin headers like in the picture then you need to solder them to the D1 mini *first*. D1 mini-plus-headers are then soldered to the PCB. Otherwise the order is reversed.

![](../img/guides/wifi-color-display-kit/2-dry-run-stack.jpg)

### Prepare display module

In order to have a stack which uses the least amount of space you will want to modify the display module a bit. The SD card holder has to go, sorry. Depending on your (de)soldering skills you can either use a desoldering braid or just cut the SD card holder off of the module with pointy cutting pliers.

![](../img/guides/wifi-color-display-kit/3-cut-off-sd-card-slot.jpg)

### Short circuit prevention

To prevent the D1 mini from accidentally causing a short circuit with the display board you can tape off the area below the connector board.

![](../img/guides/wifi-color-display-kit/4-protect-with-tape.jpg)

## Soldering

### Connect PCB and D1 mini

The options of which way to place the pin headers between PCB and the D1 mini were discussed earlier; hope you made up your mind. To achieve what you see below the recommended steps are as follows:

- stack the parts up as shown
- hold the stack between your fingers and flip it over
- solder the pins to the PCB from the back
- flip the stack back and solder the D1 mini from the top

![](../img/guides/wifi-color-display-kit/5-WeMos-D1-mini-on-PCB.jpg)

### Connect PCB to display

In the last step of the hardware setup you will solder the connector PCB to the display as shown below.

![](../img/guides/wifi-color-display-kit/6-solder-connector-PCB-to-display-PCB.jpg)

Here is a speed-up video with all the steps above. Note how PCB and display are connected in a more "space-generous" way.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7fbGS4MjoMk?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Development Environment Setup

### Install drivers
{!../includes/install-drivers.md!}

## Weather Station Color Code

tbd