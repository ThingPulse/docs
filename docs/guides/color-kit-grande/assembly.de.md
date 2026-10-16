# Zusammenbau

Es gibt verschiedene Möglichkeiten, den Bausatz zusammenzubauen.
Die folgende Vorgehensweise halten wir für die meisten Anwender für sinnvoll.
Lies sie in Ruhe durch und prüfe anschliessend noch einmal, ob sie auch für dich passt.
Bei Bedarf kannst du die Vorgehensweise anpassen.

Wie auf unserer Produktseite im Shop gezeigt, ist vorgesehen, die ESP32-Mikrocontrollerplatine steckbar mit der Anschlussplatine zu verbinden.
Wenn dich die dadurch etwas grössere Bauhöhe stört, kannst du die ESP32-Platine mit den Stiftleisten auch direkt an die Anschlussplatine löten.
Möglicherweise musst du dann die überstehenden Stifte auf der anderen Seite der Anschlussplatine kürzen, damit sie das Displaymodul nicht berühren.

!!! note "Hinweis"

    Im [Abschnitt weiter unten](#operating-the-fpc-connectors) erfährst du, wie du die FPC-Steckverbinder öffnest und schliesst.

!!! danger "Achtung"

    Behandle das empfindliche Display und seine FPC-Flachbandkabel besonders vorsichtig.
    Knicke oder falte die Flachbandkabel NICHT, ziehe nicht daran und belaste weder die Kabel noch ihre Verbindung zum Display auf andere Weise.

!!! tip "Tipp"

    Falls beim Zusammenbau ein Teil verloren geht oder beschädigt wird, kannst du [Ersatzteile](replacement-parts.md) bestellen, ohne einen vollständigen neuen Bausatz kaufen zu müssen.

## Schritt-für-Schritt-Anleitung

| [![](../../img/guides/color-kit-grande/0_clean_pads.png)](../../img/guides/color-kit-grande/0_clean_pads.png) | Reinige zuerst alle Lötpads mit Alkohol und einem Wattestäbchen. |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [![](../../img/guides/color-kit-grande/1_40female_split.png)](../../img/guides/color-kit-grande/1_40female_split.png) | Kürze die Buchsenleisten auf die benötigte Länge (12 und 16 Kontakte) und löte sie an die Anschlussplatine. |
| [![](../../img/guides/color-kit-grande/4_male_pin_1.png)](../../img/guides/color-kit-grande/4_male_pin_1.png) | Kürze die Stiftleisten auf die benötigte Länge (12 und 16 Stifte). |
|[![](../../img/guides/color-kit-grande/4_male_pins_in_pos.png)](../../img/guides/color-kit-grande/4_male_pins_in_pos.png) | Stecke die Stiftleisten für einen stabilen Halt in die bereits eingelöteten Buchsenleisten. |
|[![](../../img/guides/color-kit-grande/0_correct%20soldering.png)](../../img/guides/color-kit-grande/0_correct%20soldering.png) | Gute Löttechnik: Erhitze mit dem Lötkolben sowohl den Stift als auch das Lötpad. Führe dann Lötzinn zu, während du die Lötstelle weiter erhitzt. Das Bild zeigt Beispiele für problematische Lötstellen. Entferne überschüssiges Lötzinn mit einer Entlötpumpe oder Entlötlitze. |
|[![](../../img/guides/color-kit-grande/4_male_pin_esp32_epulse.png)](../../img/guides/color-kit-grande/4_male_pin_esp32_epulse.png) | Löte die Stiftleisten an die ESP32-Platine. |
| [![](../../img/guides/color-kit-grande/2_power_switch_1.png)](../../img/guides/color-kit-grande/2_power_switch_1.png) | OPTIONAL, aber empfohlen: Löte den Ein-/Ausschalter an die Platine. Das Gerät funktioniert auch ohne Schalter, dieser ist später jedoch praktisch. |
| [![](../../img/guides/color-kit-grande/3_grove_connector.png)](../../img/guides/color-kit-grande/3_grove_connector.png) | OPTIONAL: Löte die Grove-Buchse an die Platine. Sieh dir dazu das Video zum Löten von SMD-Bauteilen auf der Seite [Videoanleitungen](video-tutorials.md) an. Du kannst die Buchse auch später jederzeit problemlos ergänzen. |
| [![](../../img/guides/color-kit-grande/6_display.png)](../../img/guides/color-kit-grande/6_display.png) | Lege das Display mit der Vorderseite nach unten auf eine saubere Oberfläche, damit es nicht zerkratzt. **Klebe das Display noch NICHT an die Platine! Dieser Schritt folgt erst nach dem Hardwaretest.** |
| [![](../../img/guides/color-kit-grande/7_FPC.png)](../../img/guides/color-kit-grande/7_FPC.png)  | Führe die beiden FPC-Kabel des Displaymoduls durch die Aussparungen der Platine und stecke sie in die Steckverbinder. Im [Abschnitt weiter unten](#operating-the-fpc-connectors) erfährst du, wie du diese richtig öffnest und schliesst. Klappe das Display vorsichtig (!) um, sodass es auf den Schaumstoff-Klebepads liegt, deren Schutzfolie noch angebracht ist. Drehe beide Teile gemeinsam um und prüfe, ob alles passt. |
| [![](../../img/guides/color-kit-grande/CH9102F-driver.png)](../../img/guides/color-kit-grande/CH9102F-driver.png) | Teste die Hardware jetzt mit einem einfachen Programm. So stellst du sicher, dass alles funktioniert, *bevor* du das Display dauerhaft mit den Klebepads an der Anschlussplatine befestigst. Einmal angeklebt, lässt es sich nur schwer wieder lösen. Wenn du auf diesem Computer zum ersten Mal mit einem ESP32 ePulse Feather arbeitest, installiere jetzt bei Bedarf den Treiber für den CH9102F-USB-Seriell-Chip. Folge dazu der [Treiberanleitung von Adafruit](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102). |
| [![](../../img/guides/color-kit-grande/app-market-1.png)](../../img/guides/color-kit-grande/app-market-1.png) | Öffne die [Webanwendung zum Flashen](https://app-market.thingpulse.com/device/tp-color-kit-grande/app/tp-color-kit-grande-screen-test). |
| [![](../../img/guides/color-kit-grande/8_programm.png)](../../img/guides/color-kit-grande/8_programm.png) | Verbinde dein Color Kit Grande über ein USB-C-Kabel mit deinem Computer. Stelle den Ein-/Ausschalter auf „Ein“. |
| [![](../../img/guides/color-kit-grande/app-market-2.png)](../../img/guides/color-kit-grande/app-market-2.png) | Klicke auf „Flash App“ und wähle den Anschluss deines Geräts aus. Unter Mac OS X heisst das Gerät cu.wch*. Auf anderen Betriebssystemen kann der Name abweichen. |
| [![](../../img/guides/color-kit-grande/app-market-3.png)](../../img/guides/color-kit-grande/app-market-3.png) | Der Browser überträgt nun das Testprogramm auf das Gerät. Das sollte nur wenige Sekunden dauern. Am Ende sollten alle vier Fortschrittsbalken 100 % anzeigen.<br><br>Flashen nicht erfolgreich abgeschlossen? Sieh in der [Fehlerbehebung](troubleshooting.md#hardwareprobleme) nach. |
| [![](../../img/guides/color-kit-grande/testbed.jpg)](../../img/guides/color-kit-grande/testbed.jpg) | <p>Nach dem Flashen der Firmware solltest du vier farbige Kästchen und etwas Text sehen. Durch Berühren des Displays kannst du darauf zeichnen.</p><div class="admonition warning"><p class="admonition-title">Display bleibt dunkel oder Touch funktioniert nicht?</p><p>Wenn du die vier farbigen Kästchen nicht siehst oder nicht mit dem Finger zeichnen kannst, nutze die **[Color-Kit-Grande-Fehlerbehebung](troubleshooting.md)**, um das Problem einzugrenzen. Dort findest du auch den **[Selbsttest-Assistenten](https://ckg-self-test.thingpulse.com/)**; befolge dessen Vorbereitungsanweisungen, bevor du die Diagnosetests ausführst.</p><p>Sobald der Display- und Touch-Test funktioniert, fahre mit dem nächsten Montageschritt fort.</p></div> |
| [![](../../img/guides/color-kit-grande/5_tapes.png)](../../img/guides/color-kit-grande/5_tapes.png) | Ziehe auf einer Seite der vier Schaumstoff-Klebepads die Schutzfolie ab und befestige die Pads auf der Vorderseite der Anschlussplatine an den mit „TAPE“ markierten Stellen. |
| [![](../../img/guides/color-kit-grande/10_protective.png)](../../img/guides/color-kit-grande/10_protective.png)  | Entferne die verbleibende Schutzfolie von den Schaumstoff-Klebepads. |
| [![](../../img/guides/color-kit-grande/11_align.png)](../../img/guides/color-kit-grande/11_align.png)  | Befestige das Displaymodul so, dass es an den weissen Markierungen auf der Platine ausgerichtet ist. |

## FPC-Steckverbinder bedienen {#operating-the-fpc-connectors}

Die Steckverbinder für die beiden FPC-Kabel (Display und Touchmodul) sind ohne Erfahrung etwas schwierig zu bedienen.
Hinzu kommt, dass die beiden Steckverbindertypen unterschiedlich funktionieren.

- Der kleine Steckverbinder für das Touchmodul hat eine schwarze Verriegelung. Hebe sie vorsichtig an, bis sie im rechten Winkel (90°) zur Basis steht.
- Der grosse Steckverbinder für das Display hat einen Verriegelungsbügel, der über seine gesamte Länge verläuft.
Ziehe ihn parallel zur Platine von der Basis weg.
Verwende dazu *zwei Finger* und ziehe an den Vorsprüngen an beiden Enden des Bügels.

Die folgenden Bilder zeigen die offenen und geschlossenen Positionen.

| [![](../../img/guides/color-kit-grande/FPC-connectors-open-empty.jpg)](../../img/guides/color-kit-grande/FPC-connectors-open-empty.jpg) | [![](../../img/guides/color-kit-grande/FPC-connectors-closed-empty.jpg)](../../img/guides/color-kit-grande/FPC-connectors-closed-empty.jpg) |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [![](../../img/guides/color-kit-grande/FPC-connectors-open.jpg)](../../img/guides/color-kit-grande/FPC-connectors-open.jpg)             | [![](../../img/guides/color-kit-grande/FPC-connectors-closed.jpg)](../../img/guides/color-kit-grande/FPC-connectors-closed.jpg)             |
