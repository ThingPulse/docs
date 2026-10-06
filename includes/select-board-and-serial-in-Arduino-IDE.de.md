Es reicht nicht, dass die Arduino IDE ESP8266-Module grundsätzlich unterstützt: Die Module unterscheiden sich in wichtigen Details, etwa beim verfügbaren Flash-Speicher und der Art der Programmierung. Mit der Auswahl der richtigen Platine legst du auch die Namen der GPIO-Pins fest. Die Entwickler des NodeMCU-Moduls haben beispielsweise ein eigenes Namensschema eingeführt. Statt `GPIO1`, `GPIO2` usw. tragen die Pins Namen mit dem Präfix „D“: `D0` entspricht GPIO16, `D1` entspricht GPIO5 usw. Wenn du die passende Platine in der Arduino IDE auswählst, stehen dir automatisch das richtige Namensschema und weitere relevante Einstellungen zur Verfügung. Bei NodeMCU-Modulen ist das besonders hilfreich, weil diese Namen auch auf der Platine aufgedruckt sind.

Nicht alle ThingPulse-Bausätze enthalten dieselben ESP8266-Chips bzw. -Module. Wir haben für jeden Bausatz die passende Variante ausgewählt. Damit du die Arduino IDE richtig konfigurieren kannst, musst du wissen, welches Modul in deinem Bausatz enthalten ist:

- [Starter Kit](https://thingpulse.com/product/esp8266-iot-electronics-starter-kit-weatherstation-planespotter-worldclock/) --> NodeMCU 1.0, auch v2 genannt
- [Color Display Kit](https://thingpulse.com/product/esp8266-wifi-color-display-kit-2-4/) --> LOLIN(WEMOS) D1 R2 & mini
- [ESPaper Kits](https://thingpulse.com/product-category/espaper-epaper-kits/) --> Generic ESP8266

Wähle in der Arduino IDE:

==Tools== > ==Board: *== > den passenden Eintrag aus der Liste oben.

In einem früheren Schritt hast du die Treiber für den USB-Seriell-Wandler installiert. Wenn alles funktioniert hat und das Gerät mit deinem Computer verbunden ist, kannst du jetzt die serielle Verbindung auswählen. Du findest sie unter ==Tools== > ==Port==. Unter macOS heissen die seriellen Geräte `/dev/cu.xxx`. Unter Windows sollte dein Gerät als COM-Port mit der Bezeichnung `COM#` erscheinen, wobei # für eine Zahl steht.

Falls dein Gerät nicht in der Anschlussliste erscheint, ziehe es ab und stecke es nach einigen Sekunden wieder ein. Probiere auch einen anderen USB-Anschluss aus. Hilft das nicht, starte deinen Computer neu und/oder teste ein anderes USB-Kabel.

!!! warning "Warnung"

    Je nachdem, womit du zuvor in der Arduino IDE gearbeitet hast, musst du die UART-Baudrate anpassen. Unter ==Tools== > ==Upload Speed== sollte mindestens 115200 eingestellt sein. Je nach Betriebssystem und Treiber sind bis zu 921600 möglich. Probiere aus, welche Einstellung zuverlässig funktioniert; eine höhere Geschwindigkeit ist vorteilhaft.
