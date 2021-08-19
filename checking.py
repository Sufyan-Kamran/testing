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
for ro6 in row6:

    i = 0
    print("****************Defected******************\n")
    print(ro6[1],ro6[2],ro6[3], ro6[5])
    a = int(ro6[2]) 
    b = int(ro6[5])
    c = int(a * b)
    print("defected item lose : ",a * b)
    
    #print(ro6)
    items.append(ro6[1])
    #items.append(asa)
    abc.append(c)
print("Total lose of Defected itmes is : ","Rs",sum(abc))
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
a = {'Defected Items': items,'Lose': abc,}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df)
df.to_csv(r'helo.csv')
print (df)