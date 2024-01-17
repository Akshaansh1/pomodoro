from tkinter import *
from PIL import ImageTk, Image
import math

# CONSTRAINTS
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None  

def start_timer():
    global reps, timer

    reps += 1
    work_sec = WORK_MIN * 60
    short_break =SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        my_label.config(text="Break" , fg='#d24545')
    elif reps % 2 == 0:
        count_down(short_break)
        my_label.config(text="Break" , fg = "#d63484")
    else:
        count_down(work_sec)
        my_label.config(text="Work" , fg = '#9dbc98')


def count_down(count):
    global timer 
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canv.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        works_sessions = math.floor(reps / 2)
        for _ in range(works_sessions):
            marks += "✅"
        lab.config(text=marks)


def update_label(label_text, color):
    my_label.config(text=label_text, fg=color, bg='#fff8e3', font=("Courier", 35, "bold"))


def reset_timer():
    global reps, timer
    reps = 0
    if timer is not None:
        window.after_cancel(timer)
    canv.itemconfig(timer_text, text="00:00")
    update_label("Timer", '#9dbc98')
    lab.config(text="")


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg='#fff8e3')

# canvas
my_label = Label(text="Timer", fg='#9dbc98', bg='#fff8e3', font=("Courier", 35, "bold"))
my_label.grid(row=0, column=1)

canv = Canvas(window, width=400, height=424, bg='#fff8e3', highlightthickness=0)
canv.grid(row=1, column=1)

img = ImageTk.PhotoImage(Image.open("tomato.png"))
canv.create_image(100, 112, anchor=NW, image=img)
timer_text = canv.create_text(200, 260, text="00:00", fill="white", font=("Courier", 35, "bold"))

start = Button(highlightthickness=0, text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(highlightthickness=0, text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

lab = Label(highlightthickness=0, text="", bg='#fff8e3', fg='#9dbc98')
lab.grid(row=2, column=1)

mainloop()
