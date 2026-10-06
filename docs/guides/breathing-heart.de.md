# Bauanleitung für den Lötbausatz Breathing Heart {#breathing-heart-solder-kit-assembly-guide}

Willkommen zur Bauanleitung für den **Breathing Heart Solder Kit**! Ob du gerade erst anfängst oder bereits Erfahrung hast: Diese Anleitung führt dich Schritt für Schritt durch den Aufbau deiner eigenen LED-Herzschaltung. Die herzförmige Platine erzeugt nach dem Zusammenbau mit einfacher analoger Elektronik einen ruhigen, pulsierenden Lichteffekt.

Am Ende dieser Anleitung hast du:

- das Löten bedrahteter Bauteile geübt,
- Widerstände, Transistoren, Kondensatoren, ICs und weitere Bauteile kennengelernt und eingesetzt,
- eine herzförmige Schaltung mit pulsierenden LEDs aufgebaut.

🛠 **Benötigte Werkzeuge:** Lötkolben, Lötzinn, Elektronik-Seitenschneider und optional eine Pinzette.

---

## Widerstandsfarbcodes {#resistor-color-codes}

Die Farbringe helfen dir, die richtigen Widerstände einzusetzen. Die folgende Übersicht zeigt die im Bausatz verwendeten Werte. Du kannst sie anhand der Farbringe bestimmen oder mit einem Multimeter messen.

| Wert | Farbringe | Darstellung |
|------|-----------|-------------|
| 47 kΩ | Gelb, Violett, Orange, Gold | ![Farbringe eines 47-kΩ-Widerstands](../img/guides/breathing-heart/resistor-47k.png){ width="200" height="100" } |
| 10 kΩ | Braun, Schwarz, Orange, Gold | ![Farbringe eines 10-kΩ-Widerstands](../img/guides/breathing-heart/resistor-10k.png){ width="200" height="100" } |
| 22 Ω | Rot, Rot, Schwarz, Gold | ![Farbringe eines 22-Ω-Widerstands](../img/guides/breathing-heart/resistor-22.png){ width="200" height="100" } |
| 100 kΩ | Braun, Schwarz, Gelb, Gold | ![Farbringe eines 100-kΩ-Widerstands](../img/guides/breathing-heart/resistor-100k.png){ width="200" height="100" } |

💡 **Tipp:** Der **vierte Ring (Gold)** steht für eine Toleranz von ±5 %.  
🧰 **Alternative:** Wenn du unsicher bist, miss den Widerstand direkt mit einem **Multimeter**.

## Ausrichtung und Polarität der LEDs {#led-orientation-and-polarity}

LEDs (Leuchtdioden) sind **gepolte Bauteile**. Sie müssen richtig herum eingesetzt werden, damit sie funktionieren.

### LED-Anschlüsse erkennen {#how-to-identify-led-legs}

- **Langer Anschluss** = positiv (**+**) → **Anode**
- **Kurzer Anschluss** = negativ (**−**) → **Kathode**

### LEDs passend zur Platine einsetzen {#how-to-match-the-led-to-the-pcb}

An jeder LED-Position auf der Platine ist ein Diodensymbol wie dieses aufgedruckt:

![LED-Markierung auf der Platine](../img/guides/breathing-heart/led-footprint.webp){ width="120" }

- Die **flache Kante des Dreiecks** (links im Symbol) kennzeichnet die **Kathode (−)**. Hier gehört der **kurze Anschluss** der LED hin.
- Die **offene Spitze des Dreiecks** (rechts) kennzeichnet die **Anode (+)**. Hier gehört der **lange Anschluss** hin.

### Bildliche Orientierungshilfe {#visual-guide}

![Ausrichtung der LED-Anschlüsse](../img/guides/breathing-heart/led-orientation.webp){ width="200" }

⚠️ Eine verkehrt herum eingesetzte LED leuchtet nicht. Prüfe die Ausrichtung immer vor dem Löten!

## Videoanleitung von DevHackMod {#instruction-video-by-devhackmod}

