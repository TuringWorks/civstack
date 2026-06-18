# Industry & Sector Coverage Cross-Walk

A consolidated map from the major industry, sector, and software taxonomies onto CivStack's
**23 operating systems** — used to validate coverage and surface gaps. Sources: U.S. BLS
Industries at a Glance (NAICS), ILO Industries & Sectors, Wikipedia *Outline of Industry*,
Simplicable *Sectors of the Economy*, G2 software categories, and VerticalIQ industry groups.

**Headline:** every sector in every one of these taxonomies maps onto one or more of the 23
operating systems — coverage is complete at the domain level. A short list of **sub-industry
role families** is covered only implicitly and is flagged at the end as candidate additions.

The 23 operating systems: `01` Governance & Law · `02` Public Finance · `03` Defense &
Foreign Affairs · `04` Public Safety & Emergency · `05` Food & Agriculture · `06` Water &
Sanitation · `07` Energy & Grid · `08` Mining/Materials/Chemicals · `09` Manufacturing ·
`10` Shelter & Built Environment · `11` Transportation & Logistics · `12` Communications &
Software · `13` Health & Public Health · `14` Education & Human Capital · `15` Science &
Innovation · `16` Finance & Markets · `17` Commerce & Hospitality · `18` Media & Civic Life ·
`19` Environment & Waste · `20` Labor & Workforce · `21` Household & Care · `22` Resilience &
Continuity · `23` Identity, Civil Registration & Digital Public Infrastructure.

---

## 1. U.S. BLS — Industries at a Glance (NAICS)

### Goods-producing

| NAICS industry | → OS |
|---|---|
| Agriculture, Forestry, Fishing & Hunting (11): Crop Production (111), Animal Production (112), Forestry & Logging (113), Fishing/Hunting/Trapping (114), Support Activities for Ag & Forestry (115) | 05 (+ 08 timber→wood, 19 forestry/conservation) |
| Mining, Quarrying, Oil & Gas (21): Oil & Gas Extraction (211), Mining except Oil & Gas (212), Support Activities for Mining (213) | 08 (+ 07 oil & gas) |
| Utilities (22) | 07 (power/gas) + 06 (water) |
| Construction (23): Buildings (236), Heavy & Civil Engineering (237), Specialty Trade Contractors (238) | 10 |
| Manufacturing (31–33): Food (311), Beverage & Tobacco (312), Textile Mills (313), Textile Product Mills (314), Apparel (315), Leather (316), Wood Product (321), Paper (322), Printing (323), Petroleum & Coal (324), Chemical (325), Plastics & Rubber (326), Nonmetallic Mineral (327), Primary Metal (331), Fabricated Metal (332), Machinery (333), Computer & Electronic (334), Electrical Equipment (335), Transportation Equipment (336), Furniture (337), Miscellaneous (339) | 09 (+ 05 food mfg, 08 chemicals/metals/paper/plastics, 11 transport equip, 12 computer/electronic) |

### Trade, Transportation & Utilities

| NAICS industry | → OS |
|---|---|
| Wholesale Trade (42): Durable (423), Nondurable (424), Electronic Markets & Agents/Brokers (425) | 17 (+ 11 distribution) — *thin: see gaps* |
| Retail Trade (44–45): Motor Vehicle & Parts (441), Furniture (442), Electronics & Appliance (443), Building Material & Garden (444), Food & Beverage (445), Health & Personal Care (446), Gasoline (447), Clothing (448), Sporting Goods/Hobby/Book/Music (451), General Merchandise (452), Misc (453), Nonstore (454) | 17 (+ 13 pharmacy, 07 fuel, 05 food retail) |
| Transportation & Warehousing (48–49): Air (481), Rail (482), Water (483), Truck (484), Transit & Ground Passenger (485), Pipeline (486), Scenic & Sightseeing (487), Support Activities (488), Postal (491), Couriers & Messengers (492), Warehousing & Storage (493) | 11 |
| Utilities (22) | 07 + 06 |

