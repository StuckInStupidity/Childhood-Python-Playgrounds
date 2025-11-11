import tkinter
from tkinter import messagebox
import time

canvas_width = 750
canvas_height = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvas_width, height=canvas_height, bg="blue")
canvas.pack()
racket = canvas.create_rectangle(0, 0, 40,10, fill="dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill="deep pink")
window_open = True
score = 0
number_bound = 0

def main_loop():
    while window_open == True:
        move_racket()
        move_ball()
        window.update()
        time.sleep(0.02)
        if window_open == True:
            verify_game_over()

left_press = 0
right_press = 0

def when_button_press(event):
    global left_press, right_press
    if event.keysym == "Left":
        left_press = 1
    if event.keysym == "Right":
        right_press = 1

def when_button_release(event):
    global left_press, right_press
    if event.keysym == "Left":
        left_press = 0
    if event.keysym == "Right":
        right_press = 0

speed_racket = 6

def move_racket():
    mouv_racket = speed_racket*right_press - speed_racket*left_press
    (left_racket, up_racket, right_racket, down_racket) = canvas.coords(racket)
    if ((left_racket > 0 or mouv_racket > 0) and (right_racket < canvas_width or mouv_racket < 0)):
        canvas.move(racket, mouv_racket, 0)

move_ball_x = 4
move_ball_y = -4
def_up_racket = canvas_height-40
def_down_racket = canvas_height-30

def move_ball():
    global move_ball_x, move_ball_y, score, number_bound, speed_racket
    (left_ball, up_ball, right_ball, down_ball) = canvas.coords(ball)
    if move_ball_x > 0 and right_ball > canvas_width:
        move_ball_x = -move_ball_x
    if move_ball_x < 0 and left_ball < 0:
        move_ball_x = -move_ball_x
    if move_ball_y < 0 and up_ball < 0:
        move_ball_y = -move_ball_y
    if move_ball_y > 0 and down_ball > def_up_racket and down_ball < def_down_racket:
        (left_racket, up_racket, right_racket, down_racket) = canvas.coords(racket)
        if (move_ball_x > 0 and (right_ball+move_ball_x > left_racket and left_ball < right_racket) or move_ball_x < 0 and (right_ball > left_racket and left_ball+move_ball_x < right_racket)):
            move_ball_y = -move_ball_y
            score += 1
            number_bound += 1
            if number_bound == 4:
                number_bound = 0
                speed_racket += 1
                if move_ball_x > 0:
                    move_ball_x +=1
                else:
                    move_ball_x -= 1
                move_ball_y -= 1
    canvas.move(ball, move_ball_x, move_ball_y)

def verify_game_over():
    (left_ball, up_ball, right_ball, down_ball) = canvas.coords(ball)
    if up_ball > canvas_height:
        print("Ton score : " + str(score))
        replay = tkinter.messagebox.askyesno(message="Veux-tu rejouer?")
        if replay == True:
            reset()
        else:
            close()

def close():
    global window_open
    window_open = False
    window.destroy()

def reset():
    global score, number_bound, speed_racket
    global left_press, right_press
    global move_ball_x, move_ball_y
    left_press = 0
    right_press = 0
    move_ball_x = 4
    move_ball_y = -4
    canvas.coords(racket, 10, def_up_racket, 50, def_down_racket)
    canvas.coords(ball, 20, def_up_racket-10, 30, def_up_racket)
    score = 0
    number_bound = 0
    speed_racket = 6

window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", when_button_press)
window.bind("<KeyRelease>", when_button_release)

reset()
main_loop()
