import tkinter as tk
from coin import coin
import math
from PIL import Image, ImageTk

"""
Write comments so you can come back to stuff ya dum-dum
"""
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        """Just kinda choosing some default values"""
        self.numCoins = 16
        self.probHeads = 0.5
        self.makeCoins()
        self.numLabel = tk.Label(master = self, text = "# of coins (max 100): ")
        self.numEntry = tk.Entry(master = self)
        self.probLabel = tk.Label(master = self, text = "probability of heads: ")
        self.probEntry = tk.Entry(master = self)
        self.flipButton = tk.Button(master = self, text = "Flip!", command = self.flipCoins, bg ="green")
        self.eheads = tk.Label(master = self, text = "E(# of heads): \n 8")
        self.numHeadsLabel = tk.Label(master = self, text = "Observed # of heads: \n -")
        self.prob_of_flip = tk.Label(master = self, text = "Chance of last flip: \n -")
        self.bind('<Return>', self.hitReturn)

    def makeCoins(self):
        self.coins = [None] * self.numCoins
        for index in range(self.numCoins):
            self.coins[index] = coin(self.probHeads)

    def setNumCoins(self, quantity):
        self.numCoins = quantity

    def setProbHeads(self, prob):
        self.probHeads = prob

    def drawGrid(self):
        for index, coin in enumerate(self.coins):
                coin.makeLabel(index, window)

    def drawLabels(self):
        self.numLabel.grid(row = 0, column = 0)
        self.numEntry.grid(row = 0, column = 1)
        self.numEntry.insert(0, str(self.numCoins))
        self.probLabel.grid(row = 0, column = 2)
        self.probEntry.grid(row = 0, column = 3)
        self.probEntry.insert(0, str(self.probHeads))
        self.flipButton.grid(row = 0, column = 100, sticky = "nsew")
        self.eheads.grid(row = 1, column = 100)
        self.numHeadsLabel.grid(row = 2, column = 100)
        self.prob_of_flip.grid(row = 3, column = 100)
    
    def flipCoins(self):
        for index, coin in enumerate(self.coins):
            coin.flip()
        self.drawGrid()
    
    def getImage(self, state):
        if state == "heads":
            return heads
        else:
            return tails
    
    def clearGrid(self):
        for coin in self.coins:
            coin.destroy()
        
    def hitReturn(self, event):
        """
        you're gonna have to check if these inputs are valid
            """
        self.setNumCoins(int(self.numEntry.get()))
        self.setProbHeads(float(self.probEntry.get()))
        self.clearGrid()
        self.makeCoins()
        self.drawGrid()


        
    

window = app()
window.title("Coin Flip Simulator")

headsImage = Image.open("heads.jpg")
newheadsImage = headsImage.resize((150, 150))
heads = ImageTk.PhotoImage(newheadsImage)

tailsImage = Image.open("tails.jpg")
newtailsImage = tailsImage.resize((150, 150))
tails = ImageTk.PhotoImage(newtailsImage)

window.rowconfigure(100, minsize = 100, weight = 1)
window.columnconfigure(100, minsize = 100, weight = 1)
window.drawLabels()
window.makeCoins()
window.drawGrid()

window.mainloop()