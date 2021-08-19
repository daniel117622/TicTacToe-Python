from tkinter import *

xturn = 1 # 1 IS TRUE AND 0 IS FALSE. -1 IS Game over

def box_mouseover(event):
    pass

def box_onleave(event):
    pass

def box_click(event,self,game):
    global xturn

    caller = event.widget
    if caller["text"] == " " and xturn == 1:
        caller.configure(text = "X")
        self.turn.set("O")
        xturn = False
    elif caller["text"] == " " and xturn == 0:
        caller.configure(text = "O")
        self.turn.set("X")
        xturn = True
    else : 
        pass

    # check for wins.
    for i in range(3):
        #Checks for wins horizontally
        if game[0+3*i]["text"] == "X" and game[1+3*i]["text"] == "X" and game[2+3*i]["text"] == "X":
            game[0+3*i].configure(background = "green")
            game[1+3*i].configure(background = "green")
            game[2+3*i].configure(background = "green")
            xturn = -1
        if game[0+3*i]["text"] == "O" and game[1+3*i]["text"] == "O" and game[2+3*i]["text"] == "O":
            game[0+3*i].configure(background = "green")
            game[1+3*i].configure(background = "green")
            game[2+3*i].configure(background = "green") 
            xturn = -1
    for i in range(3):
        if game[0+i]["text"] == "X" and game[3+i]["text"] == "X" and game[6+i]["text"] == "X":
            game[0+i].configure(background = "green")
            game[3+i].configure(background = "green")
            game[6+i].configure(background = "green")            
            xturn = -1
        if game[0+i]["text"] == "O" and game[3+i]["text"] == "O" and game[6+i]["text"] == "O":
            game[0+i].configure(background = "green")
            game[3+i].configure(background = "green")
            game[6+i].configure(background = "green")                
            xturn = -1

        if game[0]["text"] == "X" and game[4]["text"] == "X" and game[8]["text"] == "X":
            game[0].configure(background = "green")
            game[4].configure(background = "green")
            game[8].configure(background = "green")
            xturn = -1
        if game[0]["text"] == "O" and game[4]["text"] == "O" and game[8]["text"] == "O":
            game[0].configure(background = "green")
            game[4].configure(background = "green")
            game[8].configure(background = "green")
            xturn = -1 

        if game[2]["text"] == "X" and game[4]["text"] == "X" and game[6]["text"] == "X":
            game[2].configure(background = "green")
            game[4].configure(background = "green")
            game[6].configure(background = "green")
            xturn = -1
        if game[2]["text"] == "O" and game[4]["text"] == "O" and game[6]["text"] == "O":
            game[2].configure(background = "green")
            game[4].configure(background = "green")
            game[6].configure(background = "green")
            xturn = -1                                         
    

def restart_button(event,game):
    global xturn
    print("Restarting...")
    for i in range(9):
        game[i].configure(background = "white")
        game[i].configure(text = " ")
    xturn = 1