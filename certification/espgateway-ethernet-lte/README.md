# ESPGateway Ethernet LTE — Intertek review pack

Revision 0.7 • 12 October 2026 • Owner: ThingPulse • Status: draft, not approved for production

This pack prepares the documentation review; it is not a test report, equipment authorization or signed declaration. The repository previously contained only a heading and image for this product. The user subsequently supplied a three-sheet schematic and confirmed enclosure, external 2.4 GHz Wi-Fi antenna, internal LTE foil antenna and USB-C power. The manufacturer is now confirmed as ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland. No final BOM, module grants, rated input current or test reports were available. Specifications from other ESPGateway models have deliberately not been reused.

## Documents

- [English manual draft](../../docs/guides/espgateway-ethernet-lte.md) and [German manual draft](../../docs/guides/espgateway-ethernet-lte.de.md).
- [Label, packaging and accompanying-information text](label-and-insert.md).
- [EU declaration and US compliance-information templates](declarations.md).
- [Draft reply to René and Intertek questions](reply-to-rene.md).
- [Schematic evidence and remaining engineering questions](hardware-evidence.md).

Internal review documents live outside `docs/` and therefore outside the public MkDocs site. The manual drafts are in the existing page locations and will be included in the next site build; do not deploy them as release manuals until the open items are resolved. No publication or message to René has been performed.

## Answers to the label questions

| Item | Proposed treatment | Evidence / decision required |
| --- | --- | --- |
| Product name and model | Print the product name and one stable model identifier; add serial or batch traceability. Use identical identifiers in manual, test reports and declarations. | Box designation ESPGateway Ethernet LTE and GTIN-13 `7649998893091` are now recorded. User confirms GTIN is also the SKU, with no separate sale SKU. Use product name plus SKU/GTIN throughout; confirm hardware revision and serial/batch scheme. GTIN is not a unit serial. RED Article 10(6). |
| Rated voltage | Reserve label space for input voltage/range, AC/DC and rated current; connector/polarity where applicable. | Engineering supplies measured/design rating and intended supply; Intertek confirms marking under the chosen safety standard. Do not assume USB-C means a particular rating. |
| Manufacturer name/address | Use the legal manufacturer's name/trade name and full postal contact address, preferably on the device. | RED Article 10(7); alternative placement is conditional, not a space-saving default. Confirmed by the user: ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland. |
| US responsible party | For SDoC, supply the US-based responsible party's name, address and telephone or internet contact in the manual or separate compliance sheet. It is not automatically a device-label field. | 47 CFR 2.1077. Intertek must distinguish this role from any US agent required for a certification application. |
| Country of origin | Existing box states `Hardware Made in China`; use China as the documented origin claim and retain supporting manufacturing evidence. | US import marking is a customs requirement, distinct from FCC/CE. Confirm with the importer; a Swiss design/company address does not establish Swiss origin. |
| Notified-body number | Do not add a number just because Intertek performs tests or EU-type examination. | Under RED Article 20(3), the number follows CE when Annex IV full quality assurance is used. Ask Intertek which procedure applies. |
| FCC identification | Determine host certification versus reliance on approved modules. Use assigned identifiers only. | Review every installed transmitter's grant, antenna and integration conditions. A module approval alone does not establish host compliance. |
| Manual URL / QR | Use the existing English URL as the stable entry point, with a language selector and readable URL alongside any QR. | Confirm final online/printed split with Intertek. A URL does not replace all required physical markings or accompanying information. |
| CE, WEEE and other symbols | Provide actual conforming artwork only when applicable and justified; CE also appears on RED packaging. | Review symbol size, legibility, durability, position and applicable waste obligations. No FCC or Intertek/ETL logo should be inferred from testing alone. |

