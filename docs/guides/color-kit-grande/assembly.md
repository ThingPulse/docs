# Assembly Instructions

There are different ways to skin a cat.
The recipe below is what we think is most sensible for most people.
Read it, take a step back, read it again and see if it makes sense for you, too.
Feel free to adjust it if it does not.

As seen on our product page in the shop the intention is for the ESP32 microcontroller board to be pluggable rather than soldered to the connector PCB.
If you are concerned about the little extra height this adds to the whole assembly, you may of course solder the ESP32 board directly to the connector PCB using the male pin headers.
You might need to cut off the pin headers on the other side of the connector PCB such that they will not touch the display module.

!!! note

    See the [dedicated chapter below](#operating-the-fpc-connectors) about how to open & close the FPC connectors.

!!! danger

    Handle the delicate display unit and its FPC ribbons with extra care.
    Be sure to NOT sharply bend (i.e. fold), pull or otherwise apply stress to the ribbon cables and their connection to the unit.

## Step-by-Step Instructions

| [![](../../img/guides/color-kit-grande/0_clean_pads.png)](../../img/guides/color-kit-grande/0_clean_pads.png) | First, clean all soldering pads with alcohol and a cotton swab. |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [![](../../img/guides/color-kit-grande/1_40female_split.png)](../../img/guides/color-kit-grande/1_40female_split.png) | Cut the female pin headers strips to length (12 & 16 pins) and solder them to the connector PCB. |
| [![](../../img/guides/color-kit-grande/4_male_pin_1.png)](../../img/guides/color-kit-grande/4_male_pin_1.png) |  Cut the male pin headers strips to length (12 & 16 pins) |
|[![](../../img/guides/color-kit-grande/4_male_pins_in_pos.png)](../../img/guides/color-kit-grande/4_male_pins_in_pos.png) | Place the male into the already soldered female header pins for better stability |
|[![](../../img/guides/color-kit-grande/0_correct%20soldering.png)](../../img/guides/color-kit-grande/0_correct%20soldering.png) | Good soldering technique: Heat both the pin and the pad with the soldering iron, then add solder wire while continuing to heat. Check the image for examples of problematic solder joints. If you have too much solder on a joint, use a solder pump or solder wick to remove excess solder. |
|[![](../../img/guides/color-kit-grande/4_male_pin_esp32_epulse.png)](../../img/guides/color-kit-grande/4_male_pin_esp32_epulse.png) | Solder the headers to the ESP32 board. |
| [![](../../img/guides/color-kit-grande/2_power_switch_1.png)](../../img/guides/color-kit-grande/2_power_switch_1.png) | OPTIONAL but recommended: solder the on/off switch to PCB. The device works without the power switch, but it will be handy later. |
| [![](../../img/guides/color-kit-grande/3_grove_connector.png)](../../img/guides/color-kit-grande/3_grove_connector.png) | OPTIONAL: solder the Grove connector to the PCB. See "SMD soldering" video tutorial in the [Video Tutorials](video-tutorials.md) section. Can easily be added later anytime. |
| [![](../../img/guides/color-kit-grande/6_display.png)](../../img/guides/color-kit-grande/6_display.png) |  Place the display on a clean surface upside down (as to not scratch it). **Do NOT tape the display to the PCB yet! You will be instructed to do so after testing the hardware.** |
| [![](../../img/guides/color-kit-grande/7_FPC.png)](../../img/guides/color-kit-grande/7_FPC.png)  |  Feed the two FPC cables of the display module through the cut-outs of the PCB. Insert the cables into the sockets. See the [dedicated chapter below](#operating-the-fpc-connectors) on how to correctly open & close the FPC connectors. Carefully(!) fold the display over such that it rests on the (still protected) foam pads and flip the two pieces over to verify everything fits. |
| [![](../../img/guides/color-kit-grande/CH9102F-driver.png)](../../img/guides/color-kit-grande/CH9102F-driver.png) |  Now is a good time to test the hardware with a simple programm. You will want to do this now - rather than at the very end - to verify everything works *before* you permanently tape the display with the stickers to the connector board. It will be hard to remove from the foam stickers once attached. If this is the first time working with an ESP32 ePulse Feather on your current machine you might want to install the driver for the CH9102F serial chip now. Head over to [Adafruit's driver page](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102) and follow their instructions for installing the CH9102F driver. |
| [![](../../img/guides/color-kit-grande/app-market-1.png)](../../img/guides/color-kit-grande/app-market-1.png) |  Open the [flasher web application](https://app-market.thingpulse.com/device/tp-color-kit-grande/app/tp-color-kit-grande-screen-test) |
| [![](../../img/guides/color-kit-grande/8_programm.png)](../../img/guides/color-kit-grande/8_programm.png) |  Connect your Color Kit Grande with a USB-C cable to your computer. Move the power switch to the on-position. |
| [![](../../img/guides/color-kit-grande/app-market-2.png)](../../img/guides/color-kit-grande/app-market-2.png) |  Press the "Flash App" button and select the port of your your device. On Mac OS X it is the cu.wch* device. The name of the device might be different on your operating system  |
| [![](../../img/guides/color-kit-grande/app-market-3.png)](../../img/guides/color-kit-grande/app-market-3.png) |  Now the browser will flash the test program. This should only take a few seconds and at the end there should be four progress bars at 100%  |
| [![](../../img/guides/color-kit-grande/testbed.jpg)](../../img/guides/color-kit-grande/testbed.jpg) |  After the firmware was flashed you should see four colorful boxes and some text. By touching the display you can draw  |
| [![](../../img/guides/color-kit-grande/5_tapes.png)](../../img/guides/color-kit-grande/5_tapes.png) |  Peel off the protective film on one side of the four foam stickers and attach them to the front of the connector PCB in the designated areas ("TAPE"). |
| [![](../../img/guides/color-kit-grande/10_protective.png)](../../img/guides/color-kit-grande/10_protective.png)  |  Remove the remaining protective film from the foam stickers. |
| [![](../../img/guides/color-kit-grande/11_align.png)](../../img/guides/color-kit-grande/11_align.png)  |  Attach the display module such that it aligns with the markings on the PCB (white silk screen). |


## Operating the FPC connectors

The connectors for the two FPC cables (for display and touch module) can be a bit tricky to operate for the inexperienced.
The fact that the two types required here don't work the same does not help.

- The small one for the touch module has a black latch that opens if you gently lift it such that it will protrude from its base in a 90° angle.
- The large one for the display has a locking bar that runs along the full length of the connector.
It needs to be pulled away from its base parallel to the PCB.
*Use two fingers* to pull at the knobs on either end of the bar.

The following pictures indicate the open/closed positions.

| [![](../../img/guides/color-kit-grande/FPC-connectors-open-empty.jpg)](../../img/guides/color-kit-grande/FPC-connectors-open-empty.jpg) | [![](../../img/guides/color-kit-grande/FPC-connectors-closed-empty.jpg)](../../img/guides/color-kit-grande/FPC-connectors-closed-empty.jpg) |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [![](../../img/guides/color-kit-grande/FPC-connectors-open.jpg)](../../img/guides/color-kit-grande/FPC-connectors-open.jpg)             | [![](../../img/guides/color-kit-grande/FPC-connectors-closed.jpg)](../../img/guides/color-kit-grande/FPC-connectors-closed.jpg)             |
