# Draft reply to René

Subject: ESPGateway Ethernet LTE — label and manual preparation for Intertek

Hi René,

Thanks for flagging this early. We have prepared a first documentation review pack: English and German manual drafts, device-label and packaging text, a quick-start/safety insert draft, and EU/US declaration templates. Unconfirmed information is clearly marked; these are review drafts, not production artwork or conformity claims.

The proposed manual link is:
https://docs.thingpulse.com/guides/espgateway-ethernet-lte/

The existing box identifies the product as ESPGateway Ethernet LTE, carries GTIN-13/EAN 7649998893091 and states “Hardware Made in China”. We use this GTIN as the SKU, without a separate sale SKU; it is not a unit serial number. The box currently shows an FCC logo; please include its use and the complete packaging layout in your review. We plan to use the same product/model identification throughout, with rated input, legal manufacturer/address, serial or batch identification, verified country of origin and the applicable regulatory markings. The device comes in an enclosure with an external 2.4 GHz Wi-Fi antenna, an internal LTE foil antenna and USB-C power. The Wi-Fi module is shown as ESP32-WROVER-IE-N16R8. The selected LTE board is [AND-Global BK-A7670G](https://www.and-global.com/list_23/662.html); the PCB is marked “ESP32 Ethernet Gateway with SIM760x and A7670x support” and “2026/08/30”. We will distinguish this shared-board identification from the fitted LTE assembly in the submission BOM and identify the finished device by its product name and SKU/GTIN. We still need the fitted modem marking, board revision, matching approval documents, production BOM, antenna part numbers/gains, rated input and market-contact details.

The product ships with self-test firmware only. Users write their own firmware to communicate with Wi-Fi/BLE devices via the ESP32 and send data over LTE to a backend, for example BLE temperature/humidity readings to an MQTT broker. Please agree the representative test firmware, simultaneous-radio modes, permitted user-programmable settings and cybersecurity/support scope for this intended use.

Could you ask Intertek to confirm the following in one consolidated review?

1. Which FCC authorization route applies to this host, and can we rely on the specific LTE and Wi-Fi/Bluetooth module grants with our antennas and simultaneous-transmission configuration? What FCC IDs and exact host label/manual wording are required?
2. Who must act as the US SDoC responsible party, and is a separate US agent needed for a certification application? Which details must go on the device, packaging, insert and online manual?
3. What is the EU conformity-assessment route? Our understanding is that RED requires a notified-body number beside CE for Annex IV full quality assurance, not merely because Intertek tests the product or performs Annex III EU-type examination. Please confirm for this project.
4. Please confirm the required safety/radio/EMC/RF exposure and cybersecurity scope, including the RED cybersecurity requirements applicable since August 2025, and the standards/editions to use. We also need to resolve CRA applicability and current reporting obligations for our planned sales.
5. What frequency/power, antenna, separation-distance and country-restriction information must the manual contain? Please provide or approve the exact product-specific statements.
6. Can you approve the proposed printed safety/quick-start information plus online manual, and identify anything that must remain physically on the product or accompany it on paper? Which languages are needed for our target markets?
7. What label dimensions, durability, symbol sizes and placement evidence do you need, and when should we freeze the artwork/manual relative to testing?
8. How many document review rounds are included in the quotation? Please distinguish editorial changes, report/certificate reissue charges, and technical changes that require reassessment or retesting. We would like written confirmation of the change policy before freezing the production configuration.

The product name, SKU/GTIN and manufacturer are now confirmed. Manufacturer: ThingPulse GmbH, c/o Daniel Eichhorn, Bachtelweg 4, 8052 Zurich, Switzerland. We will supply the remaining EU/US market-contact details, input rating, BOM, radio grants, antenna specifications, firmware version, target countries and label-placement drawing together, so you can review a consistent package.

Best,
Dani

---

Attachment checklist (drafts in this folder; nothing sent automatically):

- English/German manual sources or reviewed exports.
- Label and quick-start/safety insert text.
- Unsigned EU DoC and US compliance-information templates.
- Review-pack README with open inputs and release checklist.
- Schematic evidence note and supplied schematic (confirm it matches production).
