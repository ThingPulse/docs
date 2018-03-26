The Arduino IDE knowing about ESP8266 modules in general is not enough as they are not all the same. There are subtle 
but important differences as for available flash memory and how they can be programmed. The selection of the correct 
board also defines the names of the GPIO pins. The designers of the NodeMCU module for example decided to introduce a 
completely new naming scheme for the pins. Instead of calling them `GPIO1`, `GPIO2`, etc. they relabeled them and 
prefixed each one with “D”. `D0` is GPIO16, `D1` is GPIO5 and so on. By selecting a specific board in the Arduino IDE 
you automatically have the correct naming scheme and other relevant parameters available,. This helps a lot as for 
the NodeMCU modules for example those names are also printed on the PCB.

Not all ThingPulse kits come with the same ESP8266 chips/modules. We carefully selected the best option for each kit.
 It's essential that you know which module you get with a specific kit so you can configure Arduino IDE correctly

- [Starter Kit](https://thingpulse.com/product/esp8266-iot-electronics-starter-kit-weatherstation-planespotter-worldclock/) --> NodeMCU 1.0 aka v2
- [Color Display Kit](https://thingpulse.com/product/esp8266-wifi-color-display-kit-2-4/) --> WeMos D1 mini (Pro)
- [ESPaper Kits](https://thingpulse.com/product-category/espaper-epaper-kits/) --> Generic ESP8266

In the Arduino IDE do as follows:

==Tools== > ==Board: *== > select as per the above list 

In an earlier step you installed drivers for the USB-to-Serial converter. If everything went well and the device is 
plugged into your computer you should now be able to select the serial connection. It should show up in the Menu 
under ==Tools== > ==Port==. On macOS the serial devices are called `/dev/cu.xxx`. On a PC it should be listed 
as a COM port labelled `COM#` (where # is some number).

If you cannot see your device in the port list, try to unplug it and re-plug it after a few seconds. Also try a 
different USB socket. If that does not help try restarting your computer and/or try with a different USB cable.
