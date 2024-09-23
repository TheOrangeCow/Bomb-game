import tkinter
import random

def start_game():
    global window, score, squaresToClear, gameOver, bombfield
    gameOver = False
    score = 0
    squaresToClear = 0
    bombfield = create_bombfield()
    window = tkinter.Tk()
    layout_window(window, bombfield)
    window.mainloop()
    #printfield(bombfield)

def play_bombdodger():
    global window, score, squaresToClear, gameOver, bombfield
    window = None
    score = 0
    squaresToClear = 0
    gameOver = False
    bombfield = []
    start_game()

def create_bombfield():
    bombfield = []
    global squaresToClear
    for row in range(0, 10):
        rowList = []
        for column in range(0, 10):
            if random.randint(1, 100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear += 1
        bombfield.append(rowList)
    return bombfield

def layout_window(window, bombfield):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text="    ", bg="darkgreen")
            elif random.randint(1, 100) > 75:
                square = tkinter.Label(window, text="    ", bg="seagreen")
            else:
                square = tkinter.Label(window, text="    ", bg="green")
            square.grid(row=rowNumber, column=columnNumber)
            square.bind("<Button-1>", on_click)

def on_click(event):
    global score, squaresToClear, gameOver, bombfield
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if bombfield[row][column] == 1:
            gameOver = True
            square.config(bg="red")
            print("Game over! You hit a bomb!")
            print("Your score was:", score)
        elif currentText.strip() == "":
            square.config(bg="brown")
            totalbombs = 0
            for r in range(max(0, row - 1), min(10, row + 2)):
                for c in range(max(0, column - 1), min(10, column + 2)):
                    totalbombs += bombfield[r][c]
            square.config(text=" " + str(totalbombs) + " ")
            squaresToClear -= 1
            score += 1
            if squaresToClear == 0:
                gameOver = True
                print("Well done! you found all the safe squares")
                print("Your score was:", score)

def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)

start_game()
