Eine Toolchain ist eine Sammlung von Werkzeugen, mit denen du Code für eine bestimmte Plattform kompilierst und ausführbare Binärdateien erzeugst. Für den ESP8266 benötigen wir eine andere Toolchain als diejenige, die standardmässig mit der Arduino IDE geliefert wird. Der Board Manager macht die Installation einfach: Mit wenigen Klicks kannst du die Unterstützung für verschiedene Chips und Platinen ergänzen.

- Öffne in der Arduino IDE die Einstellungen und trage http://arduino.esp8266.com/stable/package_esp8266com_index.json in das Feld ==Additional Board Manager URLs== ein.
- Öffne ==Tools== > ==Board: ...== > ==Boards Manager...==, suche nach „ESP8266“ und klicke auf ==Install==. **Hinweis:** ThingPulse empfiehlt, keine Beta- oder RC-Versionen zu installieren.
- Warte, bis die Installation abgeschlossen ist.

![ESP8266 im Board Manager der Arduino IDE](/img/how-tos/Arduino-board-manager-ESP8266.png)

Prüfe von Zeit zu Zeit im Board Manager, ob du die neueste Version der ESP8266-Toolchain installiert hast, die __weder Beta noch RC__ ist. Klicke dazu auf den ESP8266-Eintrag, wähle die neueste Version aus der Auswahlliste und klicke auf ==Update==.
