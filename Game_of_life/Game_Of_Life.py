from tkinter import *
from numpy import copy
#основные переменные
WIDTH = 600
HEIGHT = 600

K_WIDTH = 30
K_HEIGHT = 30

x = WIDTH // K_WIDTH
y = HEIGHT // K_HEIGHT

root = Tk()
root.title('Game_of_life')

c = Canvas(root, width=WIDTH, height=HEIGHT)
c.pack()

array = [[False for i in range(x)] for j in range(y)]
empty = copy(array)


for i in range(0, WIDTH, K_WIDTH):
    c.create_line(i, 0, i, HEIGHT, fill='black')
for i in range(0, HEIGHT, K_HEIGHT):
    c.create_line(0, i, WIDTH, i, fill='black')


def sun(l, a, b):
    su = 0
    if a != x - 1 and b != y - 1:
        for q in [a - 1, a, a + 1]:
            for w in [b - 1, b, b + 1]:
                if l[q][w]:
                    su += 1
    elif a == x - 1 and b != y - 1:
        for q in [a - 1, a, 0]:
            for w in [b - 1, b, b + 1]:
                if l[q][w]:
                    su += 1
    elif a != x - 1 and b == y - 1:
        for q in [a - 1, a, a + 1]:
            for w in [b - 1, b, 0]:
                if l[q][w]:
                    su += 1
    else:
        for q in [a - 1, a, 0]:
            for w in [b - 1, b, 0]:
                if l[q][w]:
                    su += 1
    return su

def nextstep(array1):
    nexta = copy(empty)
    for i in range(x):
        for j in range(y):
            if not array1[i][j]:
                if sun(array1, i, j) == 3:
                    nexta[i][j] = True
                else:
                    nexta[i][j] = False
            if array1[i][j]:
                if (sun(array1, i, j) - 1) == 2:
                    nexta[i][j] = True
                elif sun(array1, i, j) - 1 == 3:
                    nexta[i][j] = True
                else:
                    nexta[i][j] = False
    return nexta

def game(event):
    lego()

def draw(event):
    global array
    i = event.x // K_WIDTH
    j = event.y // K_HEIGHT
    if array[i][j] == False:
        c.create_oval(i * K_WIDTH, j * K_HEIGHT, (i + 1) * K_WIDTH, (j + 1) * K_HEIGHT, fill='black')
        array[i][j] = True
    else:
        c.create_oval(i * K_WIDTH, j * K_HEIGHT, (i + 1) * K_WIDTH, (j + 1) * K_HEIGHT, fill='white')
        array[i][j] = False

but = Button(root,
             text="start",
             width=40,
             height=10,
             bg="white",
             fg="grey")
but.bind('<Button-1>', game)
but.pack()

c.bind("<Button-1>", draw)

def lego():
    global array
    next = nextstep(array)
    for i in range(x):
        for j in range(y):
            if next[i][j] == True:
                c.create_oval(i * K_WIDTH, j * K_HEIGHT, (i + 1) * K_WIDTH, (j + 1) * K_HEIGHT, fill='black')
            else:
                c.create_oval(i * K_WIDTH, j * K_HEIGHT, (i + 1) * K_WIDTH, (j + 1) * K_HEIGHT, fill='white')
    array = copy(next)

    root.after(1000, lego)

root.mainloop()
