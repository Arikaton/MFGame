from tkinter import *
from random import choice
import time

WIDTH = 900
HEIGHT = 600

x = 30
y = 30

K_WIDTH = WIDTH // x
K_HEIGHT = HEIGHT // y

X_SPEED = 0
Y_SPEED = 0

move = 'right'

time1 = time.time()

root = Tk()
root.title("Лабиринт")

walk = 0

lvl1 = [[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]

player1 = [(0, 0), (0, 19), (10, 22), (13, 15), (19, 25), (29, 0)]
exit1 = [(2, 26), (12, 6), (23, 0), (24, 15), (29, 24), ]

player1 = choice(player1)
exit1 = choice(exit1)

lvl1[player1[0]][player1[1]] = 2
lvl1[exit1[0]][exit1[1]] = 3


def paint(x, y):
    global player
    for i in range(x):
        for j in range(y):
            if lvl1[i][j]:
                c.create_rectangle(j * K_WIDTH, i * K_HEIGHT, (j + 1) * K_WIDTH, (i + 1) * K_HEIGHT, fill='black')
            if lvl1[i][j] == 2:
                c.create_rectangle(j * K_WIDTH, i * K_HEIGHT, (j + 1) * K_WIDTH, (i + 1) * K_HEIGHT, fill='white')
                player = c.create_rectangle(j * K_WIDTH, i * K_HEIGHT, (j + 1) * K_WIDTH, (i + 1) * K_HEIGHT,
                                            fill='red')
                POS = [i, j]
            if lvl1[i][j] == 3:
                exit = c.create_rectangle(j * K_WIDTH, i * K_HEIGHT, (j + 1) * K_WIDTH, (i + 1) * K_HEIGHT,
                                          fill='green')
                POSE = [i, j]
    return POS, POSE


c = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
for i in range(0, WIDTH, K_WIDTH):
    c.create_line(i, 0, i, HEIGHT, fill='black')
for i in range(0, HEIGHT, K_HEIGHT):
    c.create_line(0, i, WIDTH, i, fill='black')
pos, exit = paint(x, y)
c.pack()

c.focus_set()


def move_player(event):
    global pos, lvl1, walk
    i, j = pos[0], pos[1]
    if event.keysym == 'Up':
        if lvl1[i - 1][j] != 1:
            c.move(player, 0, -K_HEIGHT)
            pos[0] = i - 1
            walk += 1
    if event.keysym == 'Down':
        if lvl1[i + 1][j] != 1:
            c.move(player, 0, K_HEIGHT)
            pos[0] = i + 1
            walk += 1
    if event.keysym == "Left":
        if lvl1[pos[0]][pos[1] - 1] != 1:
            c.move(player, -K_WIDTH, 0)
            pos[1] -= 1
            walk += 1
    if event.keysym == 'Right':
        if lvl1[pos[0]][pos[1] + 1] != 1:
            c.move(player, K_WIDTH, 0)
            pos[1] += 1
            walk += 1
    if pos[0] == exit[0] and pos[1] == exit[1]:
        c.create_text(WIDTH / 2, HEIGHT / 2,
                      text=f"Вы выиграли!\nКол-во шагов {walk}\nвремя {round(time.time() - time1, 2)} секунд",
                      font='Arial 50',
                      fill='red')


def auto():
    global walk, move, pos
    right = lvl1[pos[0]][pos[1]+1]
    left = lvl1[pos[0]][pos[1]-1]
    up = lvl1[pos[0]-1][pos[1]]
    down = lvl1[pos[0]+1][pos[1]]
    if pos[0] != exit[0] and pos[1] != exit[1]:
        if move == 'right':
            if right == 0 and down == 1 and pos[1] != 30:
                c.move(player, K_WIDTH, 0)
                pos[1] += 1
            else:
                if down == 0 and pos[0] != 30:
                    c.move(player, 0, K_HEIGHT)
                    move = 'down'
                    pos[0] += 1
                else:
                    c.move(player, 0, -K_HEIGHT)
                    move = 'up'
                    pos[0] -= 1
        if move == 'down':
            if left == 1 and down == 0 and pos[0] != 30:
                c.move(player, 0, K_HEIGHT)
                pos[0] += 1
            else:
                if left == 0 and pos[1] != 0:
                    c.move(player, -K_WIDTH, 0)
                    move = 'left'
                    pos[1] -= 1
                else:
                    c.move(player, K_WIDTH, 0)
                    move = 'right'
                    pos[1] += 1


    root.after(200, auto)


c.bind('<KeyPress>', move_player)

quit = Button(root,
              text="Выход",
              command=quit)
quit.pack()

button = Button(text='пройти автоматически',
                command=auto)
button.pack()

root.mainloop()