### Information

| NAICS industry | → OS |
|---|---|
| Information (51): Publishing (511), Motion Picture & Sound (512), Broadcasting (515), Internet Publishing (516), Telecommunications (517), Data Processing & Hosting (518), Other Information (519) | 12 (+ 18 film/broadcast/publishing) |

### Financial Activities

| NAICS industry | → OS |
|---|---|
| Finance & Insurance (52): Monetary Authorities–Central Bank (521), Credit Intermediation (522), Securities & Commodity Contracts (523), Insurance Carriers (524), Funds/Trusts (525) | 16 (Central Bank also 02) |
| Real Estate & Rental & Leasing (53): Real Estate (531), Rental & Leasing Services (532), Lessors of Nonfinancial Intangible Assets (533) | 10 + 16 — *thin: see gaps* |

### Professional & Business Services

| NAICS industry | → OS |
|---|---|
| Professional, Scientific & Technical Services (54) | 12 (IT) + 15 (R&D) + 01 (legal) + 17 (consulting) |
| Management of Companies & Enterprises (55) | 20 (+ 16 holding cos) — *thin: see gaps* |
| Administrative & Support & Waste Management (56): Admin & Support (561), Waste Management & Remediation (562) | 20 (admin/staffing) + 19 (waste) + 04 (security svcs) |

### Education & Health Services

| NAICS industry | → OS |
|---|---|
| Educational Services (61) | 14 |
| Health Care & Social Assistance (62): Ambulatory (621), Hospitals (622), Nursing & Residential Care (623), Social Assistance (624) | 13 + 21 (social assistance, nursing) |

### Leisure & Hospitality

| NAICS industry | → OS |
|---|---|
| Arts, Entertainment & Recreation (71): Performing Arts & Spectator Sports (711), Museums & Historical Sites (712), Amusement/Gambling/Recreation (713) | 18 (+ 14 museums) |
| Accommodation & Food Services (72): Accommodation (721), Food Services & Drinking Places (722) | 17 |

### Other Services (except Public Administration)

| NAICS industry | → OS |
|---|---|
| Repair & Maintenance (811) | 17 + Maintainer archetype — *thin: see gaps* |
| Personal & Laundry Services (812) — incl. funeral/death care, salons, pet care | 21 + 17 — **gap: death care** |
| Religious, Grantmaking, Civic, Professional & Similar Orgs (813) | 18 + 21 |
| Private Households (814) | 21 |

### Public Administration (NAICS 92 — *not* in BLS IAG, which is private-sector)

| Government | → OS |
|---|---|
| Legislatures, courts, public admin, public finance, defense, public safety, civil registration | 01, 02, 03, 04, 23 — **CivStack covers the state; BLS IAG omits it** |

---

## 2. ILO — Industries & Sectors

| ILO sector | → OS |
|---|---|
| Agriculture, aquaculture, plantations, rural | 05 |
| Food, drink & tobacco | 05 (+ 09 mfg) |
| Forestry, wood, pulp & paper | 05 + 08 + 19 |
| Mining | 08 |
| Oil & gas | 07 |
| Energy generation | 07 |
| Basic metals | 08 |
| Chemicals & pharmaceuticals | 08 (+ 13 pharma, 15 R&D) |
| Electronics, machinery & electrical equipment | 09 (+ 12) |
| Transport equipment | 09 + 11 |
| Textiles, apparel, leather | 09 |
| Commerce | 17 |
| Financial & professional services | 16 + 12 + 15 + 20 |
| Tourism, hotels & food & beverage | 17 |
| Media, culture, sports & entertainment | 18 |
| Postal & courier services | 11 |
| Telecommunications & IT services | 12 |
| Personal, administrative & support services | 20 + 21 + 17 — **incl. personal svcs (death care, salons)** |
| Construction | 10 |
| Building materials | 08 + 10 |
| Education & training | 14 |
| Health & social services | 13 + 21 |
| Public service | 01–04, 23 |
| Utilities (gas, electricity, water, waste) | 07 + 06 + 19 |
| Shipping, fishing & inland waterways | 11 + 05 |
| Transport (aviation, rail, road), ports & logistics | 11 |

