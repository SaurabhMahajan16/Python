from tkinter import *

dialogueBox=Tk()
dialogueBox.title("challenge with grid")
dialogueBox.minsize(height=300, width=500)
dialogueBox.config(padx=20,pady=20)
label=Label(text="new label")
label.grid(column=0,row=0)
label.config(padx=20,pady=20)

def button_action():
    print("I am clicked")
    
def button_action2():
    print("I am clicked 2")

newButton=Button(text="click", command=button_action)
newButton.grid(row=0, column=2)
newButton.config(padx=20,pady=20)

button=Button(text="click me", command=button_action2)
button.grid(row=1, column=1)
button.config(padx=20,pady=20)

input=Entry()
input.config(width=30)
input.insert(END, string="email")
input.grid(row=2,column=3)
#input.config(padx=20,pady=20)

dialogueBox.mainloop()