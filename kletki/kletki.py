from tkinter import *
from random import randint

class game:
    def __init__(self, name):
        self.sq = 0
        self.name = name
        self.frame = Frame(root)
        self.label = Label(self.frame, text=name)
        self.Button = Button(self.frame, text=name, command=self.step)
        self.square = Button(self.frame, text='площадь', command=self.end)
        self.frame.pack(side='left')
        self.label.pack()
        self.Button.pack()
        self.square.pack()

    def end(self):
        self.label['text'] = self.sq

    def step(self):
        a, b = randint(1, 6), randint(1, 6)
        self.sq += a * b
        self.label['text'] = a, b

root = Tk()
root.title('Game')
alina = game('Alina')
stas = game('Stas')


root.mainloop()