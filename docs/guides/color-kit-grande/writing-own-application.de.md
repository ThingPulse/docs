# Eigene Anwendung schreiben

Verwende den Code unseres Beispielprojekts als Ausgangspunkt oder Referenz für deine eigene Anwendung.
Die Pinbelegung findest du insbesondere in der Konfiguration in `platformio.ini` und `src/settings.h`.

## Touch-Schnittstelle

Die Beispielanwendung nutzt die Touch-Schnittstelle derzeit nicht.
Der Code initialisiert sie jedoch, um die korrekte Verdrahtung sicherzustellen (`display.h#initTouchScreen`).
Ausserdem findest du am Ende von `loop()` einen auskommentierten Codeabschnitt, der zeigt, wie du die Berührungskoordinaten auslesen kannst.

## Hardware-Erweiterungen und Pinbelegung

Wir haben die Anschlussplatine so entwickelt, dass sie sich erweitern lässt.

- An die aufgelötete Buchse kannst du [I2C-Grove-Module](https://wiki.seeedstudio.com/Grove_System/) anschliessen.
Die **Pins für SCL und SDA sind 22 bzw. 23**.
- Viele der herausgeführten Pins stehen für eigene Erweiterungen zur Verfügung.
**Folgende Pins sind frei**.
Details zu diesen Pins findest du im [Espressif-Datenblatt](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf#page=12).
    - Reihe P2: 26, 25, 34, 39, 36, 19, RX, TX, 21
    - Reihe P3: 13, 12, 33, 14
