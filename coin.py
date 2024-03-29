import tkinter as tk
import random
from PIL import Image, ImageTk
import math

class coin():
    def __init__(self):
        self.probHeads = 0.5
        self.currentState = "heads"
        self.label = tk.Label()

    def __init__(self, prob):
        self.probHeads = prob
        self.currentState = "heads"


    def getState(self):
        return self.currentState
    
    def makeLabel(self, index, parent):
        numRows = round(math.sqrt(parent.numCoins))
        img = parent.getImage(self.currentState)
        self.label = tk.Label(parent, image = img)
        self.label.grid(row = (int((index / numRows))) + 1, column = int(index % numRows))

    def flip(self):
        value = random.uniform(0, 1)
        if(value > self.probHeads):
            self.currentState = "tails"
        else:
            self.currentState = "heads"

    def destroy(self):
        self.label.destroy()


        