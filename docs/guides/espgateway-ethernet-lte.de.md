# ESPGateway Ethernet LTE {#espgateway-ethernet-lte}

![ESPGateway Ethernet LTE](../img/guides/espgateway-ethernet-lte/espgateway-ethernet-lte.png)

!!! warning "Vorläufige Anleitung — Entwurf zur technischen Prüfung"
    Version 0.9, 12. Oktober 2026. Technische Daten, Bedienung und regulatorische Angaben müssen für die Serienhardware und -firmware bestätigt werden. **OFFEN** kennzeichnet Informationen, die vor der Auslieferung mit einem verkauften Produkt ergänzt werden müssen. Dieser Entwurf bestätigt weder eine FCC-Zulassung noch die EU-Konformität.

## Produktidentifikation {#product-identification}

Diese Anleitung gilt für das ThingPulse ESPGateway Ethernet LTE. Vergleiche vor der Installation das Modell und die Hardwareversion auf deinem Gerät mit dieser Anleitung.

| Angabe | Informationen zum Serienprodukt |
| --- | --- |
| Produktname | ESPGateway Ethernet LTE |
| Produktbezeichnung auf der Verpackung | ESPGateway Ethernet LTE |
| GTIN-13 / EAN auf der Verpackung | `7649998893091` — Produktkennung, keine individuelle Geräteseriennummer |
| SKU | `7649998893091` — die GTIN wird als SKU verwendet; es gibt keine separate SKU |
| Hardwareherkunft laut Verpackung | China (`Hardware Made in China`) |
| Platinenbeschriftung | `THINGPULSE` — `ESP32 Ethernet Gateway with SIM760x and A7670x support` |
| Datumsaufdruck der Platine | `2026/08/30` — Bedeutung als Hardwareversions-/Datumskennung noch zu bestätigen |
| Hardware und mitgelieferte Firmware | Ausschliesslich Selbsttest-Firmware; **OFFEN** — Serienhardwareversion und Version der Selbsttest-Firmware |
| Hersteller (juristische Person und vollständige Postadresse) | ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland |
| EU-Importeur / verantwortlicher Wirtschaftsakteur, falls erforderlich | **OFFEN** — Name und postalische Kontaktdaten |
| US-Verantwortlicher, falls erforderlich | **OFFEN** — US-Unternehmen, Adresse, Telefon oder Internetkontakt |
| Produktsupport | [ThingPulse-Support](../support.md) |
| Anleitung | <https://docs.thingpulse.com/guides/espgateway-ethernet-lte/> |

## Bestimmungsgemässe Verwendung und Lieferumfang {#intended-use}

Das ESPGateway Ethernet LTE ist ein programmierbares Gateway zur Kommunikation mit WLAN- oder Bluetooth-Low-Energy-(BLE)-Geräten über das ESP32-Modul und zur Übertragung ihrer Daten über LTE an ein Backend. Es richtet sich an Nutzer, die eigene Anwendungsfirmware entwickeln und installieren können.

**Das Gerät wird ausschliesslich mit Selbsttest-Firmware ausgeliefert. Für deine Anwendung musst du eigene Firmware schreiben und installieren.** Die mitgelieferte Firmware ist kein betriebsfertiges Sensor-Gateway und keine MQTT-Anwendung.

Deine Anwendung könnte beispielsweise Temperatur und Luftfeuchtigkeit eines BLE-Sensors auslesen und die Messwerte über LTE an einen MQTT-Broker senden. Dies ist ein Beispiel für die vorgesehene Nutzung, keine Funktion der ausgelieferten Selbsttest-Firmware.

**OFFEN:** vorgesehene Installationsumgebung, dokumentierte Nutzungsgrenzen, genauer Selbsttestumfang und dabei verwendete Funkmodi. Eine Eignung für Notfallkommunikation oder sicherheitskritische Anwendungen wurde nicht festgestellt.

Das Gerät wird mit Gehäuse, einer externen 2,4-GHz-WLAN-Antenne und einer internen LTE-Folienantenne geliefert. Die Stromversorgung erfolgt über einen USB-C-Anschluss. Die Verpackung nennt ein ESPGateway Ethernet und ein A7670G-(Global)-LTE-Modul. Diese Inhaltsangabe sagt nicht aus, ob die LTE-Baugruppe vorinstalliert ist; Einbauzustand und Schritte zur Inbetriebnahme müssen noch bestätigt werden.

