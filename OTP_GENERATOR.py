import random
import smtplib
from validate_email import validate_email
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")
img=PhotoImage(file="lock-300x300.png")
Label(root,image=img,bg="#ffffff").pack()

entry = Entry(root,fg="#000000",bg="#ffffff",bd=1)
entry.place(x=120,y=50,width=350,height=20)

label= Label(root,text="ENTER EMAIL ID")
label.place(x=15,y=50)

otp_num=random.randint(1000,10000)

def vali() :
    
    #generate a 4-digit otp number

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls() # for security...
    server.login("dakshitpandey.dp@gmail.com",password="ezykendsskxhxzvv")
    msg="hello user, Your OTP is "+str(otp_num)
    server.sendmail("dakshitpandey.dp@gmail.com",entry.get(),msg)
    server.quit()
    messagebox.showinfo(" ","otp sent successfully")


#verified OTP
def result() :
    messagebox.showinfo("","OTP verified")




btn= Button(root,text="SEND OTP",bg="#98F5FF",command=vali)
btn.place(x=199,y=90)

entry2=Entry(root)
entry2.place(x=120,y=190,width=350,height=20)

label2= Label(root,text="Enter Your OTP")
label2.place(x=15,y=190)


btn2=Button(root,text='SUBMIT',bg="#98F5FF",command=result)
btn2.place(x=199,y=260)





root.mainloop()