import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import font
import pymysql
from tkinter import messagebox
#from tkcalendar import Calendar, DateEntry


root = Tk()
root.title("Stationary Managment System | Admin Panel | Developed By Maryam.")
root.geometry("1500x800+0+0")
#lab = Label(root, text="ADMINSTRATION PANEL",fg="red", font=("times new roman", 24,"bold"))
#lab.place(x=600,y=2)
lab1 = Label(root, text="Employees",fg="black", font=("times new roman", 18,"bold"))
lab1.place(x=10,y=0)
lab2 = Label(root, text="Orders",fg="Green", font=("times new roman", 18,"bold"))
lab2.place(x=420,y=0)
lab3 = Label(root, text="Inventrory",fg="blue", font=("times new roman", 18,"bold"))
lab3.place(x=900,y=0)

pid_var= StringVar()
id_var = StringVar()
fname_var = StringVar()
lname_var = StringVar()
email_var =StringVar()
passw_var = StringVar()
occup_var = StringVar()
pname_var = StringVar()
Price_var =StringVar()
Category_var =StringVar()
Qty_var= StringVar()
Defected_var = StringVar()

def searchs():
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    cur.execute("select * from userinformations where id=%s",(searching.get()))
    
    row = cur.fetchone()
    print(row)
    
    ent1.insert(0,row[0])
    ent2.insert(0,row[1])
    ent3.insert(0,row[2])
    ent4.insert(0,row[3])
    ent5.insert(0,row[4])
    ent6.insert(0,row[5])
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)

def new():
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    cur.execute("select * from employees where email=%s",email.get())
    row = cur.fetchone()
    if fname_var.get() == "" or lname_var.get() == "" or email_var.get()== "" or passw_var.get() == "" or occup_var.get() == "":
        messagebox.showerror("Field Error"," All fields are required")
    else:
        if len(passw_var.get()) < 8:
            messagebox.showerror("Password Error","Password must be contain 8 character ")
        else:
            if row == None:
                cur.execute("insert into employees(fname,lname,email,passwrd,occupation) values(%s,%s,%s,%s,%s)",(fname_var.get(),lname_var.get(),email_var.get(),passw_var.get(),occup_var.get()))
                con.commit()
                con.close
                fname_var.delete(0,END)
                lname_var.delete(0,END)
                email_.delete(0,END)
                passw_var.delete(0,END)
                occup_var.delete(0,END)
                messagebox.showinfo("New User", "New user added successfully")
            else:
                messagebox.showerror("error","Already exist")
                email.config(fg="red")
                print(email.get(),"already exist")

            
    
def Newpro():
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    if p_name.get() == "" or price.get() == "":
        messagebox.showerror("Field Error"," All fields are required")
    else:
        cur.execute("insert into products(PName,Price,Category,QTY) values(%s,%s,%s,%s)",(pname_var.get(),Price_var.get(),Category_var.get(),Qty_var.get()))
        con.commit()
        con.close
        messagebox.showinfo("New Product", "New product added successfully")
            

        
    


def selected():
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)

    
    #grab record NUmber 

    selects = treeview.focus()

    #grab record values
    value = treeview.item(selects,'values')
    ent1.insert(0,value[0])
    ent2.insert(0,value[1])
    ent3.insert(0,value[2])
    ent4.insert(0,value[3])
    ent5.insert(0,value[4])
    ent6.insert(0,value[5])
    

def selectedprd():
    p_name.delete(0,END)
    price.delete(0,END)
    Qty.delete(0,END)
    PID.delete(0,END)
    Category.delete(0,END)
    
    #grab record NUmber 

    selects = treeview3.focus()

    #grab record values
    value = treeview3.item(selects,'values')
    PID.insert(0,value[0])
    p_name.insert(0,value[1])
    price.insert(0,value[2])
    Qty.insert(0,value[4])
    Category.insert(0,value[3])
    defected.insert(0,value[5])
    
    

    
