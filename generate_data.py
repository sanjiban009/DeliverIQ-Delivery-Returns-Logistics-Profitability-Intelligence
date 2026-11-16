import random,json,csv,pathlib,datetime
root=pathlib.Path(__file__).resolve().parents[1]
r=random.Random(19951219)
locations=[('West Bengal','Kolkata','700001','Metro'),('West Bengal','Siliguri','734001','Tier 2'),('Maharashtra','Mumbai','400001','Metro'),('Maharashtra','Nagpur','440001','Tier 2'),('Delhi','New Delhi','110001','Metro'),('Karnataka','Bengaluru','560001','Metro'),('Tamil Nadu','Chennai','600001','Metro'),('Uttar Pradesh','Lucknow','226001','Tier 2'),('Bihar','Patna','800001','Tier 2'),('Assam','Guwahati','781001','Tier 2'),('Rajasthan','Kota','324001','Tier 2'),('Odisha','Balasore','756001','Tier 3')]
products=[('Running shoes',1999,940),('Casual sneakers',1499,680),('Formal shoes',2299,1130),('Sandals',899,360),('Slippers',499,190),('Kids shoes',1199,490)]
rows=[]
for i in range(20000):
 d=datetime.date(2026,4,1)+datetime.timedelta(days=r.randrange(230)); month=d.strftime('%Y-%m')
 state,city,pin,tier=r.choice(locations); product,price,cost=r.choice(products); courier=r.choice(['SwiftShip','ParcelOne','RouteX','Bharat Express']); payment=r.choices(['COD','Prepaid'],[58,42])[0]
 festive=d.month in [10,11]; risk=.04+(.14 if payment=='COD' else 0)+(.04 if tier!='Metro' else 0)+(.045 if courier=='RouteX' else 0)+(.04 if festive else 0)
 status='RTO' if r.random()<risk else ('Customer return' if r.random()<(.115 if 'shoes' in product.lower() or 'sneakers' in product else .055) else 'Retained')
 attempts=r.choices([1,2,3],[75,20,5])[0] if status!='RTO' else r.choice([2,3]); promised=4 if tier=='Metro' else 6; days=max(1,promised+r.choice([-2,-1,0,0,1,2,4])+(1 if courier=='RouteX' else 0)) if status!='RTO' else 0
 freight=r.randint(45,75)+(20 if tier!='Metro' else 0)+(12 if courier=='Bharat Express' else 0); reverse=r.randint(40,75) if status!='Retained' else 0; pack=r.choice([12,15,18]); fee=25 if payment=='COD' and status!='RTO' else 0; handling=18 if status!='Retained' else 0; writeoff=round(cost*r.choice([0,0,0,.15,1])) if status!='Retained' else 0; sale=round(price*(1-r.choice([0,.05,.1,.15])))
 reason=r.choice(['Size or fit','Style preference','Quality issue','Wrong item']) if status=='Customer return' else (r.choice(['Customer refused','Unreachable','Address issue','Delivery delay']) if status=='RTO' else 'None')
 row=dict(Order_ID=f'DIQ{i+1:06}',Order_Date=d.isoformat(),Month=month,State=state,City=city,PIN=pin,Tier=tier,Product=product,Courier=courier,Payment=payment,Channel=r.choice(['Brand website','Marketplace']),Warehouse=r.choice(['Kolkata FC','Delhi FC','Mumbai FC']),Status=status,Attempts=attempts,Promise_Days=promised,Delivery_Days=days,Return_Reason=reason,Restock_Days=r.randint(5,19) if status!='Retained' else 0,Order_Value=sale,Unit_Cost=cost,Forward_Freight=freight,Reverse_Freight=reverse,Packaging=pack,COD_Fee=fee,Return_Handling=handling,Writeoff=writeoff)
 row.update(Net_Revenue=sale if status=='Retained' else 0,Recognised_COGS=cost if status=='Retained' else 0,Logistics_Cost=freight+reverse+pack+fee+handling,Delivered=int(status!='RTO'),On_Time=int(status!='RTO' and days<=promised),First_Attempt=int(status!='RTO' and attempts==1))
 row['Contribution']=row['Net_Revenue']-row['Recognised_COGS']-row['Logistics_Cost']-writeoff
 row.update(Financial_Year='FY 2026-27',Fiscal_Quarter='Q'+str(((d.month-4)%12)//3+1),Fiscal_Month=(d.month-4)%12+1)
 rows.append(row)
root.joinpath('data/orders.json').write_text(json.dumps(rows,separators=(',',':')))
with root.joinpath('data/DeliverIQ_Orders.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
root.joinpath('data/data.js').write_text('window.DELIVERIQ_DATA='+json.dumps(rows,separators=(',',':'))+';')
print('Generated',len(rows),'unique orders; contribution',sum(x['Contribution'] for x in rows))