Sources: [RED Articles 10, 19–21 and annexes](https://eur-lex.europa.eu/eli/dir/2014/53/oj/eng), [FCC SDoC information](https://www.ecfr.gov/current/title-47/section-2.1077), [FCC module integration guidance](https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=44637&switch=P), [US country-of-origin marking](https://www.ecfr.gov/current/title-19/chapter-I/part-134/subpart-B/section-134.11), [WEEE marking](https://europa.eu/youreurope/business/product-rules-compliance/recycling-waste-management/weee-label/index_en.htm).

## Required inputs and owners

Items below are open or partially resolved as noted. Suggested owners are assignments for planning, not confirmed commitments.

| Owner | Required input / deliverable | Why needed |
| --- | --- | --- |
| ThingPulse engineering | Final BOM, production PCB revision, enclosure drawing/photos and any regional variants; product name and SKU/GTIN confirmed; schematic rev. 1.0.3 and PCB marking `2026/08/30` received; map these to the production variant | Defines the assessed product |
| ThingPulse engineering | Enclosed product confirmed, with external Wi-Fi/internal LTE antennas and USB-C power; PSU/cable inclusion and battery/PoE status still to confirm | Defines safety, test and manual scope |
| ThingPulse engineering | Voltage/current rating, power connector, environment and mounting limits | Completes label and safety instructions |
| Module suppliers / engineering | ESP32-WROVER-IE-N16R8 shown in schematic; LTE supplier selection now confirmed (see hardware evidence). Resolve shared-design U6 designation in the fitted-variant record; obtain fitted markings, board revision, FCC IDs, grants and OEM integration manuals | Establishes approval conditions and permitted host integration |
| Antenna supplier / engineering | Antenna part numbers, types, gain by band, cable loss and connector; physical locations | Required for RF tests and exposure evaluation |
| Engineering / Intertek | Enabled bands, maximum powers, simultaneous transmission modes, separation distance and use restrictions | Completes the radio table and installation requirements |
| ThingPulse firmware | Self-test-only delivery confirmed; obtain self-test version/coverage, self-test pass/fail indications, flashing/recovery, data behavior and support scope; application firmware and LED meanings are defined by its implementer | Makes the manual usable and defines tested software |
| ThingPulse management | Manufacturer/address confirmed; remaining inputs: evidence supporting the box claim of China hardware origin, target countries and intended launch date | Completes identity and market scope |
| ThingPulse / importer | US SDoC responsible party and certification agent if needed; EU importer/responsible economic operator | Completes market-specific contacts |
| Intertek | Applicable standards with editions/amendments, FCC rule parts and Class A/B determination; EU assessment route | Prevents guessed standards or declarations |
| ThingPulse / Intertek | Final risk assessment, reports, radio exposure evaluation, approved statements and test configuration | Supports release claims |
| ThingPulse | Label dimensions/material/adhesive and placement photo; package/insert proofs | Enables physical artwork review |

For an EU sale by a non-EU manufacturer, resolve the EU economic-operator arrangements independently of the US contact. See [Regulation (EU) 2019/1020, Article 4](https://eur-lex.europa.eu/eli/reg/2019/1020/oj).

## Scope to agree before testing

1. Confirm whether existing radio module approvals can be used for this exact host, antennas and simultaneous-radio configuration. Ask whether host changes, additional certification or RF exposure testing are necessary. Include LTE licensed-service rules as well as Part 15 host emissions.
2. Agree the applicable EU legislation and standards. RED covers radio-equipment safety/health, EMC and spectrum; do not automatically list separate LVD and EMC directives for the radio host. Assess RoHS and other applicable legislation separately. See the [Commission RED overview](https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en).
3. Include cybersecurity in the EU scope now: RED delegated cybersecurity requirements have applied since August 2025 for covered equipment. As an internet-connected gateway, this product needs an explicit applicability assessment, including privacy and any relevant fraud-protection functions. Confirm EN 18031 coverage, restrictions and whether a notified body is needed. See [Decision (EU) 2025/138](https://eur-lex.europa.eu/eli/dec_impl/2025/138/oj).
4. Assess CRA applicability and the manufacturer's incident/vulnerability process. Reporting obligations began on 11 September 2026; main obligations apply from 11 December 2027. These dates do not mean every CRA conformity requirement already applies. See the [Commission CRA overview](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act).
5. Confirm sales jurisdictions and required manual/safety/DoC languages. English and German alone do not cover all EU markets. Switzerland, the UK and Canada require separate scope decisions if targeted.
6. Confirm whether carrier/PTCRB/GCF requirements apply to the intended LTE deployment. These are separate from FCC/CE authorization.
7. Confirm the printed content that must accompany the product. Proposed baseline: essential safety and installation limitations, product/contact identification, regulatory information and simplified EU declaration, plus a readable manual URL. Do not assume an online-only manual is sufficient in every market.

## Release and revision control

Freeze hardware, firmware, antennas, power supply, cables and documentation together. Record the sample serial numbers and firmware hashes used by Intertek. Submit one numbered review pack with label location photos and actual-size artwork. Maintain a change log showing each change, affected documents, technical impact and Intertek disposition.

Ask Intertek to separate editorial corrections from changes that could affect test results: antennas, power, PCB/enclosure, radio settings, firmware behavior and supported operating modes. Retest requirements depend on impact; included review rounds, reissue charges and fees must be confirmed in the quotation. No assumption about free changes is made here.

Before sale/publication:

- [ ] Close every PENDING/OFFEN/bracketed field and validate startup, reset and update instructions on the production sample.
- [ ] Confirm final test scope, completed reports, FCC authorization route/identifiers and EU conformity evidence.
- [ ] Obtain the manufacturer's signed EU DoC and final US compliance information, as applicable.
- [ ] Review production label and packaging at actual size; check adhesion, readability and placement.
- [ ] Verify each QR and readable URL from an unauthenticated device, and verify required language availability.
- [ ] Archive dated manual releases and signed declarations with the corresponding hardware/firmware revisions; retain the EU technical file and declaration for the required ten-year period.
- [ ] Complete market-specific importer, waste/packaging registration and sale-listing requirements as applicable.
- [ ] Record ThingPulse release authorization after Intertek's technical/document review; remove draft notices only then.

## Technical-file index

Maintain controlled copies of product description and intended use; variants/BOM/drawings; design and risk assessment; module grants and antenna data; hardware/firmware version evidence; standards/applicability matrix; safety, EMC, radio, RF exposure and cybersecurity evidence; RoHS evidence; label/location/package/insert proofs; manuals and translations; declarations; any notified-body certificate; production conformity controls; and change history. Reports and signed declarations remain missing from this draft pack.

## Confirmed intended use and firmware scope

The product ships only with self-test firmware. Users write and install their own application firmware to communicate with Wi-Fi/BLE devices via ESP32 and upload data over LTE to a backend. Example: read BLE temperature/humidity and publish to an MQTT broker. This example is not a supplied application.

Ask Intertek to agree representative test firmware and worst-case operating modes for this intended use, including simultaneous Wi-Fi/BLE and LTE activity as applicable. Record shipped self-test, laboratory firmware and user-programmable radio settings separately. Resolve firmware constraints and cybersecurity/support scope explicitly; do not assume that describing the device as programmable removes any assessment obligation. The final manual needs programming/recovery instructions, not invented factory web-configuration steps.