ILO adds **maritime/shipping** as a first-class lens — CivStack covers it via 11 (transport) + the autonomous-vessel/USV machines; worth noting as a named cluster.

---

## 3. Wikipedia — Outline of Industry

Sector model: **Primary** (raw materials) → **Secondary** (manufacturing & construction) →
**Tertiary** (services) → **Quaternary** (information/knowledge) → **Quinary** (human/non-profit
services). CivStack spans all five (05/08 primary; 09/10 secondary; 17/11/16 tertiary; 12/15
quaternary; 01–04/13/14/21/23 quinary).

| Wikipedia industry | → OS |
|---|---|
| Aerospace | 09 + 03 + 15 (mission: quantum-and-space) |
| Automotive | 09 + 11 |
| Chemical | 08 |
| Construction | 10 |
| Defense | 03 |
| Electric power / Energy | 07 |
| Electronics | 09 + 12 |
| Food | 05 |
| Industrial robot | 09 + embodied-AI stack |
| Meat / Mining / Oil & gas / Petroleum / Pulp & paper / Steel | 05 / 08 / 07 / 08 |
| Shipbuilding | 09 + 11 |
| Textile | 09 |
| Water | 06 |
| Broadcasting / Creative / Cultural / Entertainment / Mass media | 18 |
| Education | 14 |
| Financial services | 16 |
| Healthcare | 13 |
| Hospitality / Leisure | 17 |
| Information / Technology / Telecommunications | 12 |
| Professional services | 12 + 15 + 01 + 17 |
| Real estate | 10 + 16 — *thin* |
| Retail | 17 |
| Sport | 18 |
| Transport | 11 |

---

## 4. Simplicable — Sectors of the Economy

| Simplicable sector | → OS |
|---|---|
| Agriculture | 05 |
| Arts & Entertainment | 18 |
| Business Services | 20 + 12 + 17 |
| Construction | 10 |
| Consumer Discretionary / Consumer Staples / Consumer Services | 17 (+ 05 staples) |
| Education | 14 |
| Energy | 07 |
| Financials | 16 |
| Health Care | 13 |
| Hospitality & Tourism | 17 |
| Industrials | 09 + 11 |
| Information Technology | 12 |
| Manufacturing | 09 |
| Materials | 08 |
| Media | 18 |
| Public Sector | 01–04, 23 |
| Real Estate | 10 + 16 — *thin* |
| Retail | 17 |
| Science & Technology | 15 + 12 |
| Telecommunications | 12 |
| Transportation | 11 |
| Utilities | 07 + 06 |

Full match — all 24 Simplicable sectors map cleanly.

---

## 5. G2 — software categories (the tooling/AI-personnel layer of each OS)

Software categories aren't economic sectors; they're the **digital tools and AI personnel**
that automate each sector's work. Mapped to the OS whose work they serve:

| G2 top-level category | Serves OS |
|---|---|
| CRM, Sales, Digital Advertising, Marketing, Commerce / E-Commerce | 17 (+ 12 build) |
| Customer Service | 17 |
| ERP, Accounting, Finance, Billing | 16 + 02 + 09 |
| HR, Talent / Recruiting, Workforce Management | 20 |
| Supply Chain & Logistics, Procurement | 11 + 02 + 17 |
| Analytics & BI, Data, AI/ML platforms | 12 + 15 (cross-cutting via `capability-optimization`) |
| Collaboration & Productivity, Office, Content Management, Design, Project Management | 12 (+ 20) |
| Development (DevOps, IT Infrastructure, IT Management, Hosting) | 12 |
| Security, Data Privacy, Governance Risk & Compliance (GRC) | 12 (cyber) + 01 (compliance) + 23 (privacy/identity) |
| Greentech / ESG | 19 |
| Vertical Industry software (Healthcare IT, Fintech, Legal, GovTech, EdTech, AgTech, ConTech, PropTech, Retail/Restaurant) | 13 / 16 / 01 / 23 / 14 / 05 / 10 / 17 respectively |

This is the cleanest evidence that the **AI-personnel role skills** in each OS are the right
abstraction: every major software category corresponds to an AI-personnel role (or cluster)
under one of the operating systems.

---

## 6. VerticalIQ — industry groups (research-vertical view)

VerticalIQ groups ~500+ industries under roughly these majors, all covered:
Agriculture (05), Construction (10), Education (14), Finance & Insurance (16), Healthcare (13),
Manufacturing (09), Media & Internet (18/12), Professional Services (12/15/01/20), Real Estate
(10/16 — *thin*), Retail (17), Technology (12), Transportation & Warehousing (11), Wholesale &
Distribution (17/11 — *thin*), Utilities & Energy (07/06/19), Hospitality (17), Personal Services
(21/17 — *death care thin*), Nonprofit & Government (18/21/01–04/23).

---

## 7. Consolidated gap list (covered, but no dedicated role skills)

Every taxonomy lands inside the 23 OSs. These few sub-industries are covered only *implicitly*
and are the candidate additions, in priority order:

1. **Death / funeral / end-of-life services** (NAICS 812; ILO personal services) — funeral
   director, mortuary services, bereavement coordinator, coroner/medical examiner liaison; AI:
   death-registration assistant (ties to **OS 23**). *The one true net-new gap across every source.*
2. **Real estate & property** (NAICS 53; every taxonomy) — real-estate broker, property manager,
   leasing agent; AI: listing/valuation (AVM) agent, lease-abstraction agent. → **OS 10** (+16).
3. **Wholesale trade & distribution** (NAICS 42) — distributor/wholesale buyer, distribution-ops
   manager; AI: assortment/replenishment agent, broker-matching agent. → **OS 17** (+11).
4. **Rental & leasing services** (NAICS 532) — equipment/vehicle rental ops; AI: fleet-utilization
   & pricing agent. → **OS 17**.
5. **Repair & maintenance services** (NAICS 811) — auto/equipment repair as a consumer industry
   (distinct from the internal Maintainer archetype). → **OS 17**.
6. **Personal & consumer services** (NAICS 812) beyond death care — salon/personal care, pet care,
   laundry/dry-cleaning. → **OS 21/17**.
7. **Forestry & logging** as primary production (NAICS 113) — explicit forester/logging roles. → **OS 05** (+08/19).
8. **Maritime / shipping cluster** (ILO) — already covered by 11 + autonomous vessels, but not named
   as a cluster; optional explicit ports/maritime roles.
9. **Corporate management / holding companies** (NAICS 55) — corporate-development / portfolio
   management roles. → **OS 20** (+16).

None require a new operating system. They are sub-industry **role families** inside existing OSs.

## Recommendation — **implemented**

The gap roles were added in one pass (library now 373 skills):

- **OS 21** — funeral arrangement assistant, death registration & estate-handoff assistant,
  bereavement support coordinator, personal-services booking assistant.
- **OS 10** — property listing & valuation (AVM) agent, lease abstraction & management agent,
  tenant screening & onboarding assistant (fair-housing-bounded).
- **OS 17** — distribution & allocation agent, wholesale assortment & replenishment agent,
  equipment-rental fleet & pricing agent, repair-service scheduling & estimate agent.
- **OS 05** — forestry & logging operations agent. **OS 20** — corporate development & portfolio agent.

With these, CivStack is a complete superset of all six taxonomies at the role level. Remaining
optional refinements: an explicit maritime/ports role cluster (already covered by 11 + autonomous
vessels) and deeper personal-services sub-roles.