def update():
    
    
    
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    
    cur.execute("update employees set fname=%s,lname=%s,email=%s,passwrd=%s,occupation=%s where id=%s",(fname_var.get(),lname_var.get(),email_var.get(),passw_var.get(),occup_var.get(),id_var.get()))
    con.commit()
    con.close()    
    messagebox.showinfo("Record Updated", "Record updated successfully")
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)

    
def updateprd():
    
    
    
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    
    cur.execute("update products set PName=%s,Price=%s,Category=%s,QTY=%s,Defected=%s where Pid=%s",(pname_var.get(),Price_var.get(),Category_var.get(),Qty_var.get(),Defected_var.get(),PID.get()))
    con.commit()
    con.close()    
    messagebox.showinfo("Record Updated", "Record updated successfully")
    
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)



def dltprod():
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
        cur = con.cursor()
        
        cur.execute("delete from products where Pid=%s",(pid_var.get()))
        con.commit()
        con.close()    
        messagebox.showinfo("Record Deleted", "Record deleted successfully")
        
    except Exception as e:
        print(e)       


def delt():
        
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    
    cur.execute("delete from employees where id=%s",(id_var.get()))
    
    con.commit()
    con.close()    
    messagebox.showinfo("Record Deleted", "Record deleted successfully")
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    ent6.delete(0,END)




