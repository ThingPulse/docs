Um ESP-basierte Module zu programmieren, musst du in der Regel eine Verbindung *über USB* zwischen deinem Entwicklungsrechner (PC, Mac oder Linux) und dem Gerät herstellen. Dafür muss dein System den USB-Seriell-Adapter (auch USB-TTL- oder USB-UART-Adapter genannt) auf dem ESP8266- oder ESP32-Modul erkennen. Zwei häufig verwendete Adapter sind:

- Silicon Labs CP210x
- Winchiphead CH340x / CH341x

Neuere Platinen (ab 2022) verwenden häufig den Winchiphead-CH9102-Chip.

Verbreitete Module mit CP210x sind:

- NodeMCU v1.0 (auch V2 genannt)
- WeMos D1 mini Pro (einige Revisionen)
- [ThingPulse ePulse ESP32-Entwicklungsplatine](https://thingpulse.com/product/epulse-low-power-esp32-development-board/)
- [ThingPulse Icon64](https://thingpulse.com/product/icon64/)

Beispiele für Module mit CH340G-Chip:

- WeMos D1 mini
- D1 mini Lite

Beispiele für Produkte mit CH9102-Chip:

- [ThingPulse ePulse Feather](https://thingpulse.com/product/epulse-feather-low-power-esp32-development-board/)
- [ThingPulse ESPGateways](https://thingpulse.com/product-category/gateways/)

Du kannst die Treiber für CP210x und CH340x/CH341x problemlos beide installieren, auch wenn du gerade nur einen dieser Adapter verwendest. Wenn du nicht sicher bist, welchen dieser Adapter dein ESP8266-/ESP32-Modul nutzt, installiere beide.

#### Silicon Labs CP210x {#silicon-labs-cp210x}

Silicon Labs bietet eine [englischsprachige Seite](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) mit Treiberdownloads und Installationsanleitungen an.

#### Winchiphead CH340x / CH341x {#winchiphead-ch340x-ch341x}

Winchiphead (WCH) betreibt seine Website auf Chinesisch. Die [Downloadseite für die Treiber](http://www.wch.cn/download/CH341SER_ZIP.html) ist jedoch so einfach aufgebaut, dass du den passenden Link auch ohne Chinesischkenntnisse finden kannst.

!!! warning "Warnung"
    Manche Systeme benötigen einen Neustart, um die Treiberinstallation erfolgreich abzuschliessen. Das Installationsprogramm weist nicht immer darauf hin. Falls dein System das angeschlossene ThingPulse-Gerät später nicht erkennt, starte den Computer zunächst neu.

#### Winchiphead CH9102 {#winchiphead-ch9102}

Folge der Anleitung von [Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102).
