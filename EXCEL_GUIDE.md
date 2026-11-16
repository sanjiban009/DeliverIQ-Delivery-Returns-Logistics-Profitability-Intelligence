# Excel guide

The workbook holds all 20,000 orders and formula-driven financial calculations. The interactive slicers and page navigation are in the HTML dashboard; native Excel PivotTables or slicers are not prebuilt.

## Workbook

- Overview: formula-linked KPIs and monthly contribution chart.
- Scenario: editable amber inputs for RTO reduction, avoidable cost and intervention spend.
- Monthly: COUNTIFS and SUMIFS summaries.
- Orders: filterable source table. A:Z are inputs; AA:AJ are calculated fields.
- Dictionary: field definitions.

Input amounts are INR. Order dates are actual Excel dates. PIN codes are text. Formulas use standard IF, AND, SUM, COUNTIFS, SUMIFS, MIN and MAX functions. No macros, SQL or paid connector is needed.

## Change an assumption

On Scenario, change the amber cells. The model caps the reduction at the baseline RTO rate and prevents negative scenario inputs from producing negative counts. A reduction of 3 means **3 percentage points**, not a 3% relative change. Results cover the full FYTD workbook, not one month.

## Refresh HTML after Excel edits

1. Keep a backup of the supplied workbook and dashboard data.
2. Edit source fields A:Z in Orders. Preserve column headers and one row per parcel.
3. Format Order_Date as `yyyy-mm-dd`. Export **only the Orders sheet** as CSV UTF-8, for example `updated_orders.csv`.
4. With Python 3 available, run from the extracted project folder:

```bash
python3 source/refresh_data.py updated_orders.csv
```

On Windows, `py source/refresh_data.py updated_orders.csv` is an alternative.

5. Reload `index.html`. The script recomputes derived fields and updates data/data.js and data/orders.json. It does not modify the workbook or CSV. Run `python3 source/build_standalone.py` to refresh the single-file HTML copy too.
6. Check dashboard totals against Excel. If changing the date window, revise the fixed period labels in index.html, app.js and documentation.

The supplied workbook's summary formulas are bounded to rows 2:20001. If appending rows, extend the summary ranges and calculated columns. The HTML reads all validated CSV records after refresh.

## Optional Power Query / PivotTable learning workflow

Import the CSV with Excel's Text/CSV import, set PIN as text and amounts as numbers, and load to a table. Create a PivotTable with Courier in Rows and sums of Delivered, On_Time and Logistics_Cost in Values. Compute rates from summed numerators and denominators; do not average already-aggregated percentages. This is an optional extension, not a claim that a native Power Query connection is embedded.

Indian FYTD is fixed at 1 April–16 November 2026. The refresh utility rejects dates outside this window. Update the window, period labels and summary ranges together when extending the reporting cutoff. Fiscal fields in AH:AJ are calculated from Order_Date.
