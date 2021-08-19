import pymysql
from collections import Counter

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

for ro6 in row6:

    i = 0
    print("****************Defected******************\n")
    print(ro6[1],ro6[2],ro6[3], ro6[5])
    a = int(ro6[2]) 
    b = int(ro6[5])
    c = int(a * b)
    print("defected item lose : ",a * b)
    #print(ro6)

    abc.append(c)

total = 0
for i in range(0,len(abc)):
    total = total + abc[i]

print("Total lose of Defected itmes is : ",total)


#with open("hellos.txt","w+") as fa:
#    f = fa.write(f"hello{total}")
