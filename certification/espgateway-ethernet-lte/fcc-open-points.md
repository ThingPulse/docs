# FCC SDoC — open questions

27 November 2026. Working checklist; no declaration issued.

## Confirmed inputs

ESPGateway Ethernet LTE; SKU/GTIN 7649998893091. ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland. Intertek sample hardware marking 2026/08/30. USB-C 5 V DC / 2 A; no supplied adapter/cable, battery or PoE. Enclosed product with Ethernet, ESP32-WROVER-IE and A7670G LTE assembly. Supplied firmware is web-triggered self-test; users develop application firmware. Both antennas sourced by René. No device serial/batch numbers assigned.

## Questions to close, in order

| Question | Suggested answer/action | Owner |
| --- | --- | --- |
| Which exact tests and classification? | Propose Part 15 Subpart B Class B; Intertek confirms rule parts and measurement procedure. | Intertek |
| Can the current self-test support measurement? | Supply version/image, startup steps, tested interfaces and duration. Ask whether it needs repetition or sustained traffic; do not build new firmware before confirming. | Daniel / Intertek |
| Which PSU, USB/Ethernet cables and peripherals? | Document actual lab setup despite PSU/cable not being supplied commercially; agree representative configuration and any required restrictions. | Daniel / René / Intertek |
| Does production match the sample? | Review November LTE mounting-hole change against sample 2026/08/30; ask whether updated sample is needed. | Daniel / René / Intertek |
| Is the application accurate? | Obtain submitted form and verify applicant, manufacturer and assembly-site roles; do not assume enclosure supplier is gateway manufacturer. | René |
| What artwork/placement is required? | Submit device and box proofs; Intertek has not answered which surface needs which text. Confirm actual usable label area. | Daniel / Intertek |
| Who is US responsible party? | Response Technologies is a candidate only. November correspondence shows willingness to discuss, not acceptance. Confirm eligible entity, scope, US address and telephone/internet contact. | Daniel / proposed party |
| Which final statements and records? | Finalize compliance sheet, Class A/B notice and applicable Part 15/accessory notices; obtain report and retain controlled supporting records. | Intertek / responsible party |

## Separate FCC boundary confirmation

Ask Intertek whether the exact fitted modules and antennas can rely on their existing grants, and who reviews integration conditions. Photographed IDs: 2AC7Z-ESP32WROVERE and 2AJYU-8BAE003. René obtains supplier documents if needed. This is not a new radio-certification project in the SDoC checklist, but SDoC alone cannot resolve it. Do not guess antenna gain, RF separation or module-label requirements.

## Removed as SDoC blockers

EU importer, EU declarations, CE/WEEE markings, RED/RoHS/CRA assessments, translations, carrier approvals, generic safety qualification, finished-device temperature qualification, vulnerability/support policies and full application-development tutorials. Retain operating instructions and any restrictions actually relevant to the emissions test/compliance.

Sources: [René's scope](https://mail.google.com/mail/u/0/#all/1a13382c0f694f9f), [FCC rules](https://www.govinfo.gov/content/pkg/CFR-2025-title47-vol1/xhtml/CFR-2025-title47-vol1-part2-subpartJ.html).
