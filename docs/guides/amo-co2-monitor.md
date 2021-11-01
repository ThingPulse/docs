# AMo - CO<sub>2</sub> Monitor

How to use and configure the [ThingPulse AMo](https://thingpulse.com/product/amo-co2-monitor/) CO<sub>2</sub> monitor.

![](../img/products/ThingPulse-AMo-CO2-monitor.jpg)

## Using the AMo

The AMo is a true plug & play device. Connect it to a power source through the Micro-USB connector, turn it on, and you 
are good to go. The premium CO<sub>2</sub> sensor will self-calibrate within a couple of minutes.

**The 10second manual:** use the push button on right side to turn off/on acoustic warning.

Read on for the full manual.

### CO<sub>2</sub> readings on display

The way the measured CO<sub>2</sub> readings are displayed is specifically tuned to the characteristics of the 8x8 LED 
display. The values displayed by the AMo are 1/1000 of the actual reading rounded to 1 or 2 fractional digits 
omitting the leading 0. Consequently, the AMo will always display 2 digits in total (see examples below).

CO<sub>2</sub> is measured in "ppm", [parts per million](https://en.wikipedia.org/wiki/Parts-per_notation). Following 
the start of the Industrial Revolution, atmospheric CO<sub>2</sub> concentration increased to over 400 parts per 
million and continues to increase (causing the phenomenon of global warming). Hence, during normal operation you will 
not see readings below 400ppm. 

**Examples:**

- 603ppm → .60
- 613ppm → .61
- 615ppm → .62
- 994ppm → .99
- 995ppm → 1.0
- 1249ppm → 1.2
- 1250ppm → 1.3

### Monitoring CO<sub>2</sub> levels & alerting

The AMo uses a monitoring approach borrowed from traffic lights. Depending on the level of CO<sub>2</sub> the 
background color on the display changes from green to yellow and then to red. In addition, at the yellow and red stages 
the screen flashes slowly or quickly respectively. On top of that the integrated speaker beeps every 10s when
CO<sub>2</sub> concentration reached the red level. See table below.

There is an ongoing scientific debate as to what the "healthy" indoor CO<sub>2</sub> range is i.e. at what level you
should ventilate your office, classroom, restaurant, etc. As long as clear guidelines are missing ThingPulse decided to
configure the AMo with conservative (i.e. cautious) defaults.

Side note: effects of too much CO<sub>2</sub> (or too little oxygen actually) include fatigue and headache.

| CO<sub>2</sub> | color  | display flashing | acoustic warning |
|----------------|--------|------------------| -----------------|
|  <850ppm       | <span style="background-color: #008000; color: white;">green</span>  | -                | -                |
|  850-1000ppm   | <span style="background-color: #FFD700; color: white;">yellow | slow             | -                |
|  >1000ppm      | <span style="background-color: #FF0000; color: white;">red    | quick            | every 10s        |

### Turning off acoustic alerting

We understand that in certain environments it may be undesirable to disturb occupants with acoustic alerts. Using the 
push button on the right side allows to turn it off - and on again. After pushing the button the AMo will briefly
display one of the two speaker icons below to indicate whether acoustic alerting is off or on.

![acoustic alerting off](../img/products/speaker-off.png "acoustic alerting off")
![acoustic alerting on](../img/products/speaker-on.png "acoustic alerting on")

## Mobile apps

AMo is a fully compliant Sensirion Smart Gadget. Install the MyAmbience app for iOS and Android to visualize and 
monitor sensor data on your mobile device.

![MyAmbience app](../img/products/MyAmbience-app.webp "acoustic alerting on")

[![download from App Store](../img/products/AppStore.svg "download from App Store")](https://apps.apple.com/de/app/sensirion-myambience/id1529131572)
[![download from Play Store](../img/products/PlayStore.svg "download from Play Store")](https://play.google.com/store/apps/details?id=com.sensirion.myam&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)

## Configuring the AMo

Should you want to adjust the monitoring levels, LED brightness or speaker volume you can download and run the 
[ThingPulse App Fairy](https://github.com/ThingPulse/app-fairy) application. It will completely replace the existing
firmware with the one you configured in the App Fairy. 

!!! warning
    Proceed with caution! Although the process is fairly simple and robust malfunctions can not be ruled out. Reach out 
    to us if you get stuck.

- As a precondition please [install](/how-tos/install-drivers/) the Silicon Labs Serial-to-USB driver on your computer 
  or Mac.
- Connect the AMo to your computer or Mac over USB and turn it on.
- Start the App Fairy.
- Select "Icon64" as device type and "CO2 Monitor" as application.
- In the configuration dialog enter `scd4x` for sensor type