def TAB():
    global treeview
    global treeview2
    global treeview3
    con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur = con.cursor()
    cur.execute("select * from employees")
    row = cur.fetchall()

    #connect = mysql.connector.connect(host="localhost", user="root",password="",database="sufyan")
    #conn= connect.cursor()
    #conn.execute("select * from user")
    #print(conn)

    treeview =ttk.Treeview(root,height=700)
    treeview["columns"]= ("Id","Name","Lastname","email","Password","Occupation")
    treeview["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("Treeview.Heading", foreground="blue", font=("times new roman", 14, "bold"))
    #adding columns

    treeview.column('Id', width=1, minwidth=1,anchor=tk.CENTER)
    treeview.column('Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview.column('Lastname', width=30, minwidth=20,anchor=tk.CENTER)
    treeview.column('email', width=30, minwidth=30,anchor=tk.CENTER)
    treeview.column('Password', width=30, minwidth=30,anchor=tk.CENTER)
    treeview.column('Occupation', width=30, minwidth=30,anchor=tk.CENTER)

    #adding heading
    treeview.heading('Id', text='Id', anchor=CENTER)
    treeview.heading('Name', text='Name', anchor=CENTER)
    treeview.heading('Lastname', text='Lastname', anchor=CENTER)
    treeview.heading('email', text='Email' ,anchor=CENTER)
    treeview.heading('Password', text='Password' ,anchor=CENTER)
    treeview.heading('Occupation', text='Occupation' ,anchor=CENTER)
    #treeview.pack(side=TOP, fill=BOTH)

    treeview.place(x=5,y=30,width=410,height=500)

        
    i = 0
    for ro in row:
        treeview.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview, orient="vertical")
    hsb.configure(command=treeview.yview)
    treeview.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)



    ## order 
    
    con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur2 = con2.cursor()
    cur2.execute("select * from orders")
    row2 = cur2.fetchall()
    treeview2 =ttk.Treeview(root,height=700)
    treeview2["columns"]= ("Id","Name","email","order","date")
    treeview2["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview2.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))

    #adding columns

    treeview2.column('Id', width=5, minwidth=5,anchor=tk.CENTER)
    treeview2.column('Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview2.column('email', width=30, minwidth=30,anchor=tk.CENTER)
    treeview2.column('order', width=30, minwidth=30,anchor=tk.CENTER)
    treeview2.column('date', width=30, minwidth=30,anchor=tk.CENTER)

    #adding heading
    treeview2.heading('Id', text='Id', anchor=CENTER)
    treeview2.heading('Name', text='Name', anchor=CENTER)
    treeview2.heading('email', text='Email' ,anchor=CENTER)
    treeview2.heading('order', text='Order' ,anchor=CENTER)
    treeview2.heading('date', text='Date' ,anchor=CENTER)
    #treeview2.pack(side=TOP, fill=BOTH)

    treeview2.place(x=420,y=30,width=470,height=500)

        
    i = 0
    for ro in row2:
        treeview2.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview2, orient="vertical")
    hsb.configure(command=treeview2.yview)
    treeview2.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)


    ## order 
    con4 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
    cur4 = con4.cursor()
    cur4.execute("select * from products")
    row4 = cur4.fetchall()
    treeview3 =ttk.Treeview(root,height=700)
    treeview3["columns"]= ("PId","P_Name","Price","Category","Qty","Defects")
    treeview3["show"]="headings"
    s = ttk.Style(root)
    s.theme_use("vista")
    s.configure(".", font=('times new roman', 11))
    s.configure("treeview3.Heading", foreground="BLUE", font=("times new roman", 14, "bold"))

    #adding columns


    treeview3.column('PId', width=5, minwidth=5,anchor=tk.CENTER)
    treeview3.column('P_Name', width=30, minwidth=20,anchor=tk.CENTER)
    treeview3.column('Price', width=30, minwidth=30,anchor=tk.CENTER)
    treeview3.column('Category', width=30, minwidth=30,anchor=tk.CENTER)
    treeview3.column('Qty', width=30, minwidth=30,anchor=tk.CENTER)
    treeview3.column('Defects', width=30, minwidth=30,anchor=tk.CENTER)

    #adding heading
    treeview3.heading('PId', text='PId', anchor=CENTER)
    treeview3.heading('P_Name', text='P_Name', anchor=CENTER)
    treeview3.heading('Price', text='Price' ,anchor=CENTER)
    treeview3.heading('Category', text='Category' ,anchor=CENTER)
    treeview3.heading('Qty', text='Qty' ,anchor=CENTER)
    treeview3.heading('Defects', text='Defected' ,anchor=CENTER)
    #treeview3.pack(side=TOP, fill=BOTH)

    treeview3.place(x=900,y=30,width=600,height=600)

        
    i = 0
    for ro in row4:
        treeview3.insert('',i, text="", values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i = i+1
    hsb = ttk.Scrollbar(treeview3, orient="vertical")
    hsb.configure(command=treeview3.yview)
    treeview3.configure(yscrollcommand=hsb.set)
    hsb.pack(fill=Y,side=RIGHT)


global ent1
global ent2
global ent3
global ent4
global ent5
global ent6

#Delete And Update records
UaD = Label(root, text="Add/Update/Delete records",fg="Purple", font=("times new roman",15))
UaD.place(x=10,y=530)

lent1 = Label(root,text="ID", fg="blue",font=("times new roman",16))
lent1.place(x=10,y=560)
ent1 = Entry(root,textvariable=id_var,width=30)
ent1.place(x=120,y=560,height=30)

lent2 = Label(root,text="First Name", fg="blue",font=("times new roman",16))
lent2.place(x=10,y=600)
ent2 = Entry(root,width=30,textvariable=fname_var)
ent2.place(x=120,y=600,height=30)

lent3 = Label(root,text="Last Name", fg="blue",font=("times new roman",16))
lent3.place(x=10,y=640)
ent3 = Entry(root,width=30,textvariable=lname_var)
ent3.place(x=120,y=640,height=30)

lent4 = Label(root,text="Email", fg="blue",font=("times new roman",16))
lent4.place(x=10,y=680)
ent4 = Entry(root,width=30,textvariable=email_var)
ent4.place(x=120,y=680,height=30)

lent5 = Label(root,text="Password", fg="blue",font=("times new roman",16))
lent5.place(x=10,y=720)
ent5 = Entry(root,width=30,textvariable=passw_var)
ent5.place(x=120,y=720,height=30)

lent6 = Label(root,text="occupation", fg="blue",font=("times new roman",16))
lent6.place(x=10,y=760)
ent6 = Entry(root,width=30,textvariable=occup_var)
ent6.place(x=120,y=760,height=30)

#Create New User
#cframe = Frame(root,width=420,height=590)
#cframe.place(x=1030,y=0)

################################### new product entry 

Nlabel =Label(root, text="New Product", font=("times new roman",15,"bold"),fg="green")
Nlabel.place(x=870,y=640)
global p_name
P_name = Label(root, text="P_Name : ", font=("times new roman",15),fg="blue")
P_name.place(x=870,y=680)
p_name = Entry(root,textvariable=pname_var, font=("times new roman",15),fg="Gray")
p_name.place(x=970,y=680)

global price
LPrice = Label(root, text="Price : ", font=("times new roman",15),fg="blue")
LPrice.place(x=870,y=720)
price = Entry(root,textvariable=Price_var, font=("times new roman",15),fg="gray")
price.place(x=970,y=720)
global Qty
LQTY = Label(root, text="QTY : ", font=("times new roman",15),fg="blue")
LQTY.place(x=870,y=760)
Qty = Entry(root, font=("times new roman",15),textvariable=Qty_var,fg="gray")
Qty.place(x=970,y=760)
global Category
LC = Label(root, text="Category : ", font=("times new roman",15),fg="blue")
LC.place(x=1200,y=680)
Category= Entry(root, font=("times new roman",15),textvariable=Category_var,fg="gray")
Category.place(x=1280,y=680)
global defected
DC = Label(root, text="Defected : ", font=("times new roman",15),fg="blue")
DC.place(x=1200,y=720)
defected= Entry(root, font=("times new roman",15),textvariable=Defected_var,fg="gray")
defected.place(x=1280,y=720)

global PID
PId = Label(root, text="P_ID: ", font=("times new roman",15),fg="blue")
PId.place(x=1200,y=760)
PID= Entry(root, font=("times new roman",15),textvariable=pid_var,fg="gray")
PID.place(x=1280,y=760)



Pbtn = Button(root, text="Add_Prod",bg="green",fg="white", command=Newpro)
Pbtn.place(x=1010,y=640,width=80)
UPbtn = Button(root, text="Update_Prod",bg="orange",fg="white", command=updateprd)
UPbtn.place(x=1100,y=640,width=80)
SEbtn = Button(root, text="select_Prod",bg="gray",fg="white", command=selectedprd)
SEbtn.place(x=1190,y=640,width=80)
DLbtn = Button(root, text="Dlt_Prod",bg="red",fg="white", command=dltprod)
DLbtn.place(x=1280,y=640,width=80)


#Create user button
rbtn = Button(root, text="REFRESH",fg="WHITE", bg="orange", command=TAB)
rbtn.place(x=320,y=610,width=70)
btn = Button(root, text="SELECTED", command=selected)
btn.place(x=320,y=650,width=70)
abtn = Button(root, text="Add User",fg="WHITE", bg="Green", command=new)
abtn.place(x=320,y=690,width=70)
ubtn = Button(root, text="Update",bg="blue",fg="white", command=update)
ubtn.place(x=320,y=730,width=70)
Dbtn = Button(root, text="Delete",bg="red",fg="white", command=delt)
Dbtn.place(x=320,y=770,width=70)



############################################ ORDER #####################################################

UaD = Label(root, text="Update/Delete Orders",fg="RED", font=("times new roman",15))
UaD.place(x=420,y=530)

lent1 = Label(root,text="P_ID", fg="blue",font=("times new roman",16))
lent1.place(x=420,y=560)
ent1 = Entry(root,textvariable=id_var,width=30)
ent1.place(x=530,y=560,height=30)

NAME1 = Label(root,text="Name", fg="blue",font=("times new roman",16))
NAME1.place(x=420,y=600)
name = Entry(root,width=30,textvariable=fname_var)
name.place(x=530,y=600,height=30)

EMAIL = Label(root,text="Email", fg="blue",font=("times new roman",16))
EMAIL.place(x=420,y=640)
email = Entry(root,width=30,textvariable=lname_var)
email.place(x=530,y=640,height=30)

ORDER = Label(root,text="Order", fg="blue",font=("times new roman",16))
ORDER.place(x=420,y=680)
order = Entry(root,width=30,textvariable=email_var)
order.place(x=530,y=680,height=30)

DATE5 = Label(root,text="Date", fg="blue",font=("times new roman",16))
DATE5.place(x=420,y=720)
date5 = Entry(root,width=30,textvariable=passw_var)
date5.place(x=530,y=720,height=30)

BILL6 = Label(root,text="Bill", fg="blue",font=("times new roman",16))
BILL6.place(x=420,y=760)
bill6 = Entry(root,width=30,textvariable=occup_var)
bill6.place(x=530,y=760,height=30)


#ORDERs button
Sbtn = Button(root, text="Select", command=selected)
Sbtn.place(x=730,y=690,width=70)
Ubtn = Button(root, text="Update",bg="blue",fg="white", command=update)
Ubtn.place(x=730,y=730,width=70)
dbtn = Button(root, text="Delete",bg="red",fg="white", command=delt)
dbtn.place(x=730,y=770,width=70)


TAB()






root.mainloop()