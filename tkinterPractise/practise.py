from tkinter import *

dialogueBox=Tk()
dialogueBox.title("First tkinter")
#dialogueBox["title"]="Love"
dialogueBox.minsize(width=300, height=200)
label_box=Label(text="Hi How")
label_box["text"]="new text"
label_box.config(text="Thank you")
label_box.pack()



def button_action():
    label_box.config(text=input.get())
    label_box.pack(side="top")
    

button=Button(text="click me",command=button_action)
button.config(text="new click")
button.pack(side="bottom")

input=Entry()
input.config(width=30)
input.insert(END,string="text to start")
userInput=input.get()
input.pack()
"""no. of lines is height"""
text=Text(height=5, width=30)
text.insert(END, "multiline text entry")
text.focus()
"""to put cursor in textbox """
print(text.get("1.0", END))
"""text starting form 1st line to character 0"""

text.pack()

#spinbox
def spinbox_used():
    
    """gets current value in spinbox"""
    print(spinbox.get())

spinbox=Spinbox(from_=0, to=10, width=8, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)
    
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    """print 1 if it is checked 0 if its not"""
    print(checked_state.get())
 
checked_state=IntVar()
   
checkButton=Checkbutton(text="all in", variable=checked_state,
                        command=checkbutton_used)

checkButton.pack()
    
def radio_used():
    print(radio_state.get())

radio_state=IntVar()    
radioButton1=Radiobutton(text='try to be pure',
                         value=1, variable=radio_state,
                         command=radio_used)
radioButton2=Radiobutton(text='try to forget about fruit',
                         value=2, variable=radio_state,
                         command=radio_used)
radioButton3=Radiobutton(text='try not to feel sad when someone hurt you',
                         value=3, variable=radio_state,
                         command=radio_used)

radioButton4=Radiobutton(text='dont react if someone defame you and make fun of you',
                         value=4, variable=radio_state,
                         command=radio_used)
radioButton1.pack()
radioButton2.pack()    
radioButton3.pack()
radioButton4.pack()

def listbox_selected(event):
    """gets current selection in listbox"""
    print(listbox.get(listbox.curselection()))
itemList=["kind", "patience","trust", "believe","gain knowledge",
          "dont loose hope","love", "faith"]
listbox=Listbox(height=len(itemList))
for item in itemList:
    listbox.insert(itemList.index(item), item)

listbox.bind("<<ListboxSelect>>",listbox_selected)
listbox.pack()
class PractiseKWargs:
    
    def __init__(self, **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.type=kw.get("type")
        self.color=kw.get("color")
        self.seats=kw.get("seats")
        
newCar= PractiseKWargs(make="Honda", model="civic", type="sedan", color="white", seats=5)
print(newCar.seats)
secondCar=PractiseKWargs(make="Honda", model="CRV")
print(secondCar.seats)
"""when we use get method while using kwargs then we wont need to specify like in 2nd car 
likewe havent specify other fields in this
"""

dialogueBox.mainloop()