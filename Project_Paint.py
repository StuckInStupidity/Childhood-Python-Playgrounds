import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=500, bg="white")
canvas.pack()

lastX, lastY = 0,0
color = "black"

def recorded_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

def when_press(event):
    recorded_position(event)

def when_move(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill = color, width = 3)
    recorded_position(event)

canvas.bind("<Button-1>",when_press)
canvas.bind("<B1-Motion>", when_move)

red_id = canvas.create_rectangle(10, 10, 30, 30, fill="red")
orange_id = canvas.create_rectangle(10, 35, 30, 55, fill="orange")
yellow_id = canvas.create_rectangle(10, 60, 30, 80, fill="yellow")
green_id = canvas.create_rectangle(10, 85, 30, 105, fill="green")
blue_id = canvas.create_rectangle(10, 110, 30, 130, fill="blue")
purple_id = canvas.create_rectangle(10, 135, 30, 155, fill="purple")
pink_id = canvas.create_rectangle(10, 160, 30, 180, fill="pink")
white_id = canvas.create_rectangle(10, 185, 30, 205, fill="white")
black_id = canvas.create_rectangle(10, 210, 30, 230, fill="black")

def define_color_red(event):
    global color
    color="red"
def define_color_orange(event):
    global color
    color="orange"
def define_color_yellow(event):
    global color
    color="yellow"
def define_color_green(event):
    global color
    color="green"
def define_color_blue(event):
    global color
    color="blue"
def define_color_purple(event):
    global color
    color="purple"
def define_color_pink(event):
    global color
    color="pink"
def define_color_white(event):
    global color
    color="white"
def define_color_black(event):
    global color
    color="black"
    
canvas.tag_bind(red_id, "<Button-1>", define_color_red)
canvas.tag_bind(orange_id, "<Button-1>", define_color_orange)
canvas.tag_bind(yellow_id, "<Button-1>", define_color_yellow)
canvas.tag_bind(green_id, "<Button-1>", define_color_green)
canvas.tag_bind(blue_id, "<Button-1>", define_color_blue)
canvas.tag_bind(purple_id, "<Button-1>", define_color_purple)
canvas.tag_bind(pink_id, "<Button-1>", define_color_pink)
canvas.tag_bind(white_id, "<Button-1>", define_color_white)
canvas.tag_bind(black_id, "<Button-1>", define_color_black)

window.mainloop()
