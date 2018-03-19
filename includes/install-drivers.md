A prerequisite to program ESP8266-based modules usually is to establish a communications channel from your development platform (PC, Mac, Linux) to the device *over USB*. This in turn requires your system to detect the USB-to-Serial (aka USB-to-TTL, aka USB-to-UART) adapter on the ESP8266 module. There are two commonly used adapters in the wild these days:

- Silicon Labs CP210x
- Winchiphead CH340x / CH341x 

Popular modules that use the former are the NodeMCU v1.0 (i.e. V2) module and some revisions of the WeMos D1 mini Pro. Examples of modules that use the CH340G chip are the WeMos D1 mini and the D1 mini Lite.

Note that there is no harm done if you install both drivers even if you currently just use one! If you are not sure which adapter your ESP8266 module uses then just install both.

#### Silicon Labs CP210x

Silicon Labs maintains a [page in English](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) that list downloadable driver binaries that also contains installation instructions.

#### Winchiphead CH340x / CH341x

Winchihead (WCH) maintains its website only in Chinese. However, the [download page for the drivers](http://www.wch.cn/download/CH341SER_ZIP.html) is so simple that even non-Chinese speakers will find the right download link.