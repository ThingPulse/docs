# Declaration and compliance-information templates

Revision 0.3 • 12 October 2026 • UNSIGNED DRAFTS — NOT EVIDENCE OF CONFORMITY

Do not distribute these templates as compliance statements. Complete them from the final technical file and assessment outcome; remove non-applicable clauses and secure the required approval/signature before release.

## EU declaration of conformity — Annex VI working template

1. **Radio equipment:** ESPGateway Ethernet LTE, SKU/GTIN 7649998893091, hardware [REVISION], [BATCH/SERIAL IDENTIFICATION OR APPLICABLE RANGE]. Declaration reference [REFERENCE].
2. **Manufacturer:** ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland. Authorised representative, if applicable: [NAME, ADDRESS, MANDATE].
3. This declaration of conformity is issued under the sole responsibility of the manufacturer.
4. **Object of the declaration:** [UNAMBIGUOUS PRODUCT DESCRIPTION, VARIANTS, IDENTIFICATION AND COLOUR IMAGE IF NEEDED; FIRMWARE VERSION/CONFIGURATION WHERE RELEVANT].
5. The object of the declaration described above is in conformity with the relevant Union harmonisation legislation: [CONFIRM 2014/53/EU; ADD 2011/65/EU AS AMENDED AND OTHER APPLICABLE LEGISLATION ONLY AFTER REVIEW].
6. **References to relevant harmonised standards or other technical specifications used:** [FULL STANDARD NUMBERS, DATED EDITIONS/AMENDMENTS; IDENTIFY WHAT WAS APPLIED AND ANY LIMITATIONS]. Do not populate this from generic ESP32 examples.
7. **Notified body, where applicable:** [NAME AND NUMBER] performed [INTERVENTION / ASSESSMENT] and issued [EU-TYPE EXAMINATION CERTIFICATE / REFERENCE]. Omit if not applicable. A body named here does not automatically mean its number accompanies CE on the device.
8. **Accessories/components/software enabling intended operation:** [APPROVED ANTENNAS, POWER SUPPLIES, CABLES, FIRMWARE AND OTHER RELEVANT ITEMS].

Additional information: [RELEVANT CONDITIONS / VARIANTS].

Signed for and on behalf of: ThingPulse GmbH

Place and date of issue: [PLACE, DATE]

Name, function and signature: [AUTHORISED SIGNATORY — UNSIGNED]

Source: [RED Annex VI](https://eur-lex.europa.eu/eli/dir/2014/53/oj/eng). The manufacturer's declaration is supported by the conformity assessment and technical documentation; a laboratory report does not itself replace it. See [EU declaration guidance](https://europa.eu/youreurope/business/product-rules-compliance/general-product-compliance/signing-declaration-conformity/index_en.htm).

## Simplified EU declaration — only after the full declaration is signed

> Hereby, ThingPulse GmbH declares that the radio equipment type [designation of type of radio equipment] is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [working URL of full signed declaration].

German working text:

> Hiermit erklärt ThingPulse GmbH, dass der Funkanlagentyp [Bezeichnung] der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [funktionierende URL zur vollständigen unterzeichneten Erklärung].

Source: [RED Annex VII](https://eur-lex.europa.eu/eli/dir/2014/53/oj/eng). Confirm the official wording in each required destination language. Choose a stable download URL when the signed document exists; no declaration download is currently published by this pack.

## US Supplier's Declaration of Conformity information — if this route applies

```text
Supplier's Declaration of Conformity — compliance information
Product: ESPGateway Ethernet LTE
SKU / GTIN: 7649998893091
Responsible party in the United States: [LEGAL NAME]
US address: [FULL POSTAL ADDRESS]
Telephone or internet contact: [CONTACT]
[APPLICABLE FCC COMPLIANCE STATEMENT]
[MODULE IDENTIFICATION / SUPPORTING INFORMATION IF REQUIRED BY 2.1077(b)]
```

Use the applicable operating statement from `label-and-insert.md`. The responsible party must be located in the United States. Include this information in the manual or a separate sheet; electronic-only delivery is conditional on reasonable user access. See [47 CFR 2.1077](https://www.ecfr.gov/current/title-47/section-2.1077). Confirm whether the special assembled-modular-components provisions actually apply; do not assume a host testing exemption.

## FCC manual statement register

| Manual item | Draft / action before release |
| --- | --- |
| Part 15 operating conditions | Use the applicable statement in `label-and-insert.md`. |
| Changes/modifications notice | Proposed: “Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.” Verify against the final authorization. |
| Digital-device interference notice | Insert the complete applicable Class A or Class B notice after Intertek confirms classification. For Class B include the interference explanation and corrective measures prescribed by 15.105(b); do not claim testing has occurred before it has. |
| RF exposure | Insert approved text based on host evaluation and grants: exact separation, antenna conditions, installation restrictions and simultaneous-radio conditions. Do not default to 20 cm. |
| Module-specific text | Carry over each applicable OEM integration/manual requirement and licensed LTE service condition. |
| Special cables/accessories | Identify any accessories necessary to maintain compliance and ensure availability with the product as required. |

Sources: [47 CFR 15.21](https://www.ecfr.gov/current/title-47/section-15.21), [47 CFR 15.105](https://www.ecfr.gov/current/title-47/section-15.105), [47 CFR 15.27](https://www.ecfr.gov/current/title-47/section-15.27), [FCC module guidance](https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=44637&switch=P).
