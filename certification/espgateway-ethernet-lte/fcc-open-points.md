# FCC documentation — guided completion

Working record, 9 November 2026. Draft; no compliance declaration issued.

## Current scope and evidence

René's [13 October email](https://mail.google.com/mail/u/0/#all/1a13382c0f694f9f) says Intertek will perform FCC SDoC testing only, requires normal operation, and wants the user manual and all label artwork completed before scheduling. The quoted correspondence records Daniel's 21 September decision to focus on FCC first. EU/CE material in the older review pack is separate future work, not a prerequisite for this FCC submission.

The same email says the application has already been submitted with a partner molding company as Chinese manufacturer. Obtain the actual application and verify the company's role in manufacturing this gateway; its work on CKG enclosures does not establish that role. Retain ThingPulse's confirmed identity and distinguish applicant, manufacturer, assembly site and US responsible party.

The [4 November production order](https://mail.google.com/mail/u/0/#all/1a1a52f9e1435a2a) specifies a larger LTE mounting hole and factory installation of the LTE modem and antenna. Map this changed hardware to the sample submitted to Intertek before freezing documentation.

## Fields already available

| Field | Working value |
| --- | --- |
| Product | ESPGateway Ethernet LTE |
| SKU / GTIN | 7649998893091 |
| Legal manufacturer | ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland |
| Hardware revision of Intertek sample | `2026/08/30`, confirmed by the user and marking image on 8 November 2026; distinct from schematic revision 1.0.3 |
| Serial / production batch number | Neither assigned, confirmed by the user on 8 November 2026 |
| Photographed LTE assembly | SIMCom A7670G, P/N S2-10AZT-Z33CL; FCC ID marking `2AJYU-8BAE003`; carrier `BKP-7670 V3`. User confirms match to Intertek sample; grant review pending. |
| Photographed Wi-Fi/Bluetooth module | Espressif ESP32-WROVER-IE; FCC ID marking `2AC7Z-ESP32WROVERE`; IC ID `21098-ESPWROVERE`. User confirms match to Intertek sample; grant review pending. |
| Power connector | 5 V DC, 2 A via USB-C only; no battery/PoE |
| Installation | Indoor; desk/shelf or wall mounting using enclosure holes. User confirmed 9 November. Finished-device temperature range remains open. |
| Assembly | Enclosed gateway, external Wi-Fi antenna, internal LTE antenna |
| PCB button | No function in shipped self-test firmware, user confirmed 9 November |
| Firmware supplied | Self-test; users develop application firmware |
| Manual | https://docs.thingpulse.com/guides/espgateway-ethernet-lte/ — draft |
| Test tool identified in correspondence | https://iot-flasher.thingpulse.com/device/espgateway-ethernet-lte — user confirmed current page on 9 November; start self-test from page, read pass/fail results there; firmware version still open |
| SIM access | Nano-SIM; remove enclosure screws for access. User confirmed 9 November. Orientation and holder operation still needed |

## Completion sequence

| Step | Open information | Owner / destination |
| --- | --- | --- |
| 1 | Closed by user: 5 V DC, 2 A; no adapter/cable supplied; USB-C only, no battery/PoE | Daniel → manual, label, test setup |
| 2 | Intertek sample revision confirmed: `2026/08/30`. No serial/batch numbering. Open: November mounting-hole variant coverage, grant/integration review; photographed modules and antennas confirmed to match the test sample | Daniel / René → sample record, BOM, label |
| 3 | SIM orientation/holder operation, power-switch positions, self-test version, connection/prerequisites and duration, flashing/recovery, finished-device temperature/environment limits and mounting details | Daniel → manual |
| 4 | User asked Derexter (reported 9 November); awaiting response. No appointment confirmed; eligibility and scope remain open. Need agreed legal entity, US address, telephone or internet contact | Daniel → compliance-information sheet; do not assign the US customer automatically |
| 5 | Module FCC grants and integration instructions; antenna part numbers/gains; host integration and RF exposure review | René / suppliers / Intertek → radio evidence and approved wording |
| 6 | Actual application, accurate company roles, test sample/configuration, Class A/B, applicable rule parts, accepted operating modes | René / Intertek → report and submission scope |
| 7 | Device-label size/location, packaging artwork, final manual and accompanying compliance sheet | Daniel / René, reviewed by Intertek |

SDoC compliance information must identify the product, applicable compliance statement and US-located responsible party: [47 CFR 2.1077](https://www.ecfr.gov/current/title-47/section-2.1077), checked 8 November 2026. SDoC scope and correspondence do not establish authorization of the installed transmitters; obtain Intertek's written assessment of the exact module/antenna/host combination. The marketed configuration must be covered by the tested configuration: [47 CFR 2.906](https://www.ecfr.gov/current/title-47/section-2.906).

## Questions prepared for René / Intertek (not sent)

Antenna sourcing is confirmed: René supplied both antennas. Please provide the manufacturer/model or part number and datasheet for each, antenna type, peak gain by operating band, and RF cable/connector details (including cable loss where available). Have Intertek check these against the module integration conditions. This request remains unsent.

1. Please send the submitted application and identify the actual gateway assembly/manufacturing site's legal name and address. What role is assigned to the molding company, and does it perform that role for this gateway?
2. Please obtain the fitted LTE module's FCC grant and OEM integration instructions from AND-Global, and confirm the Wi-Fi/Bluetooth grant. Please have Intertek confirm how these approvals cover the finished host, antennas and simultaneous operation alongside the booked SDoC work.
3. The test sample is marked `2026/08/30`. Please confirm whether the November mounting-hole change needs any review or updated sample.
4. Please specify normal-operation test instructions: firmware version, Ethernet traffic, Wi-Fi/BLE activity, LTE SIM/network traffic, attached cables and power supply. Is the existing self-test sufficient for the intended measurement?
5. Please confirm Class A/B, exact manual/label statements, label-placement requirements and whether a printed compliance sheet plus the online manual is acceptable. Please confirm the remaining deliverables and test schedule.

## Power and contents answers recorded

- USB-C input: 5 V DC, 2 A, specified by the user on 8 November 2026. Recorded as the manufacturer-specified rating, not a measured test result.
- Confirmed 8 November: enclosure, PCB, LTE module, LTE antenna and Wi-Fi antenna only. No power adapter or USB cable included.
- Confirmed 8 November: USB-C is the only power source; no battery or PoE support.

English/German manuals and label draft updated. Intertek sample hardware revision recorded as `2026/08/30`. No serial or production batch numbers are assigned. Both radio-module model/FCC ID markings recorded from photos; user confirms the photographed modules and antennas match the Intertek sample; both antennas sourced by René, who must provide part numbers/datasheets and gain by band; Derexter contacted by user, reply pending; next: manual setup and firmware details; later production-variant coverage remains open.

## US responsible party — status 9 November 2026

The user reports having asked Derexter. His response is pending; no appointment or consent is recorded. Assess whether his company is the US importer or another eligible party under [47 CFR 2.909(b)](https://www.ecfr.gov/current/title-47/section-2.909), rather than treating a US address alone as sufficient. Clarify the legal entity, commercial/import role, authority to agree, product/configuration and shipment scope, access to compliance records and handling of changes. Do not assume an arrangement for his company's imports covers sales to other US customers.

The role carries compliance and recordkeeping responsibilities; see [47 CFR 2.938](https://www.ecfr.gov/current/title-47/section-2.938). Ask Intertek to confirm the proposed arrangement and documentation before entering company details in released compliance information.

## Temperature follow-up

User proposed the ESP32 range. Component datasheet states −40 to +85 °C immediately around the module; finished enclosed gateway ambient range remains open. René/Intertek: please advise the evidence/assessment needed to establish a product operating range, accounting for the complete BOM and enclosure temperature rise.

## Label scope checked against correspondence — 9 November 2026

Re-read René's 13 October message and quoted thread (Gmail message `1a13382c0f694f9f`). He requests the manual and “all label artworks” before scheduling testing. His 7 October message requests label design including the manual link. Daniel explicitly asked on 22 September and 8 October whether this means the bottom device label, box label or both; no explicit distinction was found in the reviewed replies. Working recommendation: prepare both device and packaging proofs for review, while asking René/Intertek to confirm placement. Do not describe device-label scope as an explicit answer already received.

## Enclosure drawing received — 9 November 2026

User linked https://github.com/htlabnet/SZOMK/blob/master/AK-NW_Network_enclosure/AK-NW-05/AK-NW-05.pdf . Downloaded and visually inspected its single page. It depicts a base/cover part with a 120 × 120 mm outer footprint, wall-mount keyhole features, and a central 30 × 50 mm outlined area with corner details. It does not establish the complete assembled enclosure height. The central area is a candidate label location only; usable adhesive area, actual fitted part and label size require confirmation. Do not infer full enclosure dimensions or approved label capacity from this part drawing.
