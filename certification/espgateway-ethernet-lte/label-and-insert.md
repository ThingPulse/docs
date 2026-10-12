# Label and accompanying information — copy draft

Revision 0.6 • 12 October 2026 • NOT FOR PRINTING

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

For Intertek review, the shown artwork does not include rated input, full legal manufacturer/address, CE/WEEE symbols, individual serial/batch identification or market-contact information. These may be elsewhere on the product/packaging; review all label surfaces and accompanying documents before deciding placement. The user confirms that GTIN `7649998893091` is the SKU. Use product designation ESPGateway Ethernet LTE and that SKU consistently.

The FCC logo is not an FCC ID or proof of authorization. Its voluntary use under SDoC does not replace required compliance information; retain it in production artwork only when supported by the applicable authorization. See [47 CFR 2.1074](https://www.ecfr.gov/current/title-47/section-2.1074). Confirm its treatment with Intertek together with the host/module labeling route.

## Existing PCB marking

The supplied image shows `THINGPULSE`, `2026/08/30`, and `ESP32 Ethernet Gateway with SIM760x and A7670x support`. Preserve this wording in the hardware record. Confirm whether the date is intended as a revision identifier; do not substitute it for a serial number or manufacture date without confirmation. The box product designation is known and GTIN `7649998893091` is the confirmed SKU; no separate SKU is used.

## Device label: base content

```text
ThingPulse
ESPGateway Ethernet LTE
SKU / GTIN: 7649998893091
HW: [REVISION]
Input (USB-C): [VOLTAGE/RANGE] [DC/AC SYMBOL] [RATED CURRENT]
[POLARITY / CONNECTOR IDENTIFICATION, IF APPLICABLE]
S/N or batch: [IDENTIFIER]
Manufacturer: ThingPulse GmbH
c/o Daniel Eichhorn
Bachtelweg 4
8052 Zurich, Switzerland
Made in China [EXISTING BOX CLAIM; RETAIN ORIGIN EVIDENCE]
Manual: https://docs.thingpulse.com/guides/espgateway-ethernet-lte/
[OPTIONAL QR ENCODING THE SAME URL]
[CE ARTWORK WHEN CONFORMITY IS ESTABLISHED]
[WEEE ARTWORK IF APPLICABLE]
[FCC IDENTIFICATION AND OPERATING STATEMENT AS DETERMINED BELOW]
```

Prefer full contact details on the device. Document any permitted alternate placement with Intertek. Determine whether other locality names on the label require country-of-origin wording in proximity and comparable size under [19 CFR 134.46](https://www.ecfr.gov/current/title-19/section-134.46).

## FCC identification: select the supported route

**Route A — approved modules used within their conditions:** reserve a separate `Contains FCC ID: [ACTUAL MODULE FCC ID]` line for each module requiring external host identification. Confirm wording against each grant/OEM manual, including the LTE module. A module's FCC ID is not the host's own FCC ID.

**Route B — host certification:** use `FCC ID: [ASSIGNED HOST FCC ID]` and any additional wording required by the actual grant. Do not invent a ThingPulse FCC ID or assume that Route A is sufficient.

Intertek must document the final route and applicable host testing. Reference: [FCC KDB 996369 module guidance](https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=44637&switch=P).

For applicable Part 15 devices, reserve the following statement (activate only after compliance is established):

> This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Under [47 CFR 15.19(a)(5)](https://www.ecfr.gov/current/title-47/section-15.19), the small-device exception has specific conditions; when applicable, the statement goes in the manual **and** on packaging or a removable device label. A QR link alone is not this exception. Ask Intertek to approve the actual placement and font size.

## CE and notified-body number

Use official CE artwork, maintaining its proportions and legibility, on device/data plate and packaging as required. Plan for at least 5 mm height unless an applicable exception is justified. Add a notified-body number only if the RED Annex IV procedure applies, under the body's instructions; Annex III EU-type examination alone does not trigger a number beside CE. See [RED Articles 19–20](https://eur-lex.europa.eu/eli/dir/2014/53/oj/eng).

Do not add an Intertek/ETL mark without separate authorization. Do not use a decorative FCC logo as a substitute for required identification and statements.

## Packaging proof checklist

Include product/model, manufacturer/contact, verified origin, CE and applicable traceability/market-contact information. Retain product GTIN-13 `7649998893091`; keep unit serial/batch identification separate. Resolve WEEE marking, any radio restriction pictogram/text and importer information. Match the actual contents and accessory part numbers. Add the readable manual URL and optional QR. Include the Part 15 statement here if using the permitted small-device placement route above.

The manufacturer/importer should review destination-market obligations and approve the printed languages. See [EU compliance responsibilities](https://europa.eu/youreurope/business/product-rules-compliance/general-product-compliance/index_en.htm) and [WEEE label guidance](https://europa.eu/youreurope/business/product-rules-compliance/recycling-waste-management/weee-label/index_en.htm).

## In-box quick-start and safety insert — proposed content

```text
ESPGateway Ethernet LTE — SKU / GTIN 7649998893091
Quick start and safety • Revision [REVISION / DATE]

Read before connecting power. Keep these instructions.
Ships with self-test firmware only. Write and install your own
application firmware for Wi-Fi/BLE-to-LTE backend communication.
Use only [POWER SUPPLY REQUIREMENTS] and [APPROVED ANTENNAS].
Use within [ENVIRONMENT LIMITS]. Maintain [VERIFIED RF SEPARATION]
and [MOUNTING / VENTILATION CLEARANCES].

1. With power disconnected, insert [SIM TYPE / ORIENTATION].
2. Attach the external 2.4 GHz Wi-Fi antenna [PART NUMBER]
   to [IDENTIFIED CONNECTOR]. The LTE foil antenna is internal.
3. Connect [ETHERNET / CABLE REQUIREMENTS].
4. Connect USB-C power [REQUIRED SUPPLY RATING].
   Application LED meanings are defined by the firmware implementer.
5. Follow [SELF-TEST PROCEDURE AND PASS/FAIL INDICATIONS].
6. Develop and install your application using [PROGRAMMING GUIDE].
7. Configure APN, backend and credentials in your application.

Disconnect power if damaged, smoking or unusually hot; contact support.
Keep dry. Observe local restrictions on radio use.
[PRODUCT-SPECIFIC SAFETY / RF WARNINGS FROM FINAL ASSESSMENT]

Manual, updates and support:
https://docs.thingpulse.com/guides/espgateway-ethernet-lte/
Manufacturer: ThingPulse GmbH
c/o Daniel Eichhorn
Bachtelweg 4
8052 Zurich, Switzerland
Support: https://docs.thingpulse.com/support/
[EU IMPORTER / ECONOMIC OPERATOR DETAILS, IF APPLICABLE]
[US COMPLIANCE INFORMATION, IF APPLICABLE]
[SIMPLIFIED EU DECLARATION AND FULL DoC URL, AFTER SIGNATURE]
[APPLICABLE FCC STATEMENTS / RESTRICTIONS]
```

Resolve the actual printed/online split with Intertek; enlarge the insert if necessary. Translate the approved text for each destination market. This draft is not ready to print.
