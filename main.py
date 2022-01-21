def addbag():
    strr = 'select * from bagdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    bagtable.delete(*bagtable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        bagtable.insert('',END,values=vv)
    def submitadd():
        id = idval.get()
        type = typeval.get()
        number = numval.get()
        size = sizeval.get()
        addeddate = time.strftime('%d/%m/%Y')
        addedtime = time.strftime('%H:%M:%S')
        name = nameval.get()
        address = addressval.get()

        try:
            strr = 'insert into bagdata values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,type,number,size,addeddate,addedtime,name,address))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Number {} Added sucessfully.. and want to clean the form'.format(id,number),parent=addroot)
            if(res==True):
                idval.set('')
                typeval.set('')
                numval.set('')
                sizeval.set('')
                nameval.set('')
                addressval.set('')


        except:
            messagebox.showerror('Notifications','Id already exit try another id...',parent=addroot)

        strr = 'select * from bagdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        bagtable.delete(*bagtable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
            bagtable.insert('',END,values=vv)




    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x420+220+200')
    addroot.title('Add Bag')
    addroot.config(bg='blue')
    addroot.iconbitmap('logo.ico')
    addroot.resizable(False,False)
    #------------------ Add bags labels ----------------#

    idlabel = Label(addroot,text='Enter Id : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    typelabel = Label(addroot,text='Enter type : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    typelabel.place(x=10,y=70)

    numlabel = Label(addroot,text='Enter Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=130)

    sizelabel = Label(addroot,text='Enter size : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    sizelabel.place(x=10,y=190)

    namelabel = Label(addroot,text='Enter Name : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    namelabel.place(x=10,y=250)

    addresslabel = Label(addroot,text='Enter address : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    addresslabel.place(x=10,y=310)

    #------------------ Add bags Entry ----------------#
    idval = StringVar()
    typeval = StringVar()
    numval = StringVar()
    sizeval =StringVar()
    nameval = StringVar()
    addressval =StringVar()


    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    typeentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=typeval)
    typeentry.place(x=250,y=70)

    numentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=130)

    sizeentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=sizeval)
    sizeentry.place(x=250,y=190)

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=250)

    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=310)


    #------------------ Add button ----------------#
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=submitadd)
    submitbtn.place(x=150, y=370)


    addroot.mainloop()

