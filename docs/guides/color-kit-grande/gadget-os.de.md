# Gadget OS einrichten

Installiere Gadget OS direkt im Browser und richte deinen Color Kit Grande auf dem Touchscreen ein. **Du brauchst weder Programmierkenntnisse noch eine Entwicklungsumgebung.** Dies ist der empfohlene Einstieg, wenn du deinen Bausatz ohne Codeänderungen nutzen möchtest.

Gadget OS enthält eine Wetter-App und weitere Touchscreen-Werkzeuge. Für den Wetterdienst ist kein persönlicher API-Schlüssel erforderlich.

Die Screenshots unten stammen aus dem [Gadget-OS-Benutzerhandbuch](https://github.com/ThingPulse/esp32-gadget-os/blob/master/USER_GUIDE.md) und zeigen Beispieldaten. Deine Standorte, Messwerte und der Verbindungsstatus können abweichen. Klicke auf ein Bild, um es zu vergrössern.

## Bevor du beginnst

- Schliesse die [Montageanleitung](assembly.md) einschliesslich des Display- und Touchtests ab, bevor du Gadget OS installierst.
- Halte ein USB-Datenkabel und einen Computer mit **Google Chrome oder Microsoft Edge** bereit.
- Verbinde deinen Computer mit dem Internet und halte den Namen und das Passwort deines WLANs bereit.

## Im Browser installieren

1. Verbinde den Color Kit Grande über das USB-Datenkabel mit deinem Computer und schalte ihn am Netzschalter ein.
2. Öffne den [ThingPulse App Market](https://app-market.thingpulse.com/) in Chrome oder Edge.
3. Wähle **Color Kit Grande** und danach **Gadget OS**.
4. Klicke auf **Connect & Install** und wähle das serielle Gerät deines Bausatzes aus.
5. Folge den Anweisungen des Installationsprogramms. Lass das Kit angeschlossen, bis das Programm die erfolgreiche Übertragung meldet.
6. Warte, bis Gadget OS startet. Du solltest den Touchscreen-Startbildschirm mit App-Symbolen sehen.

![Gadget-OS-Startbildschirm mit Weather, Calculator und Settings](../../img/guides/color-kit-grande/gadget-os/home.png){ width="240" }

Die Installation von Gadget OS ersetzt die bisherige Anwendung auf dem Kit, einschliesslich des Montage-Testprogramms.

!!! tip "Die Browserinstallation ist abgeschlossen"

    Fahre unten mit der Einrichtung auf dem Touchscreen fort. Die Seiten **Entwicklungsumgebung** und **Wetterstationsprojekt** beschreiben den alternativen Programmierweg. Die dortigen separaten Übertragungen von Dateisystem und Firmware sind keine zusätzlichen Schritte für Gadget OS.

## Auf dem Touchscreen einrichten

Öffne **Settings** auf dem Gadget-OS-Startbildschirm. Mit dem Pfeil oben links kehrst du zur vorherigen Ansicht zurück.

![Einstellungsmenü von Gadget OS](../../img/guides/color-kit-grande/gadget-os/settings.png){ width="240" }

### 1. Mit dem WLAN verbinden

1. Öffne **Settings > Wi-Fi** und tippe auf **Scan networks**.
2. Wähle dein Netzwerk und gib das Passwort über die Bildschirmtastatur ein.
3. Tippe auf **Save & Back** und warte einige Sekunden auf die Verbindung.

Bei bestehender Verbindung leuchtet das WLAN-Symbol dauerhaft weiss. Bei einem versteckten Netzwerk gibst du den Namen unter **SSID** manuell ein.

![WLAN-Einrichtung mit Netzwerkname, Scan networks, Passwort und Save & Back](../../img/guides/color-kit-grande/gadget-os/wifi.png){ width="240" }

### 2. Zeitzone einstellen

1. Öffne **Settings > Time**.
2. Wähle deine Region und Zeitzone sowie das gewünschte Uhrzeitformat.
3. Speichere die Einstellungen und kehre zurück.

Nach dem Verbinden mit dem WLAN stellt sich die Uhr über das Internet ein.

![Zeiteinstellungen mit Region, Zeitzone und 24-Stunden-Format](../../img/guides/color-kit-grande/gadget-os/time.png){ width="240" }

### 3. Wetterstandort wählen

1. Öffne **Settings > Weather**.
2. Gib unter **Add a location** einen Ort oder eine Postleitzahl ein und tippe auf **Search**.
3. Wähle das passende Ergebnis und tippe danach auf den gespeicherten Standort, um ihn zu aktivieren. Ein Häkchen kennzeichnet den aktiven Standort.

Standorte werden automatisch gespeichert. Mit dem Schalter für metrische Einheiten wählst du deine bevorzugten Masseinheiten.

![Wettereinstellungen mit gespeicherten Standorten, Ortssuche und metrischen Einheiten](../../img/guides/color-kit-grande/gadget-os/weather-locations.png){ width="240" }

## Ergebnis prüfen

Kehre zum Startbildschirm zurück und öffne **Weather**. Prüfe, ob der richtige Standort, Wetterwerte und Symbole erscheinen und ob die Uhr deine Ortszeit zeigt. Deine Einstellungen bleiben beim nächsten Neustart gespeichert.

![Beispiel der Wetter-App mit Standort, Wetterwerten und Vorhersagesymbolen](../../img/guides/color-kit-grande/gadget-os/weather.png){ width="240" }

**Dein Kit ist einsatzbereit.** Du kannst Gadget OS weiterverwenden und musst die Programmierseiten nicht anschliessend durcharbeiten.

## Wenn etwas nicht funktioniert

| Problem | Mögliche Lösung |
|---------|-----------------|
| Der Browser bietet dein Kit nicht als serielles Gerät an | Verwende Chrome oder Edge und ein USB-Datenkabel. Folge der [USB-Fehlerbehebung](troubleshooting.md#usb-not-detected), einschliesslich der Treiberprüfung. |
| Die Installation schlägt fehl | Notiere die Fehlermeldung und folge den [Hardware- und Verbindungsprüfungen](troubleshooting.md#hardwareprobleme). Erwähne beim Support, dass du Gadget OS über den App Market installierst. |
| Der Bildschirm bleibt dunkel oder Touch reagiert nicht | Folge den Prüfungen für [Display](troubleshooting.md#dark-display) oder [Touch](troubleshooting.md#touch-not-working). |
| Das WLAN verbindet sich nicht | Öffne **Settings > Wi-Fi** erneut und prüfe Netzwerkname und Passwort. |
| Die Uhr ist nicht eingestellt oder zeigt die falsche Zeit | Prüfe die WLAN-Verbindung und **Settings > Time** und warte auf die Synchronisierung. |
| Wetterdaten werden nicht geladen | Prüfe das WLAN und den aktiven Standort unter **Settings > Weather**. Ziehe die Wetteransicht nach unten, um es erneut zu versuchen. |

Bleibt das Problem bestehen, [kontaktiere den Support](troubleshooting.md#support-kontaktieren) mit deiner Gadget-OS-Version aus **Settings > System**, dem Symptom und einer Fehlermeldung oder einem Foto.

## Gadget OS aktualisieren

Öffne bei bestehender WLAN-Verbindung **Settings > Software Update**, um nach Updates zu suchen, und folge den Anweisungen auf dem Bildschirm. Updates lassen sich über WLAN installieren, ohne VS Code oder das Browser-Installationsprogramm erneut zu verwenden.

## Mehr erfahren

- [Gadget-OS-Einführung und Einrichtungsvideo](https://thingpulse.com/blog/gadget-os-color-kit-grande/)
- [Gadget-OS-Benutzerhandbuch](https://github.com/ThingPulse/esp32-gadget-os/blob/master/USER_GUIDE.md)
- Möchtest du stattdessen das separate Wetterstationsbeispiel anpassen? Beginne mit der [Entwicklungsumgebung](development-environment.md) und folge danach dem [Wetterstationsprojekt](weather-station.md). Die Installation dieses Projekts ersetzt Gadget OS.
