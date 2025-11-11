import tkinter
import random

game_over = False
score = 0
squares_to_verify = 0

def play_deminer():
    global window
    create_field_mined(field_mined)
    window = tkinter.Tk()
    configuration_window(window)
    window.mainloop()

field_mined = []

def create_field_mined(field_mined):
    global squares_to_verify
    for roww in range(0,10):
        list_ranged = []
        for columnn in range(0,10):
            if random.randint(1,100) < 20:
                list_ranged.append(1)
            else:
                list_ranged.append(0)
                squares_to_verify += 1
        field_mined.append(list_ranged)
    print_field(field_mined)

def print_field(field_mined):
    for list_ranged in field_mined:
        print(list_ranged)

def configuration_window(window):
    window.state('zoomed')
    for number_roww, list_ranged in enumerate(field_mined):
        for number_columnn, enter_columned in enumerate(list_ranged):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text="    ", bg = "darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text="    ", bg = "green")
            else:
                square = tkinter.Label(window, text="    ", bg = "lightgreen")
            square.grid(row = number_roww, column = number_columnn, sticky="nsew")
            square.bind("<Button-1>", when_press)

    for i in range(len(field_mined)):
        window.grid_rowconfigure(i, weight=1)
        window.grid_columnconfigure(i, weight=1)

def when_press(event):
    global score
    global game_over
    global squares_to_verify
    square = event.widget
    roww = int(square.grid_info()["row"])
    columnn = int(square.grid_info()["column"])
    text_current = square.cget("text")
    if game_over == False:
        if field_mined[roww][columnn] == 1:
            game_over = True
            square.config(bg = "red")
            print("Game Over! Tu as touché une bombe.")
            print("Ton score : ", score)
        elif text_current == "    ":
            square.config(bg = "brown")
            total_bomb = 0
            if roww < 9:
                if field_mined[roww+1][columnn] == 1:
                    total_bomb += 1
            if roww > 0:
                if field_mined[roww-1][columnn] == 1:
                    total_bomb += 1
            if columnn > 0:
                if field_mined[roww][columnn-1] == 1:
                    total_bomb += 1
            if columnn < 9:
                if field_mined[roww][columnn+1] == 1:
                    total_bomb += 1
            if roww > 0 and columnn > 0:
                if field_mined[roww-1][columnn-1] == 1:
                    total_bomb += 1
            if roww < 9 and columnn > 0:
                if field_mined[roww+1][columnn-1] == 1:
                    total_bomb += 1
            if roww > 0 and columnn < 9:
                if field_mined[roww-1][columnn+1] == 1:
                    total_bomb += 1
            if roww < 9 and columnn < 9:
                if field_mined[roww+1][columnn+1] == 1:
                    total_bomb += 1
            square.config(text = " " + str(total_bomb) + " ")
            squares_to_verify -= 1
            score +=1
            if squares_to_verify == 0:
                game_over = True
                window.destroy()
                print("You won! Tu as trouvé tous les carrés non minés.")
                print("Ton score : ", score)

play_deminer()