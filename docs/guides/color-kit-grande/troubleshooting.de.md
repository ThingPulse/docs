# Fehlerbehebung

## Hardwareprobleme

| Symptom | Lösungsvorschlag | Bild |
|---------|-----------------|------|
| Nach dem Übertragen von Dateisystem und Firmware flackert das Display, bleibt aber dunkel | Dieses Problem lässt sich häufig durch Nachlöten kalter Lötstellen beheben. Mit einem Multimeter kannst du die Verbindungen zwischen der ePulse-Feather-Platine und der grösseren Anschlussplatine Pin für Pin prüfen. Über den Masseanschluss (GND) ist eine zusätzliche Prüfung möglich: Prüfe, ob das Metallgehäuse des USB-C-Steckers elektrisch mit dem GND-Pin auf der grossen Platine verbunden ist. Besteht keine Verbindung, erhitze die Lötstelle erneut, damit der Pin richtig mit dem Lötpad verbunden wird. | [![](../../img/guides/color-kit-grande/trouble1.jpg)](../../img/guides/color-kit-grande/trouble1.jpg) |
| Das Display zeigt Text, aber keine Symbole | Wahrscheinlich wurde das Dateisystem nicht erfolgreich übertragen, aus dem die Symbole geladen werden. Stelle sicher, dass du den Schritt [Dateisystem auf das Gerät übertragen](weather-station.md#upload-the-file-system-to-device) ausgeführt hast. | [![](../../img/guides/color-kit-grande/trouble2_ckg_no_icons.jpeg)](../../img/guides/color-kit-grande/trouble2_ckg_no_icons.jpeg) |
| Das Display bleibt weiss | Die wahrscheinlichste Ursache ist eine schlechte Lötstelle. Prüfe diese Pins auf kalte Lötstellen:<br><ul><li>TFT_DC (IO02)</li><li>TFT_RESET (IO04)</li><li>TFT_SCK (IO05)</li><li>TFT_MOSI (IO18)</li><li>TFT_MISO (IO19)</li><li>TFT_CS (IO15)</li></ul>Prüfe auch die folgenden Anschlüsse, die ebenfalls beteiligt sein können:<ul><li>TFT_LED (IO32)</li><li>3V3</li><li>GND</li></ul> | [![](../../img/guides/color-kit-grande/trouble3_ckg_white_screen.png)](../../img/guides/color-kit-grande/trouble3_ckg_white_screen.png) |
| Die Platine ist eingeschaltet (LEDs leuchten), erscheint am Computer aber nicht als USB-Gerät | Wenn die Platine mit Strom versorgt wird, die USB-Schnittstelle jedoch nicht erkannt wird (kein COM-Port, kein neues Gerät im Geräte-Manager), gehe wie folgt vor:<br><ul><li>**Trenne den ePulse Feather von der Anschlussplatine** und versuche, ihn einzeln zu flashen. Ein Kurzschluss auf der Anschlussplatine könnte die USB-Kommunikation beeinträchtigen.</li><li>**Prüfe die TX- und RX-Pins** auf Lötbrücken, die die serielle Kommunikation beeinträchtigen könnten.</li><li>**Kontrolliere alle Lötstellen** auf Ober- und Unterseite beider Platinen. Das Nachlöten problematischer Stellen behebt den Fehler häufig.</li><li>Verwende ein **USB-Datenkabel**, kein reines Ladekabel.</li><li>Stelle sicher, dass der CH9102F-USB-Seriell-Treiber installiert ist. Folge bei Bedarf der [CH9102F-Treiberanleitung von Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102).</li></ul> | |
| Die TestBed-Installation bleibt bei 0 % stehen und die serielle Konsole zeigt wiederholt Punkte, Striche oder Verbindungsfehler | Das Installationsprogramm erkennt den USB-Seriell-Adapter, kann aber keine Verbindung zum ePulse Feather herstellen. Führe die folgenden Schritte der Reihe nach aus:<br><ol><li>**Probiere ein anderes USB-Kabel und einen anderen USB-Anschluss aus.** Manche USB-Kabel liefern nur Strom und übertragen keine Daten. Beschädigte oder unzuverlässige Kabel können beim Flashen ausfallen. Prüfe das Ersatzkabel nach Möglichkeit durch eine Datenübertragung zu einem anderen Gerät, beispielsweise einem Smartphone.</li><li>**Prüfe den CH9102F-Treiber.** Installiere den passenden Treiber gemäss der [CH9102F-Treiberanleitung von Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102) neu bzw. erneut und schliesse die Platine wieder an. Tritt derselbe Fehler auf einem anderen Computer mit funktionierendem Treiber auf, ist der Treiber als Ursache weniger wahrscheinlich.</li><li>**Nimm den ePulse Feather von der Anschlussplatine ab und versuche, ihn einzeln zu flashen.** Gelingt das Flashen jetzt, stört eine Lötbrücke oder ein Kurzschluss auf der Anschlussplatine die Kommunikation.</li><li>**Kontrolliere die Lötstellen.** Prüfe beide Platinen sorgfältig auf Lötbrücken, besonders an den seriellen und benachbarten Pins, und bessere verdächtige Stellen nach. Ein Kurzschluss kann auch auf dem ePulse Feather selbst vorliegen. Ein Fehlschlag beim separaten Flashen schliesst einen Lötfehler daher nicht vollständig aus.</li><li>Lässt sich die Platine auch einzeln mit einem nachweislich funktionierenden Datenkabel und Treiber nicht flashen, ist der **ePulse Feather möglicherweise beschädigt**. Wende dich an den Support und füge scharfe, gut erkennbare Fotos aller Lötstellen auf beiden Platinen bei.</li></ol> | [![TestBed-Installation bleibt bei 0 %, während die serielle Konsole wiederholte Verbindungsversuche anzeigt](../../img/guides/color-kit-grande/trouble4_testbed-serial-connection.png)](../../img/guides/color-kit-grande/trouble4_testbed-serial-connection.png) |

## Softwareprobleme

| Symptom | Lösungsvorschlag | Bild |
|---------|-----------------|------|
| Im PlatformIO-Protokoll erscheint `Please install git client from https://git-scm.com/download` | Das Wetterstationsprojekt verwendet eine Bibliothek aus einem Git-Repository. PlatformIO benötigt deshalb einen funktionsfähigen Git-Client, auch wenn du das Projekt selbst als ZIP-Datei heruntergeladen hast. Installiere Git von [git-scm.com/install](https://git-scm.com/install/) und starte Visual Studio Code vollständig neu. Öffne ein Terminal und führe `git --version` aus, um zu prüfen, ob Git installiert und über den System-`PATH` erreichbar ist. Starte danach den Build erneut. | [![PlatformIO-Protokoll mit Aufforderung zur Installation des Git-Clients](../../img/guides/color-kit-grande/trouble5_platformio-git-client.png)](../../img/guides/color-kit-grande/trouble5_platformio-git-client.png) |

## Selbsttest

Unser [Online-Selbsttest-Assistent](https://ckg-self-test.thingpulse.com/) hilft dir, Probleme mit deinem Color Kit Grande zu diagnostizieren.

[![Selbsttest-Assistent](../../img/guides/color-kit-grande/self-test-wizard.png)](https://ckg-self-test.thingpulse.com/)

### Selbsttest durchführen

1. **Entferne beide FPC-Flachbandkabel** von der Anschlussplatine (Display und Touch).
2. Verbinde die beiden gekennzeichneten Testpads auf der Anschlussplatine mit einem **Überbrückungskabel**.
3. Folge den Anweisungen im [Selbsttest-Assistenten](https://ckg-self-test.thingpulse.com/).

### Qualitätssicherung

Vor dem Versand werden alle Platinen mit einer Selbsttest-Firmware programmiert und die Displays in einer Testvorrichtung geprüft. Zum Zeitpunkt des Versands wurde somit die korrekte Funktion aller Komponenten bestätigt.

**Die meisten Probleme entstehen durch schlechte Lötstellen** beim Zusammenbau. In der Regel kannst du sie so beheben:

- Problematische Lötstellen mit dem Lötkolben **erneut erhitzen**.
- Überschüssiges Lötzinn mit **Entlötlitze** entfernen.
- Lötbrücken oder Kurzschlüsse mit einer **Entlötpumpe** beseitigen.

Prüfe im Zweifelsfall sorgfältig alle Lötstellen auf Ober- und Unterseite beider Platinen. Löte Stellen nach, die matt oder klumpig aussehen oder keine saubere Kegelform haben.

!!! tip "Tipp"

    Ist ein Teil irreparabel beschädigt, sieh auf der Seite [Ersatzteile](replacement-parts.md) nach, bevor du einen vollständigen neuen Bausatz kaufst.

## Support kontaktieren

Falls keine der oben genannten Massnahmen dein Problem behebt, kontaktiere uns unter **info AT thingpulse.com**.

Damit wir das Problem schnell eingrenzen können, gib in deiner E-Mail bitte folgende Informationen an:

```text
Betreff: Color Kit Grande – Hilfe bei der Fehlerbehebung

Hallo ThingPulse-Support,

ich habe Probleme mit meinem Color Kit Grande und benötige Unterstützung.

**Symptom:**
[Beschreibe, was passiert, z. B. Display bleibt dunkel, weisser Bildschirm, keine USB-Verbindung usw.]

**Was ich bereits versucht habe:**
- [ ] Lötstellen geprüft und nachgelötet
- [ ] TX/RX-Pins auf Lötbrücken geprüft
- [ ] Verschiedene USB-Kabel getestet
- [ ] ePulse Feather von der Anschlussplatine getrennt
- [ ] Selbsttest-Assistenten ausgeführt
- [ ] Sonstiges: ___

**Angehängte Fotos:**
Im Anhang befinden sich scharfe Fotos von:
- Oberseite der Anschlussplatine (alle Lötstellen sichtbar)
- Unterseite der Anschlussplatine
- Oberseite der ePulse-Feather-Platine
- Unterseite der ePulse-Feather-Platine

Vielen Dank für eure Hilfe!
```

!!! tip "Tipps für Fotos"
    Gute Beleuchtung und scharf abgebildete Lötstellen helfen uns, Fehler schnell zu erkennen. Auf Fotos können wir problematische Pins oft erkennen, die bei direkter Betrachtung leicht übersehen werden.
