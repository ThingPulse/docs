A tool chain is the set of tools that lets you compile and create binaries for a certain platform. Since we want to 
create binaries for the ESP8266 we need a different tool chain than the one that comes with the plain vanilla Arduino
 IDE. One of its wonderful feature is the Board Manager. It lets you install support for many different chips and 
 boards with just a few clicks.
 
 - In the Arduino IDE open the preferences/settings and enter http://arduino.esp8266.com/stable/package_esp8266com_index.json 
 into the text box ==Additional Board Manager URLs==.
 - Now go to ==Tools== > ==Board: ...== > ==Boards Manager...==, search for the "ESP8266" board and click ==Install==. **Note:** ThingPulse does not recommended to install beta or RC versions. For the Color Kit the currently recommended version is 2.4.2 due to a [bug in the touch library](https://github.com/PaulStoffregen/XPT2046_Touchscreen/pull/24#issuecomment-514809229).
 - Take a break until the installer finishes.

![Arduino IDE board manager ESP8266](/img/how-tos/Arduino-board-manager-ESP8266.png)

From time to time you want to come back to the Board Manager and make sure that you have the latest __non-beta non-RC__ version of the 
ESP8266 tool chain installed. To do that simply click on the ESP8266 entry and select the latest version from the 
dropdown. Then hit ==Update==.
