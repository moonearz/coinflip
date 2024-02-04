import tkinter as tk
import random
from PIL import Image, ImageTk
import math

class coin():
    def __init__(self):
        self.probHeads = 0.5
        self.currentState = "heads"

    def __init__(self, prob):
        self.probHeads = prob
        self.currentState = "heads"


    def getState(self):
        return self.currentState
    
    def makeLabel(self, index, parent):
        numRows = math.sqrt(parent.numCoins)
        img = parent.getImage(self.currentState)
        label = tk.Label(parent, image = img)
        label.grid(row = math.floor(int((index / numRows))) + 1, column = int(index % numRows))

    def flip(self):
        value = random.uniform(0, 1)
        if(value > self.probHeads):
            self.currentState = "tails"
        else:
            self.currentState = "heads"



        