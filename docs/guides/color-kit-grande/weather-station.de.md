# Wetterstationsprojekt

Nachdem alle Lötarbeiten abgeschlossen sind, widmen wir uns dem Projekt Weather Station Touch.

## Quellcode herunterladen

Wie alle Open-Source-Projekte von ThingPulse ist auch das Wetterstationsbeispiel öffentlich auf GitHub verfügbar.
Du hast zwei Möglichkeiten, den Quellcode herunterzuladen:

- Klone das Repository mit Git: `git clone https://github.com/ThingPulse/esp32-weather-station-touch`
- Lade den Quellcode von https://github.com/ThingPulse/esp32-weather-station-touch/archive/master.zip herunter und entpacke ihn in einen Ordner auf deinem Computer.

## Projekt in Visual Studio Code öffnen

- Starte VS Code.
- Wähle ==File== > ==Open Folder...==.
- Suche den Ordner `esp32-weather-station-touch` aus dem vorherigen Schritt und wähle ihn aus.

## Konfiguration und Anpassung

Öffne die Datei `src/settings.h` und passe die rund zehn Konfigurationsparameter im Abschnitt „User settings“ am Anfang der Datei an.
Alle Parameter sind direkt in der Datei dokumentiert.
Die Erläuterungen sollten dir bei der Konfiguration helfen.
Besonders wichtig ist der OpenWeatherMap-API-Schlüssel, den du eintragen musst ([Anleitung zum Erstellen eines Schlüssels](../../how-tos/openweathermap-key.md)).

## Dateisystem auf das Gerät übertragen {#upload-the-file-system-to-device}

- Klicke auf das PlatformIO-Symbol in der linken Seitenleiste (Alien-Gesicht).
- Wähle die Aufgabe ==Platform== > ==Upload Filesystem Image==.

Nach erfolgreicher Übertragung musst du diesen Schritt nur einmal ausführen.
Beachte die Ausgabe in der sich öffnenden VS-Code-Konsole.
Falls dort Fehler gemeldet werden, beispielsweise weil keine Verbindung zur Platine möglich ist oder die Übertragung abbricht, wiederhole den Vorgang.

![Dateisystem mit PlatformIO übertragen](../../img/how-tos/platformio-filesystem.png)

## Programm auf das Gerät übertragen

- Wähle die Aufgabe ==General== > ==Upload and Monitor==.

Diesen Schritt führst du **jedes Mal aus, wenn du den Code oder die Konfiguration änderst**.

![Programm mit PlatformIO übertragen und serielle Ausgabe anzeigen](../../img/how-tos/platformio-task-upload.png)

Alternativ kannst du die Schaltflächen in der unteren Statusleiste verwenden:

![PlatformIO-Schaltflächen in der Statusleiste](../../img/how-tos/platformio-upload.png)

!!! note "Hinweis"

    Falls die Übertragung fehlschlägt, stelle sicher, dass die erforderlichen Treiber für den CH9102-USB-Seriell-Wandler installiert sind.
    Ausführliche Informationen und eine Anleitung findest du bei [Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102).
