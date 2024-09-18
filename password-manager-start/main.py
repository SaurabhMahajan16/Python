import random
import string

#passwordgenerator=[string.ascii_lowercase]+[strin\\g.ascii_uppercase]+specialChar+[string.digits]
#generatedString=''.join(random.choices(passwordgenerator, k=passwordLength))

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox

window=Tk()
#window.minsize(height=300, width=400)
window.config(padx=50,pady=50)
window.title("Password Manager")
canvas=Canvas(width=200, height=200)
passwordImg=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=passwordImg)
canvas.grid(row=0, column=1)

labelWebsite=Label()
labelWebsite.config(text="Website:")
labelWebsite.grid(row=1, column=0)

#labelWebsite.config(padx=5,pady=5)
inputWebsite=Entry()
inputWebsite.config(width=35)
inputWebsite.grid(row=1, column=1, columnspan=2)
inputWebsite.focus()

emailLabel=Label(text="Email/Username:")
emailLabel.grid(row=2, column=0)


inputEmail=Entry()
inputEmail.config(width=35)
inputEmail.insert(0,string="srbhmahajan16@gmail.com")
inputEmail.grid(row=2, column=1, columnspan=2)

passworLabel=Label(text="Password:")
passworLabel.grid(row=3,column=0)
inputPassword=Entry()
inputPassword.config(width=17)
inputPassword.grid(row=3,column=1)

def generate_password():
    specialChar=['!', '@', '#', '$', '%', '^', '&', '*']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    numberOfLetters=random.randint(8,10)
    numberOfsymbols=random.randint(2,4)
    numberOfdigits=random.randint(2,4)


    passwordLetters=[random.choice(letters) for _ in range(random.randint(8,10))]
    passwordSymbols=[random.choice(specialChar) for _ in range(random.randint(2,4))]
    passwordDigits=[random.choice(numbers) for _ in range(random.randint(2,4))]
    #passwordUpperLetters=[uppercaseAphabets for _ in range(numberOfsymbols)]
    generatedPassword=passwordLetters+passwordDigits+passwordSymbols
    random.shuffle(generatedPassword)
    generatedPassword=''.join(generatedPassword)
    #print(generatedPassword)
    if len(inputPassword.get())>=0:
        inputPassword.delete(0,END)
        inputPassword.insert(0, string=generatedPassword)

generatePassButton=Button(text="Generate Password", command=generate_password)
generatePassButton.grid(row=3, column=2)

def add_button():
    passwordDetails=[]
    website=inputWebsite.get()
    #print(website)
    email=inputEmail.get()
    password=inputPassword.get()
    #print(password)
    details=f"{website} | {email} | {password} \n"
    #passwordDetails.append(details)
    if len(website)!=0 and len(email)!=0 and len(password)!=0:
        okToSave=messagebox.askokcancel(title=website, message=f"These are the details entered \n Email:{email}\nWebsite:{website}\nPassword:{password} \n Is it ok to save")
        if okToSave:
            with open("passwordManager.txt", "a") as editor:
                editor.write(details)
            inputPassword.delete(0,END)
            inputWebsite.delete(0,END)   
        #pass
    else:
        messagebox.showerror("error", "Please enter data in all fields")
    

addButton=Button(text="Add",command=add_button,width=36)
addButton.grid(row=4, column=1, columnspan=2)

window.mainloop()