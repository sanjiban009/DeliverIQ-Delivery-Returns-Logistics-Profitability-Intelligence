# FYTD validation

20,000 distinct orders from 1 April to 16 November 2026. Eight monthly cohorts; Q1, Q2 and partial Q3. Row-level revenue, COGS, logistics, contribution and outcome flags checked. Exact totals are in validation_totals.json. Fiscal dates and quarter mapping validated.

Workbook calculations checked against independent dataset totals; no desktop Microsoft Excel testing was performed. Dashboard fiscal-quarter and partial-month filters were checked.


## Financial Year slicer verification
Financial Year is populated from the dataset and filters all eight pages. FY 2026-27 with Q1 returns 7,854 orders; navigation preserves the selection and reset restores 20,000 orders. Screenshots refreshed with the year selected. Only FY 2026-27 is present in this synthetic dataset.
