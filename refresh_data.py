"""Refresh the offline dashboard from an Excel-exported CSV. Standard library only."""
import csv,json,pathlib,sys,datetime,math
root=pathlib.Path(__file__).resolve().parents[1]
path=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else root/'data/DeliverIQ_Orders.csv'
numeric=['Attempts','Promise_Days','Delivery_Days','Restock_Days','Order_Value','Unit_Cost','Forward_Freight','Reverse_Freight','Packaging','COD_Fee','Return_Handling','Writeoff']
required=['Order_ID','Order_Date','Month','State','City','PIN','Tier','Product','Courier','Payment','Channel','Warehouse','Status','Return_Reason']+numeric
with path.open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f);missing=set(required)-set(reader.fieldnames or [])
 if missing:raise ValueError('Missing columns: '+', '.join(sorted(missing)))
 rows=list(reader)
if not rows:raise ValueError('No records supplied')
seen=set()
for i,r in enumerate(rows,2):
 if not r['Order_ID'] or r['Order_ID'] in seen:raise ValueError(f'Row {i}: missing or duplicate Order_ID')
 seen.add(r['Order_ID'])
 for k in required:
  if not r[k].strip():raise ValueError(f'Row {i}: blank {k}')
 for k in numeric:
  r[k]=float(r[k].replace(',',''))
  if not math.isfinite(r[k]) or r[k]<0:raise ValueError(f'Row {i}: invalid {k}')
 r['PIN']=r['PIN'].zfill(6)
 if not r['PIN'].isdigit() or len(r['PIN'])!=6:raise ValueError(f'Row {i}: invalid PIN')
 date=datetime.date.fromisoformat(r['Order_Date']);r['Month']=date.strftime('%Y-%m')
 if r['Status'] not in ['Retained','RTO','Customer return']:raise ValueError(f'Row {i}: unsupported status')
 if r['Payment'] not in ['COD','Prepaid']:raise ValueError(f'Row {i}: unsupported payment')
 if r['Tier'] not in ['Metro','Tier 2','Tier 3']:raise ValueError(f'Row {i}: unsupported tier')
 if r['Attempts'] not in [1,2,3] or r['Promise_Days']<=0:raise ValueError(f'Row {i}: invalid transit assumptions')
 if r['Status']=='RTO' and r['Delivery_Days']!=0:raise ValueError(f'Row {i}: RTO must have zero delivery days')
 if r['Status']!='RTO' and r['Delivery_Days']<=0:raise ValueError(f'Row {i}: delivered order requires transit days')
 if r['Status']=='Retained' and any(r[k]!=0 for k in ['Restock_Days','Reverse_Freight','Return_Handling','Writeoff']):raise ValueError(f'Row {i}: retained order has return costs')
 if r['Writeoff']>r['Unit_Cost']:raise ValueError(f'Row {i}: writeoff exceeds unit cost')
 r.update(Net_Revenue=r['Order_Value'] if r['Status']=='Retained' else 0,Recognised_COGS=r['Unit_Cost'] if r['Status']=='Retained' else 0,Logistics_Cost=sum(r[k] for k in ['Forward_Freight','Reverse_Freight','Packaging','COD_Fee','Return_Handling']),Delivered=int(r['Status']!='RTO'))
 r['On_Time']=int(r['Delivered'] and r['Delivery_Days']<=r['Promise_Days']);r['First_Attempt']=int(r['Delivered'] and r['Attempts']==1)
 fy=date.year if date.month>=4 else date.year-1
 r.update(Financial_Year=f'FY {fy}-{str(fy+1)[2:]}',Fiscal_Quarter='Q'+str(((date.month-4)%12)//3+1),Fiscal_Month=(date.month-4)%12+1)
 if not (datetime.date(2026,4,1)<=date<=datetime.date(2026,11,16)):raise ValueError(f'Row {i}: outside FYTD 1 Apr-16 Nov 2026')
 r['Contribution']=r['Net_Revenue']-r['Recognised_COGS']-r['Logistics_Cost']-r['Writeoff']
ordered=['Order_ID','Order_Date','Month','State','City','PIN','Tier','Product','Courier','Payment','Channel','Warehouse','Status','Attempts','Promise_Days','Delivery_Days','Return_Reason','Restock_Days','Order_Value','Unit_Cost','Forward_Freight','Reverse_Freight','Packaging','COD_Fee','Return_Handling','Writeoff','Net_Revenue','Recognised_COGS','Logistics_Cost','Delivered','On_Time','First_Attempt','Contribution','Financial_Year','Fiscal_Quarter','Fiscal_Month']
rows=[{k:r[k] for k in ordered} for r in rows]
root.joinpath('data/data.js').write_text('window.DELIVERIQ_DATA='+json.dumps(rows,separators=(',',':'))+';',encoding='utf-8')
root.joinpath('data/orders.json').write_text(json.dumps(rows,separators=(',',':')),encoding='utf-8')
print(f'Validated and refreshed {len(rows):,} orders. Reload index.html. Workbook is not modified.')
