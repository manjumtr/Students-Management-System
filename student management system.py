from tkinter import *
import tkinter.messagebox
import sqlite3
from tkinter import ttk

root=Tk()
root.title("student database syatem")
root.geometry("1350x750+0+0")
root.config(bg="light grey")

#database
con=sqlite3.connect("student_database.db")
c=con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS students(
usn text,
fname text,
sname text,
dob text,
age text,
gender text,
address text,
mobile text
)

""")
con.commit()
con.close()

usn=StringVar()
fname=StringVar()
sname=StringVar()
dob=StringVar()
age=StringVar()
gender=StringVar()
address=StringVar()
mobile=StringVar()

#functions
def adddata():
    con=sqlite3.connect("student_database.db")
    c=con.cursor()
    
    if(len(str(usn.get())))!=0 and len(fname.get())!=0 and len(sname.get())!=0 and len(dob.get())!=0 and len(age.get())!=0 and len(gender.get())!=0 and len(address.get())!=0 and len(mobile.get())!=0:
        if type(int(usn.get()))==int:   
           c.execute("INSERT INTO students VALUES(:usn,:fname,:sname,:dob,:age,:gender,:address,:mobile)",

                  {'usn':usntxt.get(),
                   'fname':fnametxt.get(),
                   'sname':snametxt.get(),
                   'dob':dobtxt.get(),
                   'age':agetxt.get(),
                   'gender':gendertxt.get(),
                   'address':addresstxt.get(),
                   'mobile':mobiletxt.get()
                   
                   })
        else:
            tkinter.messagebox.showinfo("Warning!!!","USN must be an integer")

       
    else:
        tkinter.messagebox.showinfo("Warning!!!","All feilds are mandatory")
        
        
    con.commit()
    con.close()
    usntxt.delete(0,END)
    fnametxt.delete(0,END)
    snametxt.delete(0,END)
    dobtxt.delete(0,END)
    agetxt.delete(0,END)
    gendertxt.delete(0,END)
    addresstxt.delete(0,END)
    mobiletxt.delete(0,END)

    return

def display():
    con=sqlite3.connect("student_database.db")
    c=con.cursor()
    c.execute("SELECT * FROM students")
    rows=c.fetchall()
    studentlist.delete(*studentlist.get_children())
    for row in rows:
        studentlist.insert('',0,values=row)
    con.commit()
    con.close()
        
        
    return

def clear():
    usntxt.delete(0,END)
    fnametxt.delete(0,END)
    snametxt.delete(0,END)
    dobtxt.delete(0,END)
    agetxt.delete(0,END)
    gendertxt.delete(0,END)
    addresstxt.delete(0,END)
    mobiletxt.delete(0,END)
    return

def delete():
    con=sqlite3.connect("student_database.db")
    c=con.cursor()
    if len(usn.get())!=0 and type(int(usn.get()))==int:
        c.execute("DELETE FROM students WHERE usn= "+usntxt.get())
    else:
        tkinter.messagebox.showinfo("Warning!!!","Enter a valid USN")

        
    con.commit()
    con.close()
    
  
    return

def search():
    con=sqlite3.connect("student_database.db")
    c=con.cursor()
    if len(usn.get())!=0 and type(int(usn.get()))==int:
        c.execute("SELECT * FROM students WHERE usn= "+usn.get())
        a=c.fetchone()
        if a:
            studentlist.delete(*studentlist.get_children())
            studentlist.insert('',END,values=a)
        else:
            tkinter.messagebox.showinfo("Warning!!!","No data found")
    elif type(usn.get())==str:
        tkinter.messagebox.showinfo("Warning!!!","Enter a valid USN")
        

    else:
        tkinter.messagebox.showinfo("Warning!!!","Enter a valid USN")
    con.commit()
    con.close()
    
    
    return

def update():
    con=sqlite3.connect("student_database.db")
    c=con.cursor()
    if len(usn.get())!=0 and type(int(usn.get()))==int:
                if(len(usn.get())!=0 and len(fname.get())!=0 and len(sname.get())!=0 and len(dob.get())!=0 and len(age.get())!=0 and len(gender.get())!=0 and len(address.get())!=0 and len(mobile.get())!=0):
                    c.execute("UPDATE students SET fname=?, sname=?, dob=?, age=?, gender=?, address=?, mobile=? WHERE usn=?",(
                    fnametxt.get(),
                    snametxt.get(),
                    dobtxt.get(),
                    agetxt.get(),
                    gendertxt.get(),
                    addresstxt.get(),
                    mobiletxt.get(),
                    usntxt.get()))
                else:
                    tkinter.messagebox.showinfo("Warning!!!","All fields are mandatory")
    else:
        tkinter.messagebox.showinfo("Warning!!!","Enter a valid USN")
    clear()
    
    con.commit()
    con.close()
    return

def iexit():
    iexit=tkinter.messagebox.askyesno("Student Database Mangement System","Confirm if you want to exit")
    if iexit>0:
        root.destroy()
        return    

#frames
Label(root,font=('arial',40,'bold'),text="STUDENT MANAGEMENT SYSTEM",padx=10,pady=3,bg='light grey').pack(side=TOP,fill=X)

dataframe=LabelFrame(root,bd=1,width=1300,height=300,padx=20,pady=20,bg="light grey", font=('arial',20,'bold'),text="Student info",relief=RIDGE)
dataframe.pack(side=TOP)

buttonframe=Frame(root,bd=1,width=1300,height=60,padx=35,pady=10,bg="light grey",relief=RIDGE)
buttonframe.pack(side=TOP)

infoframe=LabelFrame(root,bd=1,width=1300,height=300,padx=30,pady=15,bg="light grey",font=('arial',20,'bold'),text="Student details",relief=RIDGE)
infoframe.pack(side=TOP)

#labels and texts

usnlabel=Label(dataframe,font=('arial',22,'bold'),text="USN:",padx=10,pady=3,bg='light grey')
usnlabel.grid(row=0,column=0,sticky=W)
usntxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=usn,width=25,bg='ghost white')
usntxt.grid(row=0,column=1,sticky=W)
fnamelabel=Label(dataframe,font=('arial',22,'bold'),text="NAME:",padx=10,pady=3,bg='light grey')
fnamelabel.grid(row=0,column=2,sticky=W)
fnametxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=fname,width=25,bg='ghost white')
fnametxt.grid(row=0,column=3,sticky=E)

snamelabel=Label(dataframe,font=('arial',22,'bold'),text="Email:",padx=10,pady=3,bg='light grey')
snamelabel.grid(row=1,column=0,sticky=W)
snametxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=sname,width=25,bg='ghost white')
snametxt.grid(row=1,column=1,sticky=W)

doblabel=Label(dataframe,font=('arial',22,'bold'),text="DOB:",padx=10,pady=3,bg='light grey')
doblabel.grid(row=1,column=2,sticky=W)
dobtxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=dob,width=25,bg='ghost white')
dobtxt.grid(row=1,column=3,sticky=W)

agelabel=Label(dataframe,font=('arial',22,'bold'),text="AGE:",padx=10,pady=3,bg='light grey')
agelabel.grid(row=2,column=0,sticky=W)
agetxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=age,width=25,bg='ghost white')
agetxt.grid(row=2,column=1,sticky=W)

genderlabel=Label(dataframe,font=('arial',22,'bold'),text="GENDER:",padx=10,pady=3,bg='light grey')
genderlabel.grid(row=2,column=2,sticky=W)
gendertxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=gender,width=25,bg='ghost white')
gendertxt.grid(row=2,column=3,sticky=W)

mobilelabel=Label(dataframe,font=('arial',22,'bold'),text="MOBILE:",padx=10,pady=3,bg='light grey')
mobilelabel.grid(row=3,column=0,sticky=W)
mobiletxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=mobile,width=25,bg='ghost white')
mobiletxt.grid(row=3,column=1,sticky=W)

addresslabel=Label(dataframe,font=('arial',22,'bold'),text="ADDRESS:",padx=10,pady=3,bg='light grey')
addresslabel.grid(row=3,column=2,sticky=W)
addresstxt=Entry(dataframe,font=('arial',22,'bold'),textvariable=address,width=25,bg='ghost white')
addresstxt.grid(row=3,column=3,sticky=W)

#buttons
badd=Button(buttonframe,text="Add New",font=('arial',20,'bold'),height=1,width=9,bd=2,command=adddata)
badd.grid(row=0,column=0)

bdisplay=Button(buttonframe,text="Display",font=('arial',20,'bold'),height=1,width=9,bd=2,command=display)
bdisplay.grid(row=0,column=1)

bclear=Button(buttonframe,text="Clear",font=('arial',20,'bold'),height=1,width=9,bd=2,command=clear)
bclear.grid(row=0,column=2)

bdelete=Button(buttonframe,text="Delete",font=('arial',20,'bold'),height=1,width=9,bd=2,command=delete)
bdelete.grid(row=0,column=3)

bsearch=Button(buttonframe,text="Search",font=('arial',20,'bold'),height=1,width=9,bd=2,command=search)
bsearch.grid(row=0,column=4)

bupdate=Button(buttonframe,text="Update",font=('arial',20,'bold'),height=1,width=9,bd=2,command=update)
bupdate.grid(row=0,column=5)

bexit=Button(buttonframe,text="Exit",font=('arial',20,'bold'),height=1,width=9,bd=2,command=iexit)
bexit.grid(row=0,column=6)

#listbox

scrolbarx=Scrollbar(infoframe,orient=HORIZONTAL)
scrolbary=Scrollbar(infoframe,orient=VERTICAL)

studentlist=ttk.Treeview(infoframe,columns=("usn","name","email","dob","age","gender","address","mobile"),xscrollcommand=scrolbarx.set,yscrollcommand=scrolbary.set)
scrolbarx.pack(side=BOTTOM,fill=X)
scrolbary.pack(side=RIGHT,fill=Y)
scrolbarx.config(command=studentlist.xview)
scrolbary.config(command=studentlist.yview)

studentlist.heading("usn",text="USN",)
studentlist.heading("name",text="First Name")
studentlist.heading("email",text="Email")
studentlist.heading("dob",text="DOB")
studentlist.heading("age",text="Age")
studentlist.heading("gender",text="Gender")
studentlist.heading("address",text="Address")
studentlist.heading("mobile",text="Mobile")
studentlist['show']=['headings']
studentlist.column('usn',width=100,)
studentlist.column('name',width=140)
studentlist.column('email',width=180)
studentlist.column('dob',width=100)
studentlist.column('age',width=100)
studentlist.column('gender',width=100)
studentlist.column('address',width=300)
studentlist.column('mobile',width=200)
studentlist.pack()

root=mainloop()
