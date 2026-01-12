from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1ab641"
YELLOW = "#f7f5dd"
PURPLE = "#6E026F"
GREY = "#1e293b" 
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    '''reset all the checkmarks, text inside the timer, stop the timer and change the title label back to 
    the text Timer'''
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00") # ⭐
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps+=1
   
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="LONG BREAK", fg=RED)
        session_label.config(text="🍵 Take a proper break!", fg=PURPLE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="SHORT BREAK", fg=PINK)
        session_label.config(text="☕ Quick break time", fg=PURPLE)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=GREEN)
        session_label.config(text="🚀 Deep work session", fg=PURPLE)
        # count_down(15) # pass seconds to count_down function and ther it calculates min and sec for that

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# after - Execute a command after a time delay, https://www.tcl-lang.org/man/tcl8.6/TclCmd/after.htm
# This command is used to delay execution of the program or to execute a command in 
# background sometime in the future.
# The command sleeps for ms milliseconds and then returns. 

def notify_user():
    # 1. Restore window if possible
    try:
        window.state("normal")
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
    except:
        pass

    # 2. Always notify (guaranteed)
    window.bell()

def count_down(count): # -> this method is called repeatidly after 1 second
    # now we have to format the min and sec
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}") #⭐The Python string zfill() method
    # is used to pad a string with zeros on the left side to reach a specified total width
    
# u can use zfill as well,
# like count_sec.zfill(2) then it will add filling zeroes infront

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        notify_user()

        start_timer()  # Auto-start next session

        # update checkmarks
        # after 2 reps one 25 work session done!!
        # Add a checkmark after each completed WORK session
        work_sessions = math.floor(reps/2)
        # for _ in range(work_sessions):
        check_mark.config(text="✔️" * work_sessions)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # as per the image sizze in even (to get things done easy)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)# we've told our canvas to create an image at this position,
# and then we've put the image inside.

timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2, row=3)

#Label
label = Label(text="Pomodoro Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=2, row=1)

# Session info label
session_label = Label(text="Ready to focus?", 
                     fg=RED, bg=YELLOW,
                     font=(FONT_NAME, 15))
session_label.grid(column=2, row=2)

#start_btn
def action1():
    start_timer()

#reset_btn:
def action2():
    reset_timer()

#calls action() when pressed
start_btn = Button(text="Start", command=action1, 
                   fg="WHITE", bg=PURPLE, 
                   font=(FONT_NAME, 20, "bold"),
                   padx=10, pady=10,
                   relief="flat",  # Modern flat button style
                   activebackground=GREEN,  # Color when clicked
                   activeforeground="WHITE")

start_btn.grid(column=1, row=4)

reset_btn = Button(text="Reset", command=action2, 
                   fg="WHITE", bg=GREY, 
                   font=(FONT_NAME, 20, "bold"),
                   padx=10, pady=10,
                   relief="flat",
                   activebackground=RED,
                   activeforeground="WHITE")
reset_btn.grid(column=3, row=4)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=2, row=5)

window.mainloop()




# Grid layout

# I find it easier to keep all the grid() statements together. 
# I imagine it would be quite difficult in a large GUI interface to keep track, especially if new objects are added later.

# # Grid layout
# label_activity.grid(row=0, column=1)
# canvas.grid(row=1, column=1)
# button_start.grid(row=2, column=0)
# button_reset.grid(row=2, column=2)
# label_tick.grid(row=3, column=1)
