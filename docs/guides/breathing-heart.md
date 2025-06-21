# Breathing Heart Solder Kit Assembly Guide

Welcome to the assembly guide for the **Breathing Heart Solder Kit**! Whether you're a beginner or a seasoned maker, this guide will walk you step-by-step through the process of building your very own LED breathing heart circuit. The PCB is shaped like a heart and, when assembled, will create a calming pulsing light effect using simple analog electronics.

By the end of this guide, you will have:

- Practiced through-hole soldering
- Learned to identify and place resistors, transistors, capacitors, ICs, and more
- Assembled a beautiful heart-shaped breathing LED circuit

🛠 **Required tools**: soldering iron, solder, flush cutters, and optionally tweezers.


---

## Resistor Color Codes

Understanding the color bands on resistors is crucial for placing the correct components. Below is a quick reference for the resistor values used in this kit. You can identify them either by reading the color bands or by measuring with a multimeter.

<table>
  <thead>
    <tr>
      <th>Value</th>
      <th>Color Bands</th>
      <th>Schematic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="vertical-align: middle;">47kΩ</td>
      <td style="vertical-align: middle;">Yellow, Violet, Orange, Gold</td>
      <td><img src="../../img/guides/breathing-heart/resistor-47k.png" style="width: 200px; height: 100px;" /></td>
    </tr>
    <tr>
      <td style="vertical-align: middle;">10kΩ</td>
      <td style="vertical-align: middle;">Brown, Black, Orange, Gold</td>
      <td><img src="../../img/guides/breathing-heart/resistor-10k.png" style="width: 200px; height: 100px;" /></td>
    </tr>
    <tr>
      <td style="vertical-align: middle;">22Ω</td>
      <td style="vertical-align: middle;">Red, Red, Black, Gold</td>
      <td><img src="../../img/guides/breathing-heart/resistor-22.png" style="width: 200px; height: 100px;" /></td>
    </tr>
    <tr>
      <td style="vertical-align: middle;">100kΩ</td>
      <td style="vertical-align: middle;">Brown, Black, Yellow, Gold</td>
      <td><img src="../../img/guides/breathing-heart/resistor-100k.png" style="width: 200px; height: 100px;" /></td>
    </tr>
  </tbody>
</table>

💡 **Tip**: The **fourth band (gold)** indicates a tolerance of ±5%.  
🧰 **Alternative**: Use a **multimeter** to measure resistance directly if you're unsure.

## LED Orientation and Polarity

LEDs (Light Emitting Diodes) are **polarized components**, meaning they must be installed in the correct direction to work properly.

### How to identify LED legs

- **Long leg** = Positive (**+**) → called the **anode**
- **Short leg** = Negative (**−**) → called the **cathode**

### How to match the LED to the PCB

Each LED slot on the PCB shows a diode symbol like this:

<img src="../../img/guides/breathing-heart/led-footprint.webp" width="120" />

- The **flat edge of the triangle** (left side in the symbol) is the **cathode (−)** → match this with the **short leg** of the LED.
- The **open tip of the triangle** (right side) is the **anode (+)** → match this with the **long leg** of the LED.

### Visual Guide

<img src="../../img/guides/breathing-heart/led-orientation.webp" style="width: 200px;" />

⚠️ If inserted backwards, the LED will not light up. Always verify orientation before soldering!

## Step-by-step Instructions

| Image | Description |
|-------|-------------|
| ![PCB Overview](../img/guides/breathing-heart/1-pcb.webp) | **Step 1: Identify Your PCB**<br>Start by identifying the front side of the PCB. This is where all the components will be placed and soldered. Take a moment to get familiar with the component labels. |
| ![47kΩ Resistors](../img/guides/breathing-heart/2-resistors-47k.webp) | **Step 2: Solder 47kΩ Resistors (R1, R2, R4)**<br>Locate the three 47kΩ resistors. These are marked with color bands: **yellow, violet, orange, gold**. Insert and solder them in the positions labeled R1, R2, and R4. |
| ![10kΩ Resistor](../img/guides/breathing-heart/3-resistors-10k.webp) | **Step 3: Solder 10kΩ Resistor (R6)**<br>Find the resistor marked **brown, black, orange, gold** and solder it into the R6 position. |
| ![22Ω Resistor](../img/guides/breathing-heart/4-resistors-22.webp) | **Step 4: Solder 22Ω Resistor (R5)**<br>This resistor is marked **red, red, black, gold**. Solder it into the R5 spot on the PCB. |
| ![100kΩ Resistor](../img/guides/breathing-heart/5-resistors-100k.webp) | **Step 5: Solder 100kΩ Resistor (R3)**<br>The 100kΩ resistor has the color code **brown, black, yellow, gold**. Place it in the R3 slot. |
| ![Insert IC](../img/guides/breathing-heart/6-ic.webp) | **Step 6: Insert LM358N IC (U1)**<br>Carefully insert the LM358N chip into the U1 position. Make sure the **notch or dot** on the chip matches the notch printed on the PCB. |
| ![Adjustable Resistor](../img/guides/breathing-heart/7-adj-resistor.webp) | **Step 7: Solder Adjustable Resistor (VR1)**<br>Insert the blue adjustable resistor (also known as a potentiometer) into the VR1 slot. |
| ![Transistor](../img/guides/breathing-heart/8-transistor.webp) | **Step 8: Solder Transistor (Q1)**<br>The transistor goes into the Q1 position. Make sure to align the flat side of the component with the flat side printed on the board. |
| ![Electrolytic Capacitor](../img/guides/breathing-heart/9-condensator.webp) | **Step 9: Solder Electrolytic Capacitor (C1)**<br>Pay attention to polarity! The longer leg is positive and should go into the hole marked with a plus (+). Also check the photo in the next step for orientation |
| ![Capacitor Close-up](../img/guides/breathing-heart/10-condensator-closeup.webp) | **Step 10: Check Capacitor Orientation**<br>Double-check that the negative stripe on the capacitor aligns with the negative marking on the PCB. |
| ![Tactile Switch](../img/guides/breathing-heart/11-switch.webp) | **Step 11: Solder the Switch (S1)**<br>Insert the tactile switch into the S1 slot labeled "power". Make sure it is pushed in all the way before soldering. |
| ![LED Orientation](../img/guides/breathing-heart/13-leds.webp) | **Step 12: Place All LEDs**<br>Insert the LEDs into the board. Make sure to match polarity: the **long leg** goes in the **round hole (+)**, and the **short leg** in the **square hole (-)**. |
| ![All LEDs Placed](../img/guides/breathing-heart/13-leds.webp) | **Step 13: Verify LED Placement**<br>All 20 LEDs should now be in place. Double-check that all the long legs are on the correct side before soldering. |
| ![All LEDs Placed](../img/guides/breathing-heart/14-battery-box.webp) | **Step 14: Solder Battery Box**<br>Solder the battery box wires: red to + and black to - |

---



