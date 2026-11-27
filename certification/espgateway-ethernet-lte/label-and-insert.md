# Label and accompanying information — copy draft

Revision 0.7 • 8 November 2026 • NOT FOR PRINTING

Square brackets are unresolved fields or artwork instructions. This is a content/layout specification, not dimensioned production artwork. Final label dimensions, enclosure area and material are unknown.

## Existing box label

User-supplied artwork: `Label-ESPGateway-Ethernet-LTE-label.png`, supplied from the ThingPulse project artwork folder on 12 October 2026. The source artwork was inspected as attached and has not been modified.

| Visible item | Recorded text / finding |
| --- | --- |
| Brand and product | THINGPULSE; ESPGateway Ethernet LTE |
| Getting-started URL | `https://docs.thingpulse.com/guides/espgateway-ethernet-lte/` — matches the manual route |
| Contents | `1x ESPGateway Ethernet`; `1x A7670G (Global) LTE Module` |
| Origin wording | `Hardware Made in China`; `swiss made software` |
| Barcode digits | `7649998893091` (printed as `7 649998 893091`) |
| Regulatory graphic | FCC logo visible; no FCC ID or operating statement visible in this artwork |

The printed number has a valid EAN-13 check digit: the weighted sum of the first twelve digits is 169, giving check digit 1. Record it as the product GTIN-13/EAN, not a unique device serial number. This arithmetic check does not verify GS1 assignment, barcode scan quality or ownership. GS1 registry verification remains open.

This artwork confirms the existing product designation and stated China hardware origin. Retain manufacturing-origin evidence for the final label review. Do not infer the legal manufacturer address or hardware origin from the Swiss software claim or barcode prefix.

For Intertek review, the shown artwork does not include rated input, full legal manufacturer/address, US compliance information. These may be elsewhere on the product/packaging; review all label surfaces and accompanying documents before deciding placement. The user confirms that GTIN `7649998893091` is the SKU. Use product designation ESPGateway Ethernet LTE and that SKU consistently.

The FCC logo is not an FCC ID or proof of authorization. Its voluntary use under SDoC does not replace required compliance information; retain it in production artwork only when supported by the applicable authorization. See [47 CFR 2.1074](https://www.ecfr.gov/current/title-47/section-2.1074). Confirm its treatment with Intertek together with the host/module labeling route.

## Existing PCB marking

The supplied image shows `THINGPULSE`, `2026/08/30`, and `ESP32 Ethernet Gateway with SIM760x and A7670x support`. Preserve this wording in the hardware record. The user confirmed `2026/08/30` as the revision marking of the unit supplied to Intertek on 8 November 2026. It is not a unit serial number or a confirmed manufacturing date. The box product designation is known and GTIN `7649998893091` is the confirmed SKU; no separate SKU is used.

## Device label: base content

```text
ThingPulse
ESPGateway Ethernet LTE
SKU / GTIN: 7649998893091
HW: 2026/08/30
Input (USB-C): 5 V DC, 2 A
[POLARITY / CONNECTOR IDENTIFICATION, IF APPLICABLE]
Manufacturer: ThingPulse GmbH
c/o Daniel Eichhorn
Bachtelweg 4
8052 Zurich, Switzerland
Made in China [EXISTING BOX CLAIM; RETAIN ORIGIN EVIDENCE]
Manual: https://docs.thingpulse.com/guides/espgateway-ethernet-lte/
[OPTIONAL QR ENCODING THE SAME URL]
[FCC IDENTIFICATION AND OPERATING STATEMENT AS DETERMINED BELOW]
```


## FCC identification: select the supported route

**Route A — approved modules used within their conditions:** reserve a separate `Contains FCC ID: [ACTUAL MODULE FCC ID]` line for each module requiring external host identification. Confirm wording against each grant/OEM manual, including the LTE module. A module's FCC ID is not the host's own FCC ID.

**Route B — host certification:** use `FCC ID: [ASSIGNED HOST FCC ID]` and any additional wording required by the actual grant. Do not invent a ThingPulse FCC ID or assume that Route A is sufficient.

Intertek must document the final route and applicable host testing. Reference: [FCC KDB 996369 module guidance](https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=44637&switch=P).

For applicable Part 15 devices, reserve the following statement (activate only after compliance is established):

> This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Under [47 CFR 15.19(a)(5)](https://www.ecfr.gov/current/title-47/section-15.19), the small-device exception has specific conditions; when applicable, the statement goes in the manual **and** on packaging or a removable device label. A QR link alone is not this exception. Ask Intertek to approve the actual placement and font size.

## Accompanying US information

Use declarations.md for the US compliance sheet. Supply the English operating manual and exact FCC notices approved for the tested configuration. Prepare both device and box proofs for review; placement is still unconfirmed. An online manual link is requested by René; confirm the printed/electronic delivery arrangement with Intertek.

## Confirmed box contents — 8 November 2026

Enclosure, gateway PCB, LTE module, LTE antenna and Wi-Fi antenna. No USB cable or power adapter is included. Update the packaging contents artwork accordingly. USB-C is the only power source; no battery or PoE support. The user specified the input rating as 5 V DC, 2 A on 8 November 2026. Adapter safety characteristics and cable limits remain open.

## Module identifiers transcribed from photographs — 8 November 2026

Candidate host-label text for Intertek review, the user confirms that the photographed modules and antennas match the Intertek sample. Final production-variant coverage and grant/OEM integration conditions remain to be checked:

```text
Contains FCC ID: 2AC7Z-ESP32WROVERE
Contains FCC ID: 2AJYU-8BAE003
```

These are the photographed module identifiers, not an assigned host FCC ID. Transcription alone does not establish the authorization route or final required label wording.
