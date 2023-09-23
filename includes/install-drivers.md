A prerequisite to program ESP*-based modules usually is to establish a communications channel from your development platform (PC, Mac, Linux) to the device *over USB*. This in turn requires your system to detect the USB-to-Serial (aka USB-to-TTL, aka USB-to-UART) adapter on the ESP8266 or ESP32 module. There are two commonly used adapters in the wild these days:

- Silicon Labs CP210x
- Winchiphead CH340x / CH341x

Newer boards (2022+) often use the Winchiphead CH9102 chip.

Popular modules that use the CP210x are:

- NodeMCU v1.0 (i.e. V2) module
- WeMos D1 mini Pro (some revisions)
- [ThingPulse ePulse ESP32 dev board](https://thingpulse.com/product/epulse-low-power-esp32-development-board/)
- [ThingPulse Icon64](https://thingpulse.com/product/icon64/)

Examples of modules that use the CH340G chip are:

- WeMos D1 mini
- D1 mini Lite

Examples of products that use the CH9102 chip are:

- [ThingPulse ePulse Feather](https://thingpulse.com/product/epulse-feather-low-power-esp32-development-board/)
- [ThingPulse ESPGateways](https://thingpulse.com/product-category/gateways/)

Note that there is no harm done if you install both drivers even if you currently just use one! If you are not sure which adapter your ESP8266/ESP32 module uses then just install both.

#### Silicon Labs CP210x

Silicon Labs maintains a [page in English](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) that lists downloadable driver binaries that also contains installation instructions.

#### Winchiphead CH340x / CH341x

Winchiphead (WCH) maintains its website only in Chinese. However, the [download page for the drivers](http://www.wch.cn/download/CH341SER_ZIP.html) is so simple that even non-Chinese speakers will find the right download link.

!!! warning
	Some systems require a reboot before the driver installation can be  successfully completed. The installer may or may not tell you about this! If you later connect the ThingPulse device and the system does not recognize it try rebooting as a first measure..

#### Winchiphead CH9102

Follow the instructions over at [Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102).
