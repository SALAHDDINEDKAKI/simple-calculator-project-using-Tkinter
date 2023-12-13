import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.iconbitmap('')
app_width = 570
app_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False,False)
root.configure(bg="#17161b")

label_result= Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C",width=5,height=1,font=("arial", 30, "bold"), bd=1,fg="#fff", bg="#3697f5").place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial", 30, "bold"), bd=1,fg="#fff", bg="#2a2d36").place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial", 30, "bold"), bd=1,fg="#fff", bg="#2a2d36").place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial", 30, "bold"), bd=1,fg="#fff", bg="#2a2d36").place(x=430,y=100)

root.mainloop()