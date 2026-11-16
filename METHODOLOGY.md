# Methodology and model limitations

Source: source/generate_data.py, seeded Python pseudorandom generator (19951219). No real commercial records or customer information. Operational patterns are deliberately simulated, not estimated from market data.

The generator varies delivery failure probability by payment, city tier, courier and festive dispatch month. RouteX has deliberately worse performance to create a reviewable case. Observed rankings therefore demonstrate the analytical workflow, not actual courier quality. All four courier names are fictional.

## Grain and recognition

One row = one order = one dispatched parcel = one pair. Each row has one final status: Retained, RTO or Customer return. Retained orders recognise sales and product cost. Returned orders recognise zero retained revenue, zero sold COGS, actual logistics and any unsaleable inventory write-off. This keeps recoverable inventory from being expensed twice.

Contribution is operational contribution, not statutory profit. Omitted costs include tax, commission, advertising, overhead and capital costs. COD fee is charged on delivered COD orders, including later customer returns. Packaging and outbound freight apply to every dispatch. Reverse freight and handling apply only to returns.

## Rates and populations

| Metric | Numerator | Denominator |
| --- | --- | --- |
| On-time delivery | Delivered within Promise_Days | Delivered including later customer returns |
| First-attempt success | Delivered with Attempts = 1 | All dispatched |
| RTO | RTO parcels | All dispatched |
| Customer return | Customer return parcels | All delivered |
| Reattempt recovery | Delivered with Attempts > 1 | All parcels not delivered on the first attempt |
| Contribution margin | Contribution | Retained net revenue |

Zero-denominator rates display a dash. Weighted totals use aggregate numerators and denominators, never averages of segment percentages.

## Simulator

Avoided RTO = selected dispatches × minimum(requested percentage-point reduction / 100, baseline RTO rate).

Gross savings = avoided RTO × user-assumed avoidable cost.

Net benefit = gross savings − intervention spend.

Default 3 pp, INR 180 and INR 15,000 are illustrative inputs. Avoidable cost is not automatically equal to total RTO cost: outbound costs may still be incurred on successful deliveries. No recovered revenue or incremental contribution is assumed. No causal or realised saving is claimed.

## Geography and returns

Only 12 sample PIN destinations are represented. The chart labels cities because each sample city has one PIN. Warehouse assignment is simulated, not a route-optimisation solution. Restock_Days is a completed return duration, not current ageing. Recoverable stock value is cumulative cohort flow, not current working capital.

## Insight rules

Insights use filtered aggregate metrics, largest observed failure rates and transparent accounting. Carrier and geography comparisons are descriptive and subject to mix effects. Use matched trials before acting. No predictive ML, live external data feed, production decision engine or AI API is included.