<iframe width="688" height="387" src="https://www.youtube.com/embed/3GQW5VFc7fk?si=BbdgI1Cdumdd-kd5" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Schritt-für-Schritt-Anleitung {#step-by-step-instructions}

| Bild | Beschreibung |
|------|--------------|
| ![Übersicht der Platine](../img/guides/breathing-heart/1-pcb.webp) | **Schritt 1: Platine kennenlernen**<br>Bestimme zunächst die Vorderseite der Platine. Hier werden alle Bauteile eingesetzt und verlötet. Mache dich mit den Bauteilbeschriftungen vertraut. |
| ![47-kΩ-Widerstände](../img/guides/breathing-heart/2-resistors-47k.webp) | **Schritt 2: 47-kΩ-Widerstände einlöten (R1, R2, R4)**<br>Suche die drei 47-kΩ-Widerstände mit den Farbringen **Gelb, Violett, Orange, Gold**. Setze sie an den Positionen R1, R2 und R4 ein und löte sie fest. |
| ![10-kΩ-Widerstand](../img/guides/breathing-heart/3-resistors-10k.webp) | **Schritt 3: 10-kΩ-Widerstand einlöten (R6)**<br>Suche den Widerstand mit den Farbringen **Braun, Schwarz, Orange, Gold** und löte ihn an Position R6 ein. |
| ![22-Ω-Widerstand](../img/guides/breathing-heart/4-resistors-22.webp) | **Schritt 4: 22-Ω-Widerstand einlöten (R5)**<br>Dieser Widerstand trägt die Farbringe **Rot, Rot, Schwarz, Gold**. Löte ihn an Position R5 auf der Platine ein. |
| ![100-kΩ-Widerstand](../img/guides/breathing-heart/5-resistors-100k.webp) | **Schritt 5: 100-kΩ-Widerstand einlöten (R3)**<br>Der 100-kΩ-Widerstand hat den Farbcode **Braun, Schwarz, Gelb, Gold**. Setze ihn an Position R3 ein. |
| ![IC einsetzen](../img/guides/breathing-heart/6-ic.webp) | **Schritt 6: LM358N-IC einsetzen (U1)**<br>Setze den LM358N-Chip vorsichtig an Position U1 ein. Die **Kerbe oder der Punkt** auf dem Chip muss zur aufgedruckten Kerbe auf der Platine passen. |
| ![Einstellbarer Widerstand](../img/guides/breathing-heart/7-adj-resistor.webp) | **Schritt 7: Einstellbaren Widerstand einlöten (VR1)**<br>Setze den blauen einstellbaren Widerstand, auch Potentiometer genannt, an Position VR1 ein. |
| ![Transistor](../img/guides/breathing-heart/8-transistor.webp) | **Schritt 8: Transistor einlöten (Q1)**<br>Der Transistor gehört an Position Q1. Richte seine flache Seite an der flachen Seite der aufgedruckten Umrisslinie aus. |
| ![Elektrolytkondensator](../img/guides/breathing-heart/9-condensator.webp) | **Schritt 9: Elektrolytkondensator einlöten (C1)**<br>Achte auf die Polarität! Der längere Anschluss ist positiv und gehört in das mit Plus (+) markierte Loch. Vergleiche die Ausrichtung auch mit dem Foto im nächsten Schritt. |
| ![Nahaufnahme des Kondensators](../img/guides/breathing-heart/10-condensator-closeup.webp) | **Schritt 10: Ausrichtung des Kondensators prüfen**<br>Prüfe erneut, ob der Minusstreifen am Kondensator zur Minusmarkierung auf der Platine passt. |
| ![Taster](../img/guides/breathing-heart/11-switch.webp) | **Schritt 11: Schalter einlöten (S1)**<br>Setze den Druckschalter an Position S1 mit der Beschriftung „power“ ein. Drücke ihn vor dem Löten vollständig in die Platine. |
| ![Ausrichtung der LEDs](../img/guides/breathing-heart/13-leds.webp) | **Schritt 12: Alle LEDs einsetzen**<br>Setze die LEDs in die Platine ein. Achte auf die Polarität: Der **lange Anschluss** gehört in das **runde Loch (+)**, der **kurze Anschluss** in das **quadratische Loch (−)**. |
| ![Alle LEDs eingesetzt](../img/guides/breathing-heart/13-leds.webp) | **Schritt 13: LED-Positionen prüfen**<br>Alle 20 LEDs sollten jetzt eingesetzt sein. Prüfe vor dem Löten noch einmal, ob sich alle langen Anschlüsse auf der richtigen Seite befinden. |
| ![Batteriehalter anschliessen](../img/guides/breathing-heart/14-battery-box.webp) | **Schritt 14: Batteriehalter anlöten**<br>Löte die Leitungen des Batteriehalters an: Rot an + und Schwarz an −. |

---
