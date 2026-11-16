import json,pathlib,csv
root=pathlib.Path(__file__).resolve().parents[1]
r=json.loads(root.joinpath('data/orders.json').read_text());assert len(r)==20000
assert len({x['Order_ID'] for x in r})==len(r)
assert len({x['Month'] for x in r})==8
for x in r:
 assert x['Net_Revenue']==(x['Order_Value'] if x['Status']=='Retained' else 0)
 assert x['Recognised_COGS']==(x['Unit_Cost'] if x['Status']=='Retained' else 0)
 assert x['Logistics_Cost']==sum(x[k] for k in ['Forward_Freight','Reverse_Freight','Packaging','COD_Fee','Return_Handling'])
 assert x['Contribution']==x['Net_Revenue']-x['Recognised_COGS']-x['Logistics_Cost']-x['Writeoff']
 assert x['On_Time']==int(x['Status']!='RTO' and x['Delivery_Days']<=x['Promise_Days'])
 assert x['First_Attempt']==int(x['Status']!='RTO' and x['Attempts']==1)
 assert 0<=x['Writeoff']<=x['Unit_Cost']
total={k:sum(x[k] for x in r) for k in ['Net_Revenue','Recognised_COGS','Logistics_Cost','Writeoff','Contribution','Delivered','On_Time']}
assert min(x['Order_Date'] for x in r)=='2026-04-01'
assert max(x['Order_Date'] for x in r)=='2026-11-16'
assert all(x['Financial_Year']=='FY 2026-27' for x in r)
assert set(x['Fiscal_Quarter'] for x in r)=={'Q1','Q2','Q3'}
total.update(Orders=len(r),RTO=sum(x['Status']=='RTO' for x in r),Customer_Returns=sum(x['Status']=='Customer return' for x in r))
root.joinpath('docs/validation_totals.json').write_text(json.dumps(total,indent=2))
print('PASS: row logic, unique IDs, 8 FYTD cohorts, cost reconciliation and denominators.');print(total)
