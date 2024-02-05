import tkinter as tk
from coin import coin
import math
from PIL import Image, ImageTk
from scipy.stats import binom
from tkinter import messagebox

class app(tk.Tk):
    def __init__(self):
        super().__init__()
        """Just kinda choosing some default values, 16 is like the most you can fit in the window on my computer"""
        self.numCoins = 16
        self.probHeads = 0.5
        self.makeCoins()
        self.numLabel = tk.Label(master = self, text = "# of coins (max 16): ")
        self.numEntry = tk.Entry(master = self)
        self.probLabel = tk.Label(master = self, text = "probability of heads: ")
        self.probEntry = tk.Entry(master = self)
        self.flipButton = tk.Button(master = self, text = "Flip!", command = self.flipCoins, bg ="green")
        self.eheads = tk.Label(master = self, text = "E(# of heads): \n 8")
        self.numHeadsLabel = tk.Label(master = self, text = "Observed # of heads: \n -")
        self.prob_of_flip = tk.Label(master = self, text = "Chance of last flip: \n -")
        self.how_to_use = tk.Button(master = self, text = "How To Use", bg = "orange", command = self.instructionsDialog)
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
        self.how_to_use.grid(row = 100, column = 0, columnspan= 101, sticky="nsew")
    
    """build updating the labels into this function to make counting easy"""
    def flipCoins(self):
        counter = 0
        for index, coin in enumerate(self.coins):
            coin.destroy()
            coin.flip()
            if(coin.getState() == 'heads'):
                counter += 1
        self.drawGrid()
        self.flipUpdate(counter)
    
    def getImage(self, state):
        if state == "heads":
            return heads
        else:
            return tails
    
    def clearGrid(self):
        for coin in self.coins:
            coin.destroy()

    def flipUpdate(self, number):
        self.numHeadsLabel["text"] = "Observed # of heads: \n" + str(number)
        self.prob_of_flip["text"] = "Chance of last flip: \n" + str(binom.pmf(number, self.numCoins, self.probHeads))

    def resizeUpdate(self):
        self.numHeadsLabel["text"] = "Observed # of heads: \n" + "-"
        self.prob_of_flip["text"] = "Chance of last flip: \n" + "-"
        self.eheads["text"] = "E(# of heads): \n" + str(self.formatFloat(float(float(self.numCoins) * self.probHeads)))

    def formatFloat(self, input):
        if(input % 1 == 0):
            return int(input)
        return input
    
    def instructionsDialog(self):
        text = "Enter the number of coins you would like to simulate and the probability of heads you would like for the simulation."
        text += "\n\n\nYou can update these values at any time by pressing enter. Press the flip button to simulate a flip."
        messagebox.showinfo(title = "Instructions", message = text)
        
    def hitReturn(self, event):
        """start by checking inputs"""
        intCheck = self.notValidInt(self.numEntry.get())
        floatCheck = self.notValidFloat(self.probEntry.get())
        if(intCheck[0] or floatCheck[0]):
            if(intCheck[0]):
                messagebox.showerror("Invalid Input", intCheck[1])
            else:
                messagebox.showerror("Invalid Input", floatCheck[1])
        else:
            self.clearGrid()
            self.setNumCoins(int(self.numEntry.get()))
            self.setProbHeads(float(self.probEntry.get()))
            self.makeCoins()
            self.resizeUpdate()
            self.drawGrid()
    
    def notValidInt(self, entry): 
        if(not entry.isdigit()):
            self.numEntry.delete(0, 'end')
            self.numEntry.insert(0, str(self.numCoins))
            return [True, "# of coins entry is not an int"]
        elif(int(entry) < 1 or int(entry) > 16):
            self.numEntry.delete(0, 'end')
            self.numEntry.insert(0, str(self.numCoins))
            return [True, "# of coins entry is not within range bounds"]
        return [False, ""]

    def notValidFloat(self, entry): 
        if entry.count('.') < 2 and entry.replace('.','', 1).isdigit():
            if(float(entry) > 1 or float(entry) < 0):
                self.probEntry.delete(0, 'end')
                self.probEntry.insert(0, str(self.probHeads))
                return [True, "probability entry is not between 0 and 1"]
            return [False, ""]
        else: 
            self.probEntry.delete(0, 'end')
            self.probEntry.insert(0, str(self.probHeads))
            return [True, "probability entry is not a float"]


        
    

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