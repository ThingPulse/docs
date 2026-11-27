# Hardware evidence and engineering follow-up

Revision 0.4 • 12 October 2026 • Internal review record

## Sources and limits

- User confirmation, 12 October 2026: device supplied with enclosure, external 2.4 GHz Wi-Fi antenna, internal LTE foil antenna; power through USB-C. Whether an external power adapter or cable is supplied was not stated.
- Supplied PDF: `ESPGateway_Ethernet_LTE_20261030.pdf`, inspected on all three sheets. Source location: `/Users/deichhor/Downloads/ESPGateway_Ethernet_LTE_20261030.pdf`. No copy has been added to the public website.
- Drawing title: `esp32-ethernet-gateway_with_sim7600`; title blocks show revision **1.0.3**, date **2026-08-30**. The filename date `20261030` differs from the title-block date and is later than this review. Confirm the production revision; do not treat the filename as the release date.

A schematic documents design intent. It does not establish the fitted BOM, finished-device ratings, approved accessories, firmware behavior, FCC grants or conformity of the assembled product.

## Box identification supplied by the user

The attached box-label artwork identifies the sale product as **ESPGateway Ethernet LTE**, with printed GTIN-13/EAN **7649998893091**. It lists one ESPGateway Ethernet and one A7670G (Global) LTE module and states `Hardware Made in China`. See the [box-label review](label-and-insert.md) for the exact text and outstanding checks. This GTIN identifies the product, not an individual unit; no unit serial number is visible on this label.

## PCB identification supplied by the user

The supplied marking image reads exactly:

```text
THINGPULSE
2026/08/30
ESP32 Ethernet Gateway
with SIM760x and A7670x support
```

This is now recorded as the existing PCB identification. The date matches the schematic title-block date, but does not independently establish a hardware revision number, manufacturing date or serial/batch identifier. User clarification on 8 November 2026 identifies `2026/08/30` as the revision marking of the unit supplied to Intertek. Map that sample to the production BOM; this does not identify the later November mounting-hole variant.

The family-support wording explains why a shared design may retain SIM7600 terminology. It does not identify the installed LTE modem or show that every supported assembly is covered by the same assessment. The earlier recommendation to replace every SIM7600 designation was too broad: reconcile the shared design with the actual fitted variant and make that variant unambiguous in the submission documents.

The box now establishes the finished-device product designation. The user confirms GTIN 7649998893091 is the SKU, with no separate sale SKU. The pictured marking does not show an input rating, full manufacturer address or approval identifier; it is not enough to complete the proposed finished-product label. Retain the exact PCB wording in the hardware record and identify the finished product by name and SKU/GTIN.

## Supplier selection supersedes schematic LTE identity