def manufacture():
    def searchmanufacture():
        number = numval.get()


        if(number !=''):
            strr = "select *from bagdata where number=%s AND type=%s"
            mycursor.execute(strr,(number,'M'))
            datas = mycursor.fetchall()
            bagtable.delete(*bagtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                bagtable.insert('',END,values=vv)

            manroot.destroy()





    manroot = Toplevel(master=DataEntryFrame)
    manroot.grab_set()
    manroot.geometry('470x300+220+200')
    manroot.title('Manufacture')
    manroot.config(bg='firebrick')
    manroot.iconbitmap('logo.ico')
    manroot.resizable(False,False)
    #------------------ Add bags labels ----------------#
    numlabel = Label(manroot,text='Enter Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=10)

    passlabel = Label(manroot,text='Enter Password : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    passlabel.place(x=10,y=70)

    #------------------ Add bags Entry ----------------#

    numval = StringVar()

    numentry = Entry(manroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=10)

    passentry = Entry(manroot,font=('roman',15,'bold'),bd=5)
    passentry.place(x=250,y=70)

    #------------------ Add button ----------------#
    submitbtn = Button(manroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=searchmanufacture)
    submitbtn.place(x=150, y=250)


    manroot.mainloop()


def distributor():
    def searchdistributor():
        number = numval.get()


        if(number !=''):
            strr = "select *from bagdata where number=%s AND type=%s"
            mycursor.execute(strr,(number,'D'))
            datas = mycursor.fetchall()
            bagtable.delete(*bagtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                bagtable.insert('',END,values=vv)
            disroot.destroy()


    disroot = Toplevel(master=DataEntryFrame)
    disroot.grab_set()
    disroot.geometry('470x300+220+200')
    disroot.title('Distributor')
    disroot.config(bg='yellow')
    disroot.iconbitmap('logo.ico')
    disroot.resizable(False,False)
    #------------------ Add bags labels ----------------#
    numlabel = Label(disroot,text='Enter Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=10)

    passlabel = Label(disroot,text='Enter Password : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    passlabel.place(x=10,y=70)

    #------------------ Add bags Entry ----------------#

    numval = StringVar()

    numentry = Entry(disroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=10)

    passentry = Entry(disroot,font=('roman',15,'bold'),bd=5)
    passentry.place(x=250,y=70)

    #------------------ Add button ----------------#
    submitbtn = Button(disroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=searchdistributor)
    submitbtn.place(x=150, y=250)


    disroot.mainloop()

def vendor():
    def searchvendor():
        number = numval.get()


        if(number !=''):
            strr = "select *from bagdata where number=%s AND type=%s"
            mycursor.execute(strr,(number,'V'))
            datas = mycursor.fetchall()
            bagtable.delete(*bagtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                bagtable.insert('',END,values=vv)
            venroot.destroy()

    venroot = Toplevel(master=DataEntryFrame)
    venroot.grab_set()
    venroot.geometry('470x300+220+200')
    venroot.title('Vendor')
    venroot.config(bg='red2')
    venroot.iconbitmap('logo.ico')
    venroot.resizable(False,False)
    #------------------ Add bags labels ----------------#
    numlabel = Label(venroot,text='Enter Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=10)

    passlabel = Label(venroot,text='Enter Password : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    passlabel.place(x=10,y=70)

    #------------------ Add bags Entry ----------------#

    numval = StringVar()

    numentry = Entry(venroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=10)

    passentry = Entry(venroot,font=('roman',15,'bold'),bd=5)
    passentry.place(x=250,y=70)

    #------------------ Add button ----------------#
    submitbtn = Button(venroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=searchvendor)
    submitbtn.place(x=150, y=250)


    venroot.mainloop()

def customer():
    def searchcustomer():
        number = numval.get()


        if(number !=''):
            strr = "select *from bagdata where number=%s AND type=%s"
            mycursor.execute(strr,(number,'C'))
            datas = mycursor.fetchall()
            bagtable.delete(*bagtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                bagtable.insert('',END,values=vv)

            cusroot.destroy()

    cusroot = Toplevel(master=DataEntryFrame)
    cusroot.grab_set()
    cusroot.geometry('470x300+220+200')
    cusroot.title('Customer')
    cusroot.config(bg='pink')
    cusroot.iconbitmap('logo.ico')
    cusroot.resizable(False,False)
    #------------------ Add bags labels ----------------#
    numlabel = Label(cusroot,text='Enter Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=10)

    passlabel = Label(cusroot,text='Enter Password : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    passlabel.place(x=10,y=70)

    #------------------ Add bags Entry ----------------#

    numval = StringVar()

    numentry = Entry(cusroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=10)

    passentry = Entry(cusroot,font=('roman',15,'bold'),bd=5)
    passentry.place(x=250,y=70)

    #------------------ Add button ----------------#
    submitbtn = Button(cusroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=searchcustomer)
    submitbtn.place(x=150, y=250)


    cusroot.mainloop()

def recycle():
    def searchrecycle():
        number = numval.get()


        if(number !=''):
            strr = "select *from bagdata where number=%s AND type=%s"
            mycursor.execute(strr,(number,'R'))
            datas = mycursor.fetchall()
            bagtable.delete(*bagtable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
                bagtable.insert('',END,values=vv)
            recroot.destroy()


    recroot = Toplevel(master=DataEntryFrame)
    recroot.grab_set()
    recroot.geometry('470x300+220+200')
    recroot.title('Recycle')
    recroot.config(bg='green')
    recroot.iconbitmap('logo.ico')
    recroot.resizable(False,False)
    #------------------ Add bags labels ----------------#
    numlabel = Label(recroot,text='Enter Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=10)

    passlabel = Label(recroot,text='Enter Password : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    passlabel.place(x=10,y=70)

    #------------------ Add bags Entry ----------------#

    numval = StringVar()

    numentry = Entry(recroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=10)

    passentry = Entry(recroot,font=('roman',15,'bold'),bd=5)
    passentry.place(x=250,y=70)

    #------------------ Add button ----------------#
    submitbtn = Button(recroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=searchrecycle)
    submitbtn.place(x=150, y=250)


    recroot.mainloop()

def give():
    def submitgive():
        id = idval.get()
        type = typeval.get()
        number = numval.get()
        size = sizeval.get()
        date = dateval.get()
        time = timeval.get()
        name = nameval.get()
        address = addressval.get()


        strr = 'update bagdata set type=%s,number=%s,size=%s,date=%s,time=%s,name=%s,address=%s where id=%s'

        if(type == 'M'):
            typ = 'D'
        if(type == 'D'):
            typ = 'V'
        if(type == 'V'):
            typ = 'C'
        if(type == 'C'):
            typ = 'R'
        if(type == 'R'):
            typ = 'M'
        print(typ)
        mycursor.execute(strr,(typ,number,size,date,time,name,address,id))
        con.commit()
        messagebox.showinfo('Notifications','Bag {} distributed sucessfully..'.format(id),parent=giveroot)

        strr = 'select * from bagdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        bagtable.delete(*bagtable.get_children())
        for i in datas:
            vv = ['sucessfulL','sucessfulL','sucessfulL','sucessfulL','sucessfulL','sucessfulL','sucessfulL','sucessfulL']
            bagtable.insert('',END,values=vv)
        giveroot.destroy()



    giveroot = Toplevel(master=DataEntryFrame)
    giveroot.grab_set()
    giveroot.geometry('470x420+220+200')
    giveroot.title('Give Bag')
    giveroot.config(bg='blue')
    giveroot.iconbitmap('logo.ico')
    giveroot.resizable(False,False)
    #------------------ Add bags labels ----------------#

    idlabel = Label(giveroot,text='Bag Id : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    typelabel = Label(giveroot,text='Bag type : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    typelabel.place(x=10,y=70)


    sizelabel = Label(giveroot,text='Bag size : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    sizelabel.place(x=10,y=130)


    namelabel = Label(giveroot,text='Name : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    namelabel.place(x=10,y=190)

    addresslabel = Label(giveroot,text='Address : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    numlabel = Label(giveroot,text='Reciver Number : ',bg='gold2',font=('time',20,'bold'),relief=GROOVE,borderwidth=1,width=12,anchor='w')
    numlabel.place(x=10,y=310)





    #------------------ Add bags Entry ----------------#
    idval = StringVar()
    typeval = StringVar()
    numval = StringVar()
    sizeval =StringVar()
    dateval = StringVar()
    timeval = StringVar()
    nameval = StringVar()
    addressval = StringVar()




    identry = Entry(giveroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    typeentry = Entry(giveroot,font=('roman',15,'bold'),bd=5,textvariable=typeval)
    typeentry.place(x=250,y=70)

    sizeentry = Entry(giveroot,font=('roman',15,'bold'),bd=5,textvariable=sizeval)
    sizeentry.place(x=250,y=130)

    nameentry = Entry(giveroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=190)


    addressentry = Entry(giveroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    numentry = Entry(giveroot,font=('roman',15,'bold'),bd=5,textvariable=numval)
    numentry.place(x=250,y=310)


    #------------------ Add button ----------------#
    submitbtn = Button(giveroot,text='Give',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                        bg='red',command=submitgive)
    submitbtn.place(x=150, y=370)


    cc = bagtable.focus()
    content = bagtable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        typeval.set(pp[1])
        numval.set(pp[2])
        sizeval.set(pp[3])
        dateval.set(pp[4])
        timeval.set(pp[5])
        nameval.set(pp[6])
        addressval.set(pp[7])




    giveroot.mainloop()

def delete():
    cc = bagtable.focus()
    content = bagtable.item(cc)
    pp = content['values'][0]
    strr = 'delete from bagdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))

    strr = 'select * from bagdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    bagtable.delete(*bagtable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]]
        bagtable.insert('',END,values=vv)



# def exit():
#     res = messagebox.askyesnocancel('Notifications','Do you want to exit?')
#     if(res == True):
#         root.destroy()


#id, type, phone, size



############ ConnectToDataBase ###########
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect plase try again')
            return
        try:
            strr = 'create database bagmanagementsystem'
            mycursor.execute(strr)
            strr = 'use bagmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table bagdata(id int,type varchar(10),number varchar(12),size varchar(10),date varchar(50),time varchar(50),name varchar(20),address varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table bagdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table bagdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notifications','Database created and now you are connected to the database ...',parent=dbroot)



        except:
            strr = 'use bagmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notifications','Now you are connected to the database ...',parent=dbroot)



        dbroot.destroy()






    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('logo.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    ############### connectdb Label #############
    hostlabel = Label(dbroot,text="Enter Host : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)


    ############### connectdb Entry #############
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    ############### connectdb Button #############
    submitbutton = Button(dbroot,text='Submit', font=('roman',15,'bold'),width=20,bg='red',bd=5,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)




    dbroot.mainloop()

##########################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\r"+"Time :"+time_string)
    clock.after(200,tick)

###########################
import random
colors = ['red','green','blue','yellow','pink','red2','gold2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if(count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)
#############################
from tkinter import *
from tkinter import Toplevel, messagebox,ttk
from tkinter.ttk import Treeview
import pymysql
import time

root = Tk()
root.title('Bag Management System')
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.iconbitmap('logo.ico')
root.resizable(False,False)

########## frames ########
##-------------- Dataentry Frame Intro ---------------##
DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontlabel = Label(DataEntryFrame,text='--------------Welcome-------------',width=30,font=('arial',22,'italic bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Bag',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addbag)
addbtn.pack(side=TOP,expand=True)

manbtn = Button(DataEntryFrame,text='2. Manufacture',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=manufacture)
manbtn.pack(side=TOP,expand=True)

disbtn = Button(DataEntryFrame,text='3. Distributor',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=distributor)
disbtn.pack(side=TOP,expand=True)

disbtn = Button(DataEntryFrame,text='4. Vendor',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=vendor)
disbtn.pack(side=TOP,expand=True)

cusbtn = Button(DataEntryFrame,text='5. Customer',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=customer)
cusbtn.pack(side=TOP,expand=True)

recbtn = Button(DataEntryFrame,text='6. Recyler',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=recycle)
recbtn.pack(side=TOP,expand=True)

givebtn = Button(DataEntryFrame,text='7. Give',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=give)
givebtn.pack(side=TOP,expand=True)

delbtn = Button(DataEntryFrame,text='8. Delete Bag',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=delete)
delbtn.pack(side=TOP,expand=True)









# exitbtn = Button(DataEntryFrame,text='8. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
#                 activeforeground='white',command=exit)
# exitbtn.pack(side=TOP,expand=True)



##-------------- Show Data Frame ---------------##
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
bagtable = Treeview(ShowDataFrame,columns=('Id','Type','Number','Size','Added Date','Added Time','Name','Address'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=bagtable.xview)
scroll_y.config(command=bagtable.yview)
bagtable.heading('Id', text='Id')
bagtable.heading('Type', text='Type')
bagtable.heading('Number', text='Number')
bagtable.heading('Size', text='Size')
bagtable.heading('Added Date', text='Added Date')
bagtable.heading('Added Time', text='Added Time')
bagtable.heading('Name', text='Name')
bagtable.heading('Address', text='Address')
bagtable['show'] = 'headings '
bagtable.column('Id', width=100)
bagtable.column('Type', width=100)
bagtable.column('Number', width=200)
bagtable.column('Size', width=100)
bagtable.column('Added Date', width=150)
bagtable.column('Added Time', width=150)
bagtable.column('Name', width=150)
bagtable.column('Address', width=200)
bagtable.pack(fill=BOTH,expand=1)

######### Slider #########
ss = 'Welcome to Bag Management System'
count = 0
text = ''
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260, y=0)
IntroLabelTick()
IntroLabelColorTick()
######### clock ##########
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()

#########  ConnectToDataBaseButton #########
connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',
                        activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930, y=0)


root.mainloop()
