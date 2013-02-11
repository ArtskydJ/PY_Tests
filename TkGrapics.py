from tkinter import *
def turnRed(self, event):
    event.widget["activeforeground"] = "red"

button.bind("<Enter>", self.turnRed)
