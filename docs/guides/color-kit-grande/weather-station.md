# Weather Station Project

After completing the [assembly test](assembly.md) and [development environment setup](development-environment.md), you can install the Weather Station Touch project.

!!! important "Two uploads are required"

    Installing the Weather Station requires **both** the filesystem (which contains the icons) **and** the firmware (the program). Follow [Upload 1 of 2](#upload-the-file-system-to-device), then [Upload 2 of 2](#upload-code-to-device). Uploading the firmware alone does not install the icons.

## Obtain the code

The Weather Station sample project is, as all of ThingPulse's open-source code, publicly accessible on GitHub.
Hence, there are two options to download the code:

- Clone the repository with Git: `git clone https://github.com/ThingPulse/esp32-weather-station-touch`
- Download the sources from https://github.com/ThingPulse/esp32-weather-station-touch/archive/master.zip and unpack
  them somewhere to your local file system.

## Open project in Visual Studio Code

- Start VS Code
- ==File== > ==Open Folder...==
- Find and select the `esp32-weather-station-touch` folder from the previous step.

## Configuration & customization

Open `src/settings.h` and follow the comments in the "User settings" section at the top to configure your station. Enter your OpenWeatherMap API key ([how to get a key](../../how-tos/openweathermap-key.md)) and save your changes before uploading.

## Upload 1 of 2: Filesystem and icons {#upload-the-file-system-to-device}

**Required for the first installation.** This upload installs the files used by the Weather Station, including the weather icons.

1. Connect the kit to your computer with a USB data cable.
2. Click the **PlatformIO** icon in the left sidebar.
3. Select ==Platform== > ==Upload Filesystem Image== in the project tasks.
4. Wait for the task to finish and check the terminal output for **SUCCESS**. If it fails, follow the [upload troubleshooting guidance](troubleshooting.md#hardware-problems), then retry. Do not continue until this upload succeeds.

![Upload the filesystem and icons with PlatformIO](../../img/how-tos/platformio-filesystem.png)

After a successful upload, **continue with Upload 2 of 2 below**. The filesystem upload does not install the Weather Station program.

You normally only need to repeat this step if the filesystem files change, the flash is erased, or the icons are missing.

## Upload 2 of 2: Firmware {#upload-code-to-device}

**Required for the first installation and whenever you change code or configuration.** This upload installs the Weather Station program and your saved settings.

1. Confirm that [Upload 1 of 2: Filesystem and icons](#upload-the-file-system-to-device) completed successfully.
2. In the PlatformIO project tasks, select ==General== > ==Upload and Monitor==.
3. Wait for the upload to finish and check the terminal output for **SUCCESS**. The serial monitor then opens to show messages from the device. If the upload fails, use the [troubleshooting guide](troubleshooting.md#hardware-problems) before retrying.

![Upload the firmware and open the serial monitor with PlatformIO](../../img/how-tos/platformio-task-upload.png)

The upload shortcut in the bottom status bar uploads **firmware only**. It does not replace **Upload Filesystem Image** in step 1.

![PlatformIO shortcuts in the status bar](../../img/how-tos/platformio-upload.png)

!!! note "USB driver"

    If your computer cannot communicate with the kit, check that the CH9102 USB-to-serial driver is installed. See [Adafruit’s driver instructions](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102) and the [upload troubleshooting guidance](troubleshooting.md#hardware-problems).

## Check the result

After both uploads succeed, let the station start and load its weather data. Check that it displays weather information **and icons**.

!!! warning "Text appears, but the weather icons are missing?"

    The icons are stored in the filesystem, separately from the firmware. Return to [Upload 1 of 2: Filesystem and icons](#upload-the-file-system-to-device) and make sure **Upload Filesystem Image** completes successfully. Uploading only the firmware again will not install the missing icons. See [Troubleshooting: missing icons](troubleshooting.md#missing-icons) if the problem remains.

    ![Weather Station displaying text and readings without weather icons](../../img/guides/color-kit-grande/trouble2_ckg_no_icons.jpeg){ width="240" }

    *Example: weather readings are visible, but the icons are missing. Click the image to enlarge it.*