The user identified the [AND-Global BK-A7670G supplier listing](https://www.and-global.com/list_23/662.html) as the LTE assembly used. Checked 12 October 2026: the description names SIMCom A7670G-LLSE, LTE Cat 1. Use this selection in the manual; retain the old schematic designation only as a discrepancy to resolve.

Before submission, identify the selected U6 assembly unambiguously in the schematic/BOM variant records, record the board revision and photograph the fitted modem marking. Obtain the matching FCC grant/ID, integration instructions, EU conformity/test evidence and board power/pinout documentation from the supplier. The product listing does not establish host authorization, approved bands, RF exposure conditions or the finished gateway power rating. Supplier board origin is not sufficient evidence of finished-product customs origin.

## Observations used in the manual

| Evidence | Sheet / reference | What can be documented |
| --- | --- | --- |
| ESP32-WROVER-IE-N16R8 | 1 / U3 | Exact designation shown; production fit and enabled radio modes still need confirmation |
| BK-SIM7600 symbol, SIM7600 text, C124418 reference | 1 / U6 | Shared-design designation; does not identify the selected sale assembly. Reconcile the drawing/BOM variant record with the supplier selection. The C-reference is not an FCC ID. |
| UART connection to LTE assembly | 1 / U6 | GPIO14 net connects to assembly RXD; assembly TXD connects to GPIO13 net. Net names retain SDA/SCL suffixes but are used at the assembly's UART pins. |
| LTE assembly VCC connected to VUSB | 1 / U6 | Power supplied from switched USB rail to the assembly; its internal regulation is not shown. Do not infer the bare modem's permissible supply voltage. |
| USB-C receptacle, CC resistors, VBUS and data nets | 2 / USBC2, R19/R20 | USB-C is the power/data connector; no USB-PD controller is shown. User specified 5 V DC, 2 A on 8 November 2026; cable limits and measurement evidence remain open. |
| CH9102F | 2 / U5 | USB-to-UART bridge designation |
| VUSB power switch and 3.3 V regulator | 2 / SW1, Q2 | Switched USB supply and XC6220B331MR-G regulator shown; regulator rating alone is not the complete product input-current rating |
| Four WS2812E-V5 devices | 2 / LED1–LED4 | Four addressable LEDs shown; user confirms colours/patterns/meanings are defined by the firmware implementer. Self-test-specific pass/fail indications remain to be documented |
| Button labelled RST wired to IO4 | 2 / RST | Button input on GPIO4, not a direct EN reset connection in the drawing |
| LAN8720A-CP-TR and HR911105A | 3 / U1, J1 | Ethernet controller and RJ45 connector designations; no PoE input stage shown |
| 10-pin 2.54 mm headers | 1 / X1, X3 | Headers exist in the design; final enclosure access and allowed user connections remain unknown |

## Resolve before freezing the manual and test sample

1. **LTE evidence and variant identification:** supplier link received; obtain the fitted modem marking, board revision, corrected BOM, assembly schematic/datasheet, FCC grant and integration instructions for the selected assembly. Verify pin compatibility with the existing U6 symbol: the seven-pin block does not show SIM holder, antenna connections or internal power circuitry. Do not reuse SIM7600 specifications or approvals.
2. **Antenna evidence:** provide part numbers, datasheets and gain by band for both antennas, plus RF cables/connectors and internal foil mounting photos. Confirm factory installation of the LTE antenna, separation from other radios and whether any additional LTE diversity/GNSS antenna ports are used or left unused. Do not infer these from an assembly block symbol.
3. **Finished-product supply rating:** user specified 5 V DC, 2 A on 8 November 2026; no adapter or USB cable included. This closes the documentation rating field. Supporting measurements, tolerance and cable limits have not been supplied.
4. **Button behavior — closed 9 November:** the user confirms the RST-labelled GPIO4 button does nothing in the shipped self-test firmware. Do not describe it as reset, reboot or factory reset.
5. **Ethernet control inconsistency:** sheet 3's prose note says `GPIO17 - PHY_POWER`; sheet 1 connects `PHY_PWR` to ESP32 IO5 and leaves IO17 unconnected. Resolve against PCB/netlist and firmware. Do not copy the note as a firmware pin assignment.
6. **Product revision:** reconcile filename/title-block dates and confirm the schematic corresponds to the assembled unit submitted to Intertek. The sample revision marking is confirmed as `2026/08/30`; supply the matching final BOM and resolve coverage of the later mounting-hole change.
7. **Remaining physical details:** SIM orientation and holder operation (nano-SIM and screw access confirmed 9 November), connector diagram, power-switch positions, antenna attachment instructions, dimensions, mounting and thermal/environmental limits.

These are documentation and evidence follow-ups, not a completed electrical design review. No safety or RF compliance conclusion is drawn from the schematic.

## Confirmed SKU and cellular documentation update

The user confirmed that GTIN `7649998893091` is also the SKU; no separate sale SKU is assigned. Use product name ESPGateway Ethernet LTE and SKU/GTIN together in the submission and declarations. The user confirmed on 8 November 2026 that neither device serial numbers nor production batch numbers are assigned.

The English/German manuals now record the LLSE-specific band list and module data rates from [SIMCom A7670G-LLSE, version 2021.11](https://datasheet.lcsc.com/datasheet/pdf/a6ff746802142b3caed58b61817fe57c.pdf?productCode=C21264512), a manufacturer-authored datasheet hosted by LCSC. This closes the generic module-capability placeholder, not final gateway RF approval. The datasheet marks certifications as ongoing; it is not evidence of a current grant. Obtain current approval documents independently.

A search also returned an A7670G user manual internally titled A7670X R6 Hardware Design V1.00 (2025-08-25). Its power table and broader band coverage were not applied to the LLSE selection. Request the matching hardware-design manual and production configuration before completing per-band maximum power, frequency ranges and exposure conditions. Include GSM/GPRS/EDGE in the scope decision instead of assuming LTE-only operation.

## Confirmed manufacturer

The user confirmed the legal manufacturer on 12 October 2026: **ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland**. This replaces the manufacturer/address placeholders in both manuals, label/insert text and EU declaration drafts. It does not identify a US responsible party or EU importer/economic operator; those fields remain open. The c/o contact is not automatically recorded as the declaration signatory.

## Confirmed intended use

User confirmation: only self-test firmware is shipped; users write their application firmware. Intended communication is ESP32 Wi-Fi/BLE devices to an LTE backend, with BLE temperature/humidity to MQTT as an example. Self-test version, coverage, radio activity, programming/recovery procedures and firmware assessment scope remain open.

## Power and contents confirmation — 8 November 2026

The user confirms enclosure, PCB, LTE module, LTE antenna and Wi-Fi antenna only; no USB cable or adapter included. USB-C is the sole power source, with no battery or PoE support. This closes the earlier inclusion/power-source questions. The user subsequently specified 5 V DC, 2 A as the product input rating. This is the manufacturer-specified value for the documentation; no measurement or independent verification is claimed.

## Intertek sample revision confirmed — 8 November 2026

The user states that the revision held by René/Intertek is marked `2026/08/30`, and supplies an image showing this marking. Use `2026/08/30` as the sample hardware revision identifier in the manual and label draft. Schematic revision `1.0.3` remains a separate drawing identifier. The confirmation does not establish the revision or assessment coverage of the later November mounting-hole change.

## Fitted LTE assembly photographed — 8 November 2026

User-supplied photographs: `/Users/deichhor/Downloads/IMG_1722.jpeg` (SIM-holder side) and `/Users/deichhor/Downloads/IMG_1723.jpeg` (modem-label side). These photographs identify the user's photographed assembly; matching it to the unit held by Intertek remains to be confirmed.

| Visible marking | Transcription / interpretation |
| --- | --- |
| Modem manufacturer/model | SIMCom A7670G |
| Modem part number | S2-10AZT-Z33CL |
| Modem FCC ID | 2AJYU-8BAE003 — transcribed from label; grant and integration conditions not yet checked |
| Carrier board | `www.and-global.com`, `BKP-7670 V3` |
| Internal LTE antenna marking | `698–960/1710–2690MHz`; no antenna part number or gain visible |

The modem label also carries a module serial number and IMEI. These are component identifiers, not a manufacturer-assigned finished-gateway serial or batch number. Their existence does not change the user's statement that the gateway has no serial/batch scheme.

The photo says A7670G without an LLSE suffix. The previous LLSE-specific supplier identification remains unverified for this fitted part number; obtain matching supplier documentation before treating the earlier band table as this unit's capabilities. Carrier marking `BKP-7670 V3` supersedes the unidentified carrier-revision field for this photographed assembly, but does not by itself resolve supplier catalog naming. The main PCB's `SIM7600` silkscreen is a shared-design marking, not the fitted modem model.

The ESP32 shield is partly cropped in IMG_1722 and its full model/FCC ID cannot be read reliably. A close-up of that shield is still needed. LTE antenna frequency printing does not establish gain, approved antenna type or host authorization.

## Fitted ESP32 module photographed — 8 November 2026

Source: user photograph `/Users/deichhor/Downloads/IMG_1724.jpeg`. Visible markings:

| Field | Transcription |
| --- | --- |
| Manufacturer | Espressif |
| Model | ESP32-WROVER-IE |
| FCC ID | 2AC7Z-ESP32WROVERE |
| IC ID | 21098-ESPWROVERE |

The model marking is consistent with the schematic's ESP32-WROVER-IE family. The full ordering suffix N16R8 remains based on the schematic/BOM record, rather than independently verified from this photograph. The external antenna cable is connected to the module's RF connector. The FCC identifier is transcribed from the shield; grant conditions, approved antenna specifications and host integration have not yet been verified. This photo closes the earlier unreadable ESP32-label item. Confirm that the photographed LTE and ESP32 assemblies match the sample held by Intertek.

## Photographed configuration matched to Intertek sample — 8 November 2026

The user confirms that the unit held by René/Intertek uses the same ESP32 module, LTE module and antennas as the photographed unit. This closes the sample-match question for those components. The recorded module identifiers therefore apply to that sample: ESP32-WROVER-IE, FCC ID `2AC7Z-ESP32WROVERE`, and SIMCom A7670G, FCC ID `2AJYU-8BAE003`, on carrier marked `BKP-7670 V3`. Antenna part numbers, gain specifications and grant/integration review remain open. This confirmation does not establish coverage of the later November mounting-hole change.

## Antenna sourcing confirmed — 8 November 2026

The user confirms René sourced both the Wi-Fi and LTE antennas. René is the follow-up contact for manufacturer/model or part number, datasheets, antenna type, peak gain by operating band, RF connector/cable details and cable loss where available. Ask him to retain the supplied antenna configuration and obtain Intertek's review against the module integration conditions. The photographed LTE frequency marking alone does not close these specification fields.

## Setup confirmations — 9 November 2026

The user confirms nano-SIM format, enclosure access by removing screws, and no PCB-button function in the shipped self-test firmware. SIM orientation, holder mechanism and power-switch positions remain open. No screw count, tool size or card orientation has been inferred.

## Self-test workflow confirmed — 9 November 2026

The user confirms https://iot-flasher.thingpulse.com/device/espgateway-ethernet-lte is the current flashing/testing page. Users start the self-test from this page, rather than automatically at power-on, and read pass/fail results on the web page. Firmware version/hash, browser/connection requirements, test coverage and prerequisites, duration and recovery procedure remain open. No button labels or LED result codes have been invented.

## Installation and temperature — 9 November 2026

User confirms indoor use, desk/shelf placement and wall mounting through enclosure holes. Mounting hardware, dimensions and clearances remain unspecified.

The user proposes adopting the ESP32 module operating temperature. Espressif's [ESP32-WROVER-E/IE datasheet](https://documentation.espressif.com/esp32-wrover-e_esp32-wrover-ie_datasheet_en.html), checked 9 November 2026, lists −40 to +85 °C for ESP32-WROVER-IE-N16R8 and defines ambient as the environment immediately outside the module. Record this as component evidence only. It does not establish the temperature outside the assembled gateway enclosure: internal heating and the limits of the LTE carrier, Ethernet circuitry, power components and other materials must also be considered. No finished-device temperature range has been verified; retain that field as pending and ask René/Intertek what evidence or assessment they need for the intended product rating.

## Enclosure part drawing — 9 November 2026

The user supplied the [AK-NW-05 drawing](https://github.com/htlabnet/SZOMK/blob/master/AK-NW_Network_enclosure/AK-NW-05/AK-NW-05.pdf). Its one page was rendered and visually inspected: base/cover outer footprint 120 × 120 mm; wall-mount keyhole features; central outlined area dimensioned 30 × 50 mm. Full assembled height is not provided by this part drawing. Confirm usable label area on the actual enclosure before dimensioning artwork.
