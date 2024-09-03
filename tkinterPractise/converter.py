from tkinter import *
import math

dialogueBox=Tk()
dialogueBox.title("Mile to km converter")
dialogueBox.minsize(height=150, width=300)
dialogueBox.config(padx=10,pady=20)
label1=Label(text="is equal to")
label1.grid(column=0,row=1)
label1.config(padx=5,pady=5)



input=Entry()
input.config(width=15)

input.grid(row=0,column=2)

label2=Label(text="Miles")
label2.grid(column=3,row=0)
label2.config(padx=2,pady=2)

label3=Label()
label3.grid(column=2,row=1)
label3.config(padx=2,pady=2)

label4=Label(text="Km")
label4.grid(column=3,row=1)
label4.config(padx=2,pady=2)

def button_click():
    miles=int(input.get())
    km=math.ceil(miles*1.6)
    label3.config(text=km)
    

button=Button(text="Calculate",command=button_click )
button.grid(column=2,row=2)

def button_click2():
    buttonQuit.quit()

buttonQuit=Button(text="Quit",command=button_click2 )
buttonQuit.grid(column=3,row=2)




dialogueBox.mainloop()

