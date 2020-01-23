from tkinter import *
import tkinter as tk
import time,sqlite3,tkinter.filedialog,tkinter.messagebox,pymysql,importlib
root = Tk()
root.geometry('1000x800')
root.title("ข้อมูล")
mail = StringVar()
tel = StringVar()
user = StringVar()
religion = StringVar()
entry_0 = Entry(root,textvar= religion,width = 45)
entry_0.place(x=170,y=500)
entry_1 = Entry(root,textvar= mail,width = 45)
entry_1.place(x=170,y=600)
entry_2 = Entry(root,textvar=tel,width = 45)
entry_2.place(x=680,y=500)
label_13 = Label(root, text="E-mail(อีเมล) :",width=20,font=("bold", 10))
label_13.place(x=-25,y = 600)
label_14 = Label(root, text="Telephone(หมายเลขโทรศัพท์) :",width=20,font=("bold", 10))
label_14.place(x=515,y=500)
label_15 = Label(root, text="User Type(ประเภทผู้ใช้งาน) :",width=20,font=("bold", 10))
label_15.place(x=10,y=500)
def saveInputDB():
    try:
        textbox = []
        mail = entry_0.get()
        tel = entry_1.get()
        user = entry_2.get()
        textbox.append(mail)
        textbox.append(tel)
        textbox.append(user)
        cnx = pymysql.connect(user='root', password='', host='localhost', database='test')
        cur = cnx.cursor()
        insert = "INSERT INTO studeninfo ( userid, password, realname)"
        value = "VALUES ('"+str(textbox[0])+"', '"+str(textbox[1])+"', '"+str(textbox[2])+"')"
        count = cur.execute( insert + value)
        cnx.commit()
        cur.close()
        cnx.close()
        tkinter.messagebox.showinfo("บันทึกฐานข้อมูล","บันทึกข้อมูลสำเร็จ")
    
    except:
        tkinter.messagebox.showinfo("บันทึกฐานข้อมูล","บันทึกข้อมูลไม่สำเร็จ กรุณาตรวจสอบการใช้งานอีกครั้ง")
button_saveDB = Button(root, text='บันทึกในฐานข้อมูล',width=18,bg='green',fg='white',font=("bold", 10),command=saveInputDB).place(x=520,y=600)
root.mainloop()