**OFFEN — weitere Angaben zur Packliste:** Antennenteilenummern, Kabel, USB-Netzteil (mitgeliefert oder separat erforderlich), SIM-Anforderungen und gedruckte Sicherheits-/Kurzanleitung. Das Zubehör muss der bewerteten Konfiguration entsprechen.

## Technische Daten {#technical-specifications}

Die Bauteilbezeichnungen stammen aus Schaltplanrevision 1.0.3 vom 2026-08-30, ausser der LTE-Baugruppe: Diese folgt der von ThingPulse bestätigten Lieferantenauswahl. Die Platinenbeschriftung nennt die Unterstützung zweier Modemfamilien; sie identifiziert nicht das bestückte Modem. Die LTE-Bezeichnung im Schaltplan muss mit der ausgewählten Baugruppe in der Serien-BOM abgeglichen werden; die Modulbeschriftung muss zum Prüfmuster passen.

| Parameter | Bekannte Angaben und offene Bestätigungen |
| --- | --- |
| Stromversorgung | USB-C; **OFFEN** — endgültige Eingangsnennspannung/-bereich und Nennstrom. Der Anschluss allein legt die Leistungsdaten nicht fest. |
| Externes Netzteil und Kabel | **OFFEN** — erforderliche Ausgangswerte, Sicherheitsmerkmale und zulässige Kabelgrenzen |
| Ethernet | RJ45 (J1, HR911105A), LAN8720A-CP-TR-Controller (U1). Keine PoE-Eingangsschaltung dargestellt; **OFFEN** — Bestätigung für das Seriengerät und unterstützte Übertragungsraten. |
| LTE-Baugruppe | [AND-Global BK-A7670G](https://www.and-global.com/list_23/662.html), laut Angebot mit SIMCom A7670G-LLSE (LTE Cat 1). **OFFEN** — Platinenrevision, Beschriftung des bestückten Moduls und Zulassungsunterlagen. |
| WLAN-/Bluetooth-Modul | ESP32-WROVER-IE-N16R8 (U3); **OFFEN** — Bestätigung des Serienbauteils und aktivierte Firmwaremodi. |
| USB-UART-Brücke | CH9102F (U5), mit den USB-C-Datenleitungen verbunden |
| Anzeigen und Bedienelemente | Vier WS2812E-V5-LEDs (LED1–LED4); Farben, Muster und Bedeutungen der LEDs werden vom Firmwareentwickler festgelegt. Netzschalter SW1 und ein Taster an GPIO4; **OFFEN** — Tasterfunktion der ausgelieferten Selbsttest-Firmware. |
| SIM | **OFFEN** — Typ, Ausrichtung, Einsetzen/Entnehmen und Mobilfunkanbieter-Anforderungen |
| Betriebs-/Lagerbedingungen | **OFFEN** — Temperatur, Feuchtigkeit, Höhe, Innen-/Ausseneinsatz und Schutzart |
| Abmessungen und Montage | **OFFEN** — Gehäuseabmessungen, Ausrichtung und Abstände |
| Erweiterungsschnittstellen | Zwei 10-polige Stiftleisten mit 2,54 mm Raster (X1/X3) dargestellt; **OFFEN** — Zugänglichkeit im Gehäuse, elektrische Grenzen und unterstütztes Zubehör. |

### Frequenzbänder und Antennen {#radio-bands}

Der Lieferant bezeichnet den Modemtyp als A7670G-LLSE. Die folgenden **Modulfähigkeiten** stammen aus dem [SIMCom-Datenblatt A7670G-LLSE, Version 2021.11](https://datasheet.lcsc.com/datasheet/pdf/a6ff746802142b3caed58b61817fe57c.pdf?productCode=C21264512); sie erklären nicht die zugelassenen Betriebsbänder des Gateways.

| Mobilfunkmodus | Vom Modul unterstützte Bänder / nominelle Bandbezeichnungen |
| --- | --- |
| LTE-FDD | B1, B2, B3, B4, B5, B7, B8, B20, B28, B66 |
| LTE-TDD | B34, B38, B39, B40, B41 |
| GSM / GPRS / EDGE | 850, 900, 1800, 1900 MHz |

LTE Cat 1 unterstützt auf Modulebene bis zu **10 Mbit/s im Downlink / 5 Mbit/s im Uplink**. Der tatsächliche Gateway-Durchsatz hängt von Hostschnittstelle, Firmware, Netz und Empfangsbedingungen ab. Bestätige die LLSE-Beschriftung des Serienmoduls, bevor du diese Bandliste auf eine andere A7670G-Revision überträgst. «Global» garantiert weder Netzverfügbarkeit noch Zulassung in jedem Land.

Das Gateway verwendet eine interne Mobilfunk-Folienantenne und eine externe 2,4-GHz-WLAN-Antenne. Antennenteilenummern, Gewinn je Band, Anschlüsse und Installationsbedingungen bleiben **OFFEN**.

| Angaben für die Freigabe | Status |
| --- | --- |
| Aktivierte Mobilfunkbänder und -modi | **OFFEN** — Serienfirmware-/Netzkonfiguration mit obiger Modulliste abgleichen; GSM/GPRS/EDGE bei Aktivierung in die Bewertung aufnehmen |
| Frequenzbereiche und maximale HF-Ausgangsleistung | **OFFEN** — Sende-/Empfangsbereiche und maximale Leistung je aktiviertem Band/Modus anhand der passenden Modulunterlagen und abschliessenden Bewertung ergänzen; leitungsgebundene Leistung oder EIRP sowie relevante Toleranzen angeben |
| WLAN und Bluetooth | **OFFEN** — aktivierte Modi, Frequenzen und maximale Leistungen des ESP32-Funks |
| Regionale Beschränkungen und gleichzeitiger Sendebetrieb | **OFFEN** — zulässige Länder, Funkkombinationen und Installationsbeschränkungen bestimmen |
| HF-Exposition und Abstand zwischen Antennen und Personen | **OFFEN** — abschliessende Bewertung und Zulassungsbedingungen verwenden; kein pauschaler Mindestabstand angegeben |

Das LLSE-Datenblatt nennt keine HF-Ausgangsleistung. Es wurde kein Wert einer anderen A7670G-Hardwarerevision übernommen. Auch Versorgungsspannungs- und Temperaturgrenzen des Moduls sind keine Nenndaten des fertigen Gateways; USB-C-Eingangsnenndaten und Betriebsgrenzen im Gehäuse müssen noch bestätigt werden.

## Sicherheit und Installation {#safety}

Die folgenden Sicherheitshinweise sind ein Vorschlag zur Prüfung anhand der abschliessenden Produktrisikobeurteilung.

- Lies die vollständige Anleitung, bevor du die Stromversorgung anschliesst. Verwende nur die vorgegebene Stromversorgung, Kabel und freigegebenen Antennen.
- Trenne die Stromversorgung, bevor du SIM, Antenne oder Erweiterungen einsetzt, anschliesst oder entfernst, sofern die endgültige Anleitung dies nicht ausdrücklich im eingeschalteten Zustand erlaubt.
- Halte das Gerät trocken und fern von übermässiger Hitze. Betreibe es nur innerhalb der festgelegten Umgebungsbedingungen. Halte Lüftungsöffnungen frei.
- Verwende keine beschädigten Geräte, Kabel oder Netzteile. Trenne bei Rauch, ungewöhnlichem Geruch oder sichtbaren Schäden die Stromversorgung und kontaktiere den Support.
- Beachte Funkbeschränkungen in Krankenhäusern, Flugzeugen und explosionsgefährdeten Umgebungen.
- Beachte die freigegebene Antennenposition und die vorgeschriebenen Abstände. Ersetze Antennen nicht durch andere Typen und ändere Funkeinstellungen nicht über die dokumentierten Grenzen hinaus.
- Trenne das Gerät vor der Reinigung vom Strom und verwende ein trockenes Tuch. Halte Kleinteile von Kindern fern.

**Vor Freigabe OFFEN:** Produktspezifische elektrische, thermische, mechanische, ESD- und HF-Sicherheitshinweise ergänzen; zugängliche Anschlüsse, Montage, Trennung der Stromversorgung und Öffnen des Gehäuses durch Nutzer klären. Batteriehinweise nur ergänzen, wenn eine Batterie vorhanden ist oder unterstützt wird.

## Erste Inbetriebnahme {#setup}

**Vorläufiger Ablauf — vor Verwendung am Serienmuster prüfen.**

1. Prüfe Modell, Lieferumfang und erforderliche Stromversorgung.
2. Setze bei getrennter Stromversorgung die erforderliche SIM ein und verbinde die mitgelieferte externe WLAN-Antenne mit dem zugehörigen Anschluss. Die LTE-Folienantenne befindet sich im Inneren; ihr Anschluss gehört nicht zum externen Antennenanschluss. **OFFEN:** Anschlussbild, SIM-Zugang/-Ausrichtung und Bestätigung der werkseitigen LTE-Antennenplatzierung.
3. Verbinde Ethernet, falls der dokumentierte Selbsttest oder deine Anwendung dies erfordert. **OFFEN:** Kabelanforderungen und PoE-Beschränkungen.
4. Stelle Gerät und Antennen unter Einhaltung der oben angegebenen Montage- und HF-Abstände auf.
5. Schliesse das vorgegebene Netzteil an USB-C an und befolge die Selbsttest-Anleitung. **OFFEN:** Testablauf, Startdauer und selbsttestspezifische Erfolgs-/Fehleranzeigen.
6. Entwickle ESP32-Anwendungsfirmware, die mit deinen WLAN-/BLE-Geräten kommuniziert und Daten über die LTE-Baugruppe überträgt. **OFFEN:** dokumentierte Entwicklungsumgebung, Boardkonfiguration, Pinzuordnung und Programmierverfahren.
7. Installiere deine Anwendungsfirmware gemäss dokumentiertem Programmierverfahren. **OFFEN:** genaue Befehle/Werkzeuge, Flash-Einstellungen und Wiederherstellungsdatei der Selbsttest-Firmware.
8. Konfiguriere Mobilfunkanbieter/APN, Backend-Endpunkt und Authentifizierung in deiner Anwendung. Lege bei MQTT Broker, Topics und Zugangsdaten fest und prüfe den Empfang der Sensordaten. Diese Einstellungen hängen von deiner Anwendung ab; eine werkseitige Konfigurationsoberfläche ist nicht dokumentiert.

## Firmware, Sicherheit und Zurücksetzen {#firmware}

ThingPulse liefert Selbsttest-Firmware. Nutzer entwickeln, installieren und pflegen die Firmware ihrer eigenen Anwendung, einschliesslich WLAN-/BLE-Kommunikation, LTE-Verbindung und Backend-Anbindung. Eine fertige Anwendung, automatische Gateway-Funktion oder Web-Konfigurationsoberfläche gehört nicht zum angegebenen Lieferumfang.

Anwendungsentwickler sollten geschützte Zugangsdaten, authentifizierte Backend-Verbindungen, geeignete Transportverschlüsselung, Fehlerbehandlung und ein wartbares Update-/Wiederherstellungsverfahren umsetzen. Gespeicherte oder übertragene Daten, Rücksetzverhalten und Datenlöschung hängen von der Anwendung ab; dokumentiere dies für deren Nutzer.

**Von ThingPulse noch OFFEN:** Selbsttest-Quellcode/Download und Version, Programmier- und Wiederherstellungsanleitung, Boot-/Tasterverhalten, Daten-/Netzwerkverhalten des Selbsttests, Kontakt für Schwachstellenmeldungen und Supportumfang/-zeitraum für die gelieferten Komponenten und Selbsttest-Firmware. Eine Funktion zum Zurücksetzen auf Werkseinstellungen darf nicht vorausgesetzt werden.

Verwende in deiner Anwendungsfirmware die dokumentierten Antennen, Regionseinstellungen und Funkgrenzen. Kläre mit Intertek, welche nutzerprogrammierbaren Einstellungen und WLAN-/BLE-/LTE-Kombinationen die Bewertung abdeckt; die Lieferung mit Selbsttest-Firmware belegt nicht die Abdeckung jeder Nutzeranwendung.

## Fehlerbehebung {#troubleshooting}

| Symptom | Erste Prüfung |
| --- | --- |
| Gerät startet nicht | Prüfe vorgegebene Stromversorgung, Kabel und Anschluss; trenne die Versorgung bei Schäden. |
| Anwendung überträgt keine Sensordaten | Die ausgelieferte Firmware führt nur den Selbsttest aus. Prüfe, ob deine eigene Anwendung installiert ist und Sensorabfrage sowie Backend-Übertragung implementiert. |
| Ethernet-Verbindung fehlt | Prüfe Kabel und Netzwerkanschluss, danach die Netzwerkeinstellungen der Firmware. |
| LTE-Verbindung fehlt | Prüfe SIM und externen Antennenanschluss bei getrennter Stromversorgung; prüfe Abonnement, Netzabdeckung und APN. Kontaktiere bei vermuteten Fehlern der internen LTE-Antenne den Support. |
| Wiederholte Neustarts oder Verbindungsabbrüche | Prüfe Eignung der Stromversorgung und Umgebungsbedingungen; kontaktiere bei anhaltenden Problemen den Support. |

Die LED-Bedeutungen sind anwendungsspezifisch; beachte die Dokumentation deines Firmwareentwicklers. **OFFEN:** Erfolgs-/Fehleranzeigen des ausgelieferten Selbsttests und Wiederherstellungsanleitung ergänzen. Nenne dem Support Modell, Hardware-/Firmwareversion und Fehlerbeschreibung. Veröffentliche keine SIM-Zugangsdaten oder Netzwerkpasswörter.

## Regulatorische Informationen {#regulatory}

### Vereinigte Staaten {#united-states}

**OFFEN — dieser Entwurf enthält keine Konformitätszusage.** Endgültige FCC-Kennzeichnung für Gerät/Module, anwendbaren Part-15-Betriebshinweis, Änderungshinweis, Störschutzhinweis für die geprüfte Klasse A oder B, gegebenenfalls US-Verantwortlichen und freigegebene HF-Expositions-/Installationshinweise ergänzen. Die Bewertung muss auch die LTE-Zulassung für lizenzierte Funkdienste und gleichzeitigen Sendebetrieb abdecken.

### Europäische Union {#european-union}

**OFFEN — keine Erklärung ausgestellt.** Unterzeichnete EU-Konformitätserklärung oder vereinfachte Erklärung mit funktionierender URL zur vollständigen unterzeichneten Erklärung ergänzen. Nutzungsbeschränkungen, freigegebene Frequenzbänder und maximale Sendeleistungen angeben. Erforderliche Sprachfassungen für die Zielländer mitliefern.

### Entsorgung {#disposal}

Sammle Elektro- und Elektronikgeräte getrennt vom Hausmüll. Nutze geeignete örtliche Sammel- oder Rücknahmestellen. **OFFEN:** Geltende Rücknahmeinformationen des Herstellers ergänzen und endgültige WEEE-Kennzeichnung bestätigen.

## Dokumentversion {#document-revision}

| Version | Datum | Umfang |
| --- | --- | --- |
| 0.1 | 2026-10-12 | Erste vorläufige Anleitung; Seriendaten und regulatorische Prüfung offen |
| 0.2 | 2026-10-12 | Mitgeliefertes Gehäuse/Antennen, USB-C-Versorgung und Bauteilbezeichnungen aus Schaltplan ergänzt; Seriennenndaten und Zulassungen weiterhin offen |
| 0.3 | 2026-10-12 | LTE-Identität gemäss bestätigter Lieferantenauswahl aktualisiert; Abgleich mit Schaltplan/BOM offen |
| 0.4 | 2026-10-12 | Platinenbeschriftung und Datumsaufdruck erfasst; Platinenfamilie, bestücktes Modem und Modell des fertigen Geräts unterschieden |
| 0.5 | 2026-10-12 | Produktbezeichnung, GTIN-13, Inhalt und angegebene Hardwareherkunft der Verpackung ergänzt |
| 0.6 | 2026-10-12 | LLSE-spezifische Mobilfunkfähigkeiten ergänzt und GTIN als SKU bestätigt; endgültige HF-Leistungen und aktivierte Bänder weiterhin offen |
| 0.7 | 2026-10-12 | Bestätigte juristische Person und Postadresse des Herstellers ergänzt |
| 0.8 | 2026-10-12 | Lieferung nur mit Selbsttest-Firmware und nutzerentwickelte WLAN-/BLE-zu-LTE-Anwendungen bestätigt; Einrichtung und Firmwareumfang angepasst |
| 0.9 | 2026-10-12 | Firmwareabhängige LED-Bedeutungen bestätigt; Selbsttestanzeigen separat weiterhin offen |
