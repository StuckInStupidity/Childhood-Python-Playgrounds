from tkinter import *
import time
import winsound

t = Tk()
t.title("Timer")
t.geometry("400x600")
t.config(bg="black")
t.resizable(False, False)

heading = Label(t, text="Timer", font="arial 30 bold", bg="black", fg="red")
heading.pack(pady=10)

Label(t, font=("arial", 15, "bold"), text="current time:", bg="darkblue").place(x=65, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

current_time = Label(t, font=("arial", 15, "bold"), text="", bg="darkblue")
current_time.place(x=190, y=70)
clock()

hrs = StringVar(value="00")
Entry(t, textvariable=hrs, width=2, font="arial 50", bg="black", fg="white", bd=0).place(x=30, y=155)

mins = StringVar(value="00")
Entry(t, textvariable=mins, width=2, font="arial 50", bg="black", fg="white", bd=0).place(x=150, y=155)

secs = StringVar(value="00")
Entry(t, textvariable=secs, width=2, font="arial 50", bg="black", fg="white", bd=0).place(x=270, y=155)

Label(t, text="hour", font=("arial", 12), bg="black", fg="white").place(x=105, y=200)
Label(t, text="mins", font=("arial", 12), bg="black", fg="white").place(x=225, y=200)
Label(t, text="secs", font=("arial", 12), bg="black", fg="white").place(x=345, y=200)

def timer():
    try:
        total_seconds = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(secs.get())

        def countdown(times):
            if times >= 0:
                minute, second = divmod(times, 60)
                hour, minute = divmod(minute, 60)
                # a, b = divmod(c, d) -> a = c//d, b = c%d

                hrs.set(f"{hour:02}")
                mins.set(f"{minute:02}")
                secs.set(f"{second:02}")

                t.after(1000, countdown, times - 1)
            else:
                def repeat_beep(count):
                    if count > 0:
                        winsound.Beep(2000, 400) # frequency=2000Hz, duration=400ms
                        t.after(500, repeat_beep, count - 1) #500ms between beeps
                repeat_beep(5)

        countdown(total_seconds)
    except Exception as e:
        print("Error:", e)

def set_25_min():
    hrs.set("00")
    mins.set("25")
    secs.set("00")

def reset():
    hrs.set("00")
    mins.set("00")
    secs.set("00")

def add_5_min():
    try:
        current_total = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(secs.get())
        new_total = current_total + 300 # 5 minutes = 300 seconds

        minute, second = divmod(new_total, 60)
        hour, minute = divmod(minute, 60)

        hrs.set(f"{hour:02}")
        mins.set(f"{minute:02}")
        secs.set(f"{second:02}")
    except Exception as e:
        print("Error adding 5 minutes:", e)

button1 = Button(t, text="25.00", bg="black", bd=0, fg="white", width=5, height=2, font="arial 20", command=set_25_min)
button1.place(x=160, y=250)

button2 = Button(t, text="+5 min", bg="black", bd=0, fg="white", width=5, height=2, font="arial 20", command=add_5_min)
button2.place(x=160, y=320)

button3 = Button(t, text="reset", bg="black", bd=0, fg="white", width=5, height=2, font="arial 20", command=reset)
button3.place(x=160, y=390)

button = Button(t, text="Start", bg="red", bd=0, fg="white", width=20, height=2, font="arial 10 bold", command=timer)
button.pack(padx=5, pady=40, side=BOTTOM)

t.mainloop()


"""
simple cmd timer ::
import time
def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
    print("time's up")
t = input("Enter the time : ")
countdown(int(t))
"""

