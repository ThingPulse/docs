# Writing Your Own Application

Use the code in our sample project as a starting point or reference to build your own application.
In particular, see the configuration in `platformio.ini` and `src/settings.h` for pin assignments.

## Touch interface

The sample application does not currently make use of the touch interface.
However, the code does initialize it to ensure it is wired up correctly (`display.h#initTouchScreen`).
Furthermore, there is a commented out snippet at the end of `loop()` that shows how to obtain touch coordinates.

## Hardware extensions / pin assignment

We designed the connector PCB with extensibility in mind.

- You may plug [any I2C Groove module](https://wiki.seeedstudio.com/Grove_System/) into the connector you soldered to the PCB.
The **SCL/SDA pins are 22 and 23** respectively.
- Many of the broken out pins are available for custom extensions.
**Free pins as follows**.
Please see the [Espressif datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf#page=12) for details on those pins.
    - P2 row: 26, 25, 34, 39, 36, 19, RX, TX, 21
    - P3 row: 13, 12, 33, 14
