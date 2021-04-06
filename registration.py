from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import  messagebox
import pymysql

win=Tk()
win.title('Registration')
win.geometry('1350x700+0+0')
# bg image
image = Image. open('13.jpg')
image = image. resize((1350, 700), Image. ANTIALIAS)
bg=ImageTk.PhotoImage(image)
bag=Label(win,image=bg).place(x=230,y=0,relwidth=1)
# 2nd pic
image1 = Image. open('11.jpg')
image1 = image1. resize((400, 500), Image. ANTIALIAS)
bg1=ImageTk.PhotoImage(image1)
bag1=Label(win,image=bg1).place(x=100,y=100)

# from
frame=Frame(win,bg='white')
frame.place(x=501,y=102,width=700,height=502)
tittle=Label(frame,text="Registration Here", font=("times new roman", 20 ,'bold'),bg='white',fg='green')
tittle.place(x=50,y=30)

fname_var=StringVar()
f_name=Label(frame,text="Frist Name", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
f_name.place(x=50,y=100)
f_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=fname_var)
f_name_entry.place(x=50,y=130)

con_var=StringVar()
c_name=Label(frame,text="Contact", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
c_name.place(x=50,y=160)
c_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=con_var)
c_name_entry.place(x=50,y=190)

Q_name=Label(frame,text="Security Question", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
Q_name.place(x=50,y=220)
com_var=StringVar()
c_box=ttk.Combobox(frame,font=("times new roman", 13),justify=CENTER,state='readonly',textvariable=com_var)
c_box['values']=('select','Favourite pet','Birth place','Best friend Name')
c_box.current(0)
c_box.place(x=50,y=250)

pass_var=StringVar()
p_name=Label(frame,text="Password", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
p_name.place(x=50,y=280)
p_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=pass_var)
p_name_entry.place(x=50,y=310)

lname_var=StringVar()
l_name=Label(frame,text="Last Name", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
l_name.place(x=300,y=100)
l_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=lname_var)
l_name_entry.place(x=300,y=130)


email=StringVar()
e_name=Label(frame,text="Email", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
e_name.place(x=300,y=160)
e_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=email)
e_name_entry.place(x=300,y=190)

answer=StringVar()
A_name=Label(frame,text="Answer", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
A_name.place(x=300,y=220)
A_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=answer)
A_name_entry.place(x=300,y=250)

cpass_var=StringVar()
c_name=Label(frame,text="Confirm Password", font=("times new roman", 15 ,'bold'),bg='white',fg='grey')
c_name.place(x=300,y=280)
c_name_entry=Entry(frame, font=("times new roman", 15 ),bg='lightgrey',textvariable=cpass_var)
c_name_entry.place(x=300,y=310)

check_var=IntVar()
chek=Checkbutton(frame,text='I Agree The Condition',onvalue=1,offvalue=0,font=("times new roman", 12 ),bg='white',variable=check_var)
chek.place(x=50,y=340)





def clear():
     
    
    f_name_entry.delete(0,END)
    e_name_entry.delete(0,END)
    l_name_entry.delete(0,END)
    A_name_entry.delete(0,END)
    c_name_entry.delete(0,END)
    p_name_entry.delete(0,END)
    


def regis():

    if fname_var.get()=='' or pass_var.get()=='' or check_var.get()==''or con_var.get()=='':
        messagebox.showerror('Error','All file are required to fill up')

    elif cpass_var.get() != pass_var.get():
        messagebox.showerror('Error','pass not match')
        
    # connecting with database below

    else:
        try:
            con=pymysql.connect(host="localhost",user='root',password='',database='student')
            cur=con.cursor()
            cur.execute("select * from st where email=%s",email.get())
            row=cur.fetchone()
            if row != None:
                messagebox.showerror('Error','use another email')
            else:    
                cur.execute('insert into st (FName,LName,Contact,Email,Question,Answer,Pass) values(%s,%s,%s,%s,%s,%s,%s)',
                (fname_var.get(),lname_var.get(),con_var.get(),email.get(),com_var.get(),answer.get(),pass_var.get()))#todo
                con.commit()
                con.close()
                messagebox.showinfo('sucess','Registration Complete')
                clear()

        except: 
            messagebox.showerror("Error",'Bech error' )

        # messagebox.showinfo('sucess','Registration Complete')

    
# print(f'fast name {fname_var.get()}last {lname_var.get()} contact{con_var.get()} box {com_var.get()} pass {pass_var.get()} enail {email.get()} anwer {answer.get()} cpass {cpass_var.get()} chek {check_var.get()}')





button=Button(frame,text='Registration Now',cursor="hand2",font=("times new roman", 15 ,'bold'),bg='grey',fg='white',command=regis)
button.place(x=50,y=380,width=200,height=50)

or_=Label(frame,text="Or",font=("times new roman", 20 ,'bold'),bg='white',fg='grey')
or_.place(x=270,y=390)



buttonl=Button(frame,text='sign up',cursor="hand2",font=("times new roman", 20 ,'bold'),bg='grey',fg='white')
buttonl.place(x=320,y=380,width=200,height=50)

 

win.configure(bg= '#25383C')
win.mainloop()



