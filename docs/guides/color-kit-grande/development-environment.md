# Development Environment

This page prepares your computer to configure and upload the [Weather Station project](weather-station.md). You only need to do this setup once.

You will install three tools: **Visual Studio Code** (VS Code), the editor; **Git**, which downloads a required project library; and **PlatformIO IDE**, the VS Code extension that builds and uploads the firmware. Keep your computer connected to the internet during setup.

## Installation Steps

### 1. Install Visual Studio Code

1. Download the desktop version of [Visual Studio Code](https://code.visualstudio.com/) for your operating system.
2. Install it and open it.

### 2. Install Git {#install-git}

Git is required even if you download the Weather Station project as a ZIP file. PlatformIO uses it to download a library needed by the project.

1. Follow the [Git installation instructions](https://git-scm.com/install/) for your operating system. If Git is already installed, go straight to the check below.
2. After installation, quit VS Code completely and open it again.
3. In VS Code, select **Terminal > New Terminal**. In the terminal panel that opens, type the following command and press Enter:

    ```text
    git --version
    ```

You should see a response starting with `git version`, followed by a version number. If the command is not found or not recognized, finish installing Git and restart VS Code before continuing. See the [Git troubleshooting instructions](troubleshooting.md#software-problems) if needed.

### 3. Install PlatformIO IDE

1. In VS Code, open **View > Extensions**. You can also use **Ctrl+Shift+X** on Windows/Linux or **Cmd+Shift+X** on macOS.
2. Search for **PlatformIO IDE** and select the extension published by **PlatformIO**.
3. Click **Install**. Wait for the extension and its initial setup to finish; this can take several minutes. Follow any prompt to restart or reload VS Code.
4. Click the **PlatformIO** icon in the left sidebar, then open **Home** under **Quick Access**.

![PlatformIO IDE in the VS Code Extensions view](../../img/how-tos/platformio-install.png)

!!! note "Linux setup"

    PlatformIO also requires the `python3-venv` package on Linux. See the [official installation instructions](https://docs.platformio.org/en/latest/integration/ide/vscode.html#installation) for this requirement and further setup help.

## Ready to continue?

You are ready when:

- `git --version` prints a version number in the VS Code terminal.
- PlatformIO Home opens without an installation error.

Continue with **[Weather Station Project](weather-station.md#obtain-the-code)** to download and open the existing project. You do not need to create a new PlatformIO project or complete the Blink tutorial.

## If setup does not work

- **PlatformIO is missing from the sidebar:** Open **View > Extensions** and check that PlatformIO IDE is installed and enabled. Let setup finish, then restart VS Code.
- **PlatformIO reports an installation error:** Note the exact message and consult the [PlatformIO installation guide](https://docs.platformio.org/en/latest/integration/ide/vscode.html#installation). If you remain stuck, [contact support](troubleshooting.md#contact-support) with your operating system and the error message or a screenshot.
- **PlatformIO asks you to install Git:** Follow [Install Git](#install-git) above and check the command in a newly opened VS Code terminal.

## Video Tutorial

If you prefer a video, see [Video Tutorials](video-tutorials.md) for a walkthrough of the development environment setup.
