import pymysql
import pandas as pd
import csv

con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur = con.cursor()
cur.execute("select * from orders")
row = cur.fetchall()
con.commit()
con.close
c= []
sums = 0
qty =0
for ro in row:
    sums = sums + ro[6]
    qty = qty + ro[5]
totalsale = []
totalsale.append(sums)
totalqty = []
totalqty.append(qty)
print("Total Sale is " , sums)
print("Total Sales Units is " , qty)

con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur2 = con2.cursor()
#cur2.execute("select Pname and bill, count(Pname and bill) as value_occurrence from orders group by Pname and bill order by value_occurrence desc limit 100;")
cur2.execute("select MAX(QTY) AS maximum FROM orders limit 100")
row3 = cur2.fetchall()
for ro in row3:
    print(ro)
cur2.execute("select Pname,QTY, COUNT(*) AS magnitude FROM orders GROUP BY QTY ORDER BY magnitude DESC LIMIT 100")
row5 = cur2.fetchall()
for ro4 in row5:
    print(ro4)
cur2.execute("select * from products where Defected > 0 Limit 100000")
row6 = cur2.fetchall()
abc = []
items = []
DEfecte = []
for ro6 in row6:
    i = 0
    a = int(ro6[2]) 
    b = int(ro6[5])
    c = int(a * b)
    DEfecte.append(c)
    items.append(ro6[1])
    abc.append(c)
ap = []
ap.append(sum(DEfecte))
cur2.execute("select * from products")
row9 = cur2.fetchall()
PQTY = []
PPRICE = []
for ro9 in row9:
    i = 0
    a = int(ro9[2]) 
    b = int(ro9[4])
    c = int(a * b)
    PPRICE.append(c)
PQTY.append(sum(PPRICE))
"""
C = {   'Sale': sums,
        'QTY' : qty,
        'Defected Items': items,
        'Lose': abc,
        
    }


#df = pd.DataFrame(C, columns= ['Sale','QTY','Defected Items','Lose','most']).transpose()


#export_csv = df.to_csv (r'pandaresult.csv' ,index = None, header=True) # here you have to write path, where result file will be stored
df = pd.DataFrame.from_dict(C, orient='index', columns= ['Sale','QTY','Defected Items','Lose'])
df = df.transpose()
df.to_csv(r'hel.csv',index = None, header=True)"""
totalSTk= []
cur2.execute("select * from products")
row7 = cur2.fetchall()
for r in row7:
    print(r[4])
    totalSTk.append(r[4])
totalstock = []
totalstock.append(sum(totalSTk))
a = {'Defected Items': items,'Lose': abc,'Total Sale':totalsale,'Sale Item':totalqty,'Total Stock':totalstock,'Total Stock Value': PQTY,'Total Lose':ap,}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df)
df.to_csv(r'helo.csv')
print (df)
print("defected item lose : ",sum(DEfecte))