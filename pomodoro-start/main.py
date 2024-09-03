from tkinter import *
import math

from music import Music

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
REPS=0
timer=None

sounds=Music()
window=Tk()
#window.minsize(height=300, width=400)
window.config(padx=10,pady=10,bg=YELLOW)
window.title("Pomodoro")


def saySomething(thing):
    print(thing)

def countDown(count):
    countMinute=math.floor(count/60)
    countSec=count%60
    global timer
    if countSec < 10:
        countSec=f"0{countSec}"
    canvas.itemconfig(timerText, text=f"{countMinute}:{countSec}")
    if count>0:
        timer= window.after(1000,countDown, count-1)
    else:
        button_start()


label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=("Arial",25,"bold"))
label.grid(row=0,column=1)
canvas=Canvas(width=210, height=224,  bg=YELLOW, highlightthickness=0)
tomatoImg=PhotoImage(file='tomato.png')
canvas.create_image(103,112,image=tomatoImg)
timerText=canvas.create_text(103,130, text="00:00",fill="white",
                   font=("Arial", 25,"bold"))
canvas.grid(row=1,column=1)



def button_click2():
    buttonQuit.quit()

buttonQuit=Button(text="Quit",command=button_click2 )
buttonQuit.config(padx=5,pady=5, highlightthickness=0)
buttonQuit.grid(column=1,row=5)

labelNumberSession=Label()
labelNumberSession.config(padx=5,pady=5)
labelNumberSession.grid(column=1,row=4)

def button_start():
    #buttonQuit.quit()
    global REPS
    workSec=WORK_MIN*60
    shortBreak=SHORT_BREAK_MIN*60
    longBreakSec=LONG_BREAK_MIN*60
    
    REPS+=1
    if REPS %2==0:
        countDown(shortBreak)
        sounds.brakeTime()
        
        
    
    elif REPS%8==0:
        countDown(longBreakSec)
        sounds.finish()
    else:
        countDown(workSec)
        mark=""
        workSessions=math.floor(REPS/2)
        for _ in range(workSessions):
            mark+="✔"
        labelNumberSession.config(text=mark, fg=GREEN,bg=YELLOW)
        

    
    #pass
buttonStart=Button(text="Start",command=button_start )
buttonStart.config(padx=5,pady=5,highlightthickness=0)
buttonStart.grid(column=0,row=3)

def button_reset():
    #buttonQuit.quit()
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    labelNumberSession.config(text="")
    global REPS
    REPS=0
    #pass


buttonReset=Button(text="Reset",command=button_reset )
buttonReset.config(padx=5,pady=5,highlightthickness=0)
buttonReset.grid(column=2,row=3)






window.mainloop()

# ----------------- TIMER RESET ----------------- # 

# --------------- TIMER MECHANISM --------------- # 

# -------------- COUNTDOWN MECHANISM ------------ # 

# --------------- UI SETUP ---------------------- #