# DeliverIQ — Delivery, Returns & Logistics Profitability Intelligence

An Excel-supported, Power BI-style HTML analytics project by **Sanjiban Das**, designed around an Indian footwear and lifestyle brand.

**Synthetic case study:** all 20,000 orders, courier identities and business results are fictional. This is an HTML dashboard with an Excel workbook, not a Power BI `.pbix` file. No SQL or database is required.

![Executive dashboard](screenshots/01_Executive.jpg)

**Reporting period: FY 2026-27 · FYTD 1 April–16 November 2026.** November and Q3 are partial. See [Indian FYTD definitions](docs/INDIAN_FYTD.md).

## Launch

1. Download and extract the complete ZIP.
2. Open **index.html** in Chrome, Edge, Safari or Firefox.
3. Select a financial year, fiscal quarter, month, state, courier, payment mode or product. Filters persist across pages.
4. Open **data/DeliverIQ_Excel_Dataset.xlsx** to inspect inputs and Excel formulas.

The dashboard works offline. Keep `app.js`, `style.css` and the `data` folder beside `index.html`. Alternatively, open **DeliverIQ_Standalone.html**, which embeds all its assets and data. No login, installation, CDN, API or corporate email is needed to view it.

## Business problem

Shipping more orders does not necessarily improve contribution. Delivery failures, post-delivery returns, reverse freight and inventory write-offs can erase product margins. DeliverIQ connects delivery service levels with financial consequences and proposed actions.

## Dashboard pages

| Page | Decision supported |
| --- | --- |
| Executive overview | Prioritise service and contribution issues |
| Courier performance | Compare carrier service and total fulfilment cost |
| PIN-code intelligence | Identify destination-level delivery friction |
| COD & delivery recovery | Compare payment cohorts and reattempt recovery |
| Returns & reverse logistics | Separate RTO from customer returns and inspect recovery time |
| Cost-to-serve & profitability | Reconcile retained revenue to contribution |
| Decision simulator | Estimate a savings-only intervention business case |
| Data & methodology | Audit definitions and browse/search individual orders |

Every page includes an observation, a business implication and a recommended action. Narrative values recalculate with filters; recommendations are rules-based, not an external AI service.

## Included

- 20,000 synthetic orders, eight FYTD monthly cohorts, 10 states, 12 sample city/PIN destinations, 6 product categories and 4 fictional couriers.
- Excel workbook: Overview, Scenario, Monthly, Orders and Dictionary.
- CSV, JSON and offline JavaScript data copy.
- Eight full-page screenshots.
- LinkedIn project description, launch post, short role description and portfolio card copy.
- Source code, seeded data generator, CSV refresh utility and documentation.

## Important definitions

- On-time rate = on-time delivered / delivered; includes orders subsequently returned by customers.
- First-attempt success = first-attempt delivered / all dispatched.
- RTO rate = RTO / dispatched.
- Customer return rate = post-delivery returns / delivered.
- Contribution = retained revenue − recognised product cost − logistics − inventory write-off.
- Logistics = forward freight + reverse freight + packaging + COD fee + return handling.

All returns receive full revenue refunds. Recoverable returned inventory is not treated as sold COGS; only write-offs are expensed. Contribution excludes GST, advertising, marketplace commission, overhead and financing costs. It is not net profit.

The dataset is a retrospective closed-cohort simulation. All outcomes are known; there is no open-shipment queue or inventory balance. Dates identify dispatch cohorts, and durations are simulated. Later outcomes can extend beyond the FYTD dispatch cutoff. One pair, one parcel and one courier per order; no partial returns or split shipments.

## Technology

Excel formulas and structured source table; HTML, CSS, vanilla JavaScript and inline SVG charts. Python utilities are optional for refreshing or reproducing data. Viewing and analysis require no Python.

## Refresh and publishing

See [Excel guide](docs/EXCEL_GUIDE.md), [methodology](docs/METHODOLOGY.md), [GitHub guide](docs/GITHUB_GUIDE.md) and [validation](docs/VALIDATION.md).

Author: [Sanjiban Das](https://www.linkedin.com/in/sanjibandas009/).
