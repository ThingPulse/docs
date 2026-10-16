# Troubleshooting

## Start here

Choose the symptom that matches what you see:

- **Cannot install firmware:** [Computer does not detect the board](#usb-not-detected) or [TestBed installation stays at 0%](#flashing-stuck).
- **Display or touch does not work:** [Dark display](#dark-display), [white screen](#white-screen), or [touch does not respond](#touch-not-working).
- **Weather Station application problems:** [Missing icons](#missing-icons) or [PlatformIO asks for Git](#software-problems).

Start with the checks for your symptom. If they do not resolve a display or connection problem, use the [Self-Test Wizard](#self-test-tool) to investigate further. If you cannot flash the board, resolve that problem first or [contact support](#contact-support).

!!! warning "Before working on the hardware"

    Disconnect USB and any battery or other power source before removing or reconnecting ribbon cables or boards, checking continuity, or soldering. See the illustrated [FPC connector instructions](assembly.md#operating-the-fpc-connectors) before releasing a ribbon cable; do not pull it out with the latch closed. Reconnect power only after the hardware is ready for the next test. During the self-test, attach jumpers only when the wizard instructs you to.

## Hardware Problems

| Symptom | Suggested Solution | Image |
|---------|---------------------|-------|
| <span id="dark-display"></span>The display flickers or stays dark after flashing | First disconnect power and check that the display ribbon cable is fully inserted and its latch is closed; see the [connector instructions](assembly.md#operating-the-fpc-connectors). Reconnect power and repeat the display test. If it still fails, disconnect power and inspect the solder joints between the ePulse Feather and connector board. Use the [Self-Test Wizard](#self-test-tool) to help narrow down connection problems, or follow the [continuity check](#checking-continuity) if you have a multimeter. | [![Display stays dark](../../img/guides/color-kit-grande/trouble1.jpg)](../../img/guides/color-kit-grande/trouble1.jpg) |
| <span id="missing-icons"></span>Weather Station: the display shows text but no icons  | This applies to the Weather Station application, not the TestBed assembly test. This probably means that the filesystem upload was not successful, as the icons are loaded from there. Make sure that you have followed the [Upload the file system to device](weather-station.md#upload-the-file-system-to-device) step | [![](../../img/guides/color-kit-grande/trouble2_ckg_no_icons.jpeg)](../../img/guides/color-kit-grande/trouble2_ckg_no_icons.jpeg) |
| <span id="white-screen"></span>The display shows a white screen  | Disconnect power and check the display ribbon connection first using the [connector instructions](assembly.md#operating-the-fpc-connectors). A poor solder connection can also cause this symptom. Check these pins for cold solder joints:<br><ul><li>TFT_DC (IO02)</li><li>TFT_RESET (IO04)</li><li>TFT_SCK (IO05)</li><li>TFT_MOSI (IO18)</li><li>TFT_MISO (IO19)</li><li>TFT_CS (IO15)</li></ul>Also check these which can be involved:<ul><li>TFT_LED (IO32)</li><li>3V3</li><li>GND</li></ul> | [![](../../img/guides/color-kit-grande/trouble3_ckg_white_screen.png)](../../img/guides/color-kit-grande/trouble3_ckg_white_screen.png) |
| <span id="usb-not-detected"></span>Board powers on (LEDs lit) but the computer does not detect it | Try these checks in order:<br><ol><li>Use a known-good **USB data cable** and try another USB port. A charge-only cable can power the board but cannot transfer data.</li><li>Check that the CH9102F USB-to-serial driver is installed. Follow [Adafruit’s driver guide](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102), then reconnect the board.</li><li>Disconnect all power, remove the ePulse Feather from the connector board, then reconnect USB and try flashing it standalone. If this works, the issue is likely related to the connector board or attached hardware; it does not by itself prove a short circuit.</li><li>Disconnect power again and inspect both sides of both boards for solder bridges, especially around TX/RX and adjacent pins. Rework suspect joints if you are comfortable soldering; otherwise [contact support](#contact-support).</li></ol> | |
| <span id="flashing-stuck"></span>TestBed installation remains at 0% and the serial console repeatedly displays dots, dashes, or connection errors | The installer can see the USB-to-serial adapter, but it cannot establish communication with the ePulse Feather. Try these steps in order:<br><ol><li>**Try another USB cable and USB port.** Some USB cables provide power but do not carry data, and damaged or marginal cables can fail during flashing. If possible, verify the replacement cable by using it to transfer data to another device, such as a smartphone.</li><li>**Verify the CH9102F driver.** Install or reinstall the correct driver by following [Adafruit's CH9102F driver installation guide](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102), then reconnect the board. If the same failure occurs on another computer where the driver works, the driver is less likely to be the cause.</li><li>**Disconnect all power, remove the ePulse Feather from the connector board, then reconnect USB and try flashing it standalone.** If flashing then succeeds, investigate the connector board and attached hardware for connection problems or shorts. This result does not identify the exact fault.</li><li>**Disconnect power and inspect the soldering.** Check both boards carefully for solder bridges, especially around the serial and adjacent pins, and rework any suspicious joints. A short can also be on the ePulse Feather itself, so a standalone failure does not completely rule out a soldering issue.</li><li>If the board still cannot be flashed standalone with a known-good data cable and driver, the **ePulse Feather may be damaged**. Contact support and include clear, in-focus photos of all solder joints on both boards.</li></ol> | [![TestBed installation stuck at 0% while the serial console displays repeated connection attempts](../../img/guides/color-kit-grande/trouble4_testbed-serial-connection.png)](../../img/guides/color-kit-grande/trouble4_testbed-serial-connection.png) |
| <span id="touch-not-working"></span>The display works, but touching it does not draw in TestBed | Disconnect all power. Check that the smaller touch ribbon cable is fully inserted and its black latch is closed; follow the illustrated [connector instructions](assembly.md#operating-the-fpc-connectors). Reconnect power and repeat the TestBed touch test. If touch still fails, disconnect power and inspect the touch connector and solder joints for loose connections or bridges. Use the [Self-Test Wizard](#self-test-tool) for further connection checks; if the problem remains, [contact support](#contact-support) with the results and photos. | |

### Checking continuity

With **all power disconnected**, set your multimeter to continuity mode and touch its probes together to check how it indicates a connection. To check a soldered connection between the boards, place one probe on the metal pin on the ePulse Feather side and the other on the corresponding solder pad on the connector board. Check the same connection at both ends, not two adjacent pins. A connection should give a continuity indication (usually a beep or low resistance). An open connection suggests a joint that needs inspection. If you cannot identify the corresponding points, use the wizard or ask support before reworking the joint.

## Software Problems

| Symptom | Suggested Solution | Image |
|---------|---------------------|-------|
| `Please install git client from https://git-scm.com/download` is displayed in the PlatformIO log | The Weather Station project has a Git-hosted library dependency, so PlatformIO needs a working Git client even if you downloaded the project itself as a ZIP file. Install Git from [git-scm.com/install](https://git-scm.com/install/) and completely restart Visual Studio Code. Open a terminal and run `git --version` to confirm that Git is installed and available on the system `PATH`, then build the project again. | [![PlatformIO log asking to install the Git client](../../img/guides/color-kit-grande/trouble5_platformio-git-client.png)](../../img/guides/color-kit-grande/trouble5_platformio-git-client.png) |

## Self-Test Tool

We provide an online [Self-Test Wizard](https://ckg-self-test.thingpulse.com/) that helps you diagnose issues with your Color Kit Grande.

[![Self-Test Wizard](../../img/guides/color-kit-grande/self-test-wizard.png)](https://ckg-self-test.thingpulse.com/)

### How to use the Self-Test

1. Open the [Self-Test Wizard](https://ckg-self-test.thingpulse.com/) first and read its preparation instructions. Have a jumper wire ready, but **do not connect it yet**.
2. Before removing the display and touch ribbon cables from the connector board, **disconnect USB and any other power source**. Release their latches as shown in the [FPC connector instructions](assembly.md#operating-the-fpc-connectors).
3. Follow the wizard’s setup and connection instructions in order. Attach or move the jumper **only when prompted**, between the exact points highlighted for the current test. The image above shows one test partway through the wizard, not a permanent jumper connection.
4. Observe the wizard’s reset and power-cycle warnings. In particular, the illustrated DC / GPIO 2 jumper must be removed before any reset or power cycle.
5. Record any failed tests and the pin names shown. When finished, disconnect power, remove the test jumper, and reconnect and secure both ribbon cables before powering the kit again. Return to the [assembly display and touch test](assembly.md) once the problem is resolved, or send your results to [support](#contact-support).

### About Quality Assurance

Boards are flashed with self-test firmware and displays are checked in a test harness before shipping. These checks help narrow down troubleshooting, but do not rule out damage or a later component failure.

Poor solder joints can cause problems after assembly. If inspection or testing identifies a suspect joint, disconnect all power before repairing it. Depending on the fault, repairs can include:

- **Re-heating** the problematic solder joint with your soldering iron
- Using a **solder wick** to remove excess solder
- Using a **de-solder pump** to clean up bridges or shorts

Inspect both sides of the boards for bridges, gaps, or loose pins. Appearance alone does not prove a joint is faulty. If you are unsure about a repair, contact support with photos before reworking it.

!!! tip

    If a part is damaged beyond repair, check the [replacement parts](replacement-parts.md) page before buying a complete new kit.

## Contact Support

If none of the above measures resolved your issue, please contact us at **info AT thingpulse.com**. 

To help us diagnose the problem quickly, please include the following information in your email:

```
Subject: Color Kit Grande - Troubleshooting Help

Hi ThingPulse Support,

I am having issues with my Color Kit Grande and need assistance.

**Symptom:**
[Describe what happens - e.g., display stays dark, white screen, no USB connection, etc.]

**What I have tried:**
- [ ] Inspected and reheated solder joints
- [ ] Checked for solder bridges on TX/RX pins
- [ ] Tested with different USB cables
- [ ] Disconnected ePulse Feather from connector board
- [ ] Ran the Self-Test Wizard
- [ ] Other: ___

**Attached photos:**
Please find attached in-focus photos of:
- Top side of the connector board (all solder joints visible)
- Bottom side of the connector board
- Top side of the ePulse Feather board
- Bottom side of the ePulse Feather board

Thank you for your help!
```

!!! tip "Photo Tips"
    Good lighting and sharp focus on the solder joints help us identify issues quickly. We can often spot problematic pins in photos that might not be obvious in person.
