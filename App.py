from tkinter import *
from widgetfunctions import *

class App(Tk):
    def __init__(self):

        super().__init__()
        self.geometry("500x500")
        self.turn = StringVar()
        self.turn.set("X")

        self.rowconfigure(0,weight = 1)
        self.rowconfigure(1,weight = 5)

        self.columnconfigure(0,weight = 1)
        self.columnconfigure(1,weight = 3)
        self.columnconfigure(2,weight = 1)
        
        self.createwidgets()



    def createwidgets(self):
        
        lbl_turn = Label(self,textvariable=self.turn,font = ("Arial",24),borderwidth=0,relief=SOLID,width=5)
        lbl_restart = Label(self,text = "Restart",font = ("Arial",24))

        lbl_turn.grid(row=0,column=0,sticky="nswe")
        lbl_restart.grid(row=0,column=2,sticky="nswe")

        frm_game = Frame(self,borderwidth=1,relief=SOLID)
        #Configure the game frame to be 3 by 3 to hold the game
        for i in range(0,3):
            frm_game.rowconfigure(i,weight=1)
            frm_game.columnconfigure(i,weight=1)
        #Grid fills entire gamespace
        frm_game.grid(row=1,column=0,columnspan=3,sticky="nswe")
        
        #This holds all the boxes objects
        game_boxes = []

        #Positioning boxes in frm_game and creating them
        for i in range(0,3):
            for j in range(0,3):
                lbl = Label(frm_game,text=" ",background="white",borderwidth=3,relief=SOLID,font = ("Arial",24),width=20)
                lbl.grid(row = i,column = j,sticky="nsew")
                game_boxes.append(lbl)

        #Binding actions to every box
        for i in range(len(game_boxes)):
            game_boxes[i].bind("<Enter>",  box_mouseover)
            game_boxes[i].bind("<Leave>", box_onleave)
            game_boxes[i].bind("<Button-1>",lambda e , self = self , game = game_boxes: box_click(e,self,game)) # We pass self to modify a game variable, and we pass game to modify the gameboxes
        
        #Binding the restart button.
        lbl_restart.bind("<Button-1>",lambda e , game = game_boxes: restart_button(e,game)) #This will restart the game boxes


if __name__ == "__main__":
    app = App()
    app.mainloop()
