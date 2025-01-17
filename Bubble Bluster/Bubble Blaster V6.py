from tkinter import *
from random import randint
from math import sqrt
from time import sleep, time

# Shchrtt 1
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='blue')
c.pack()

# Schritt 2
schiff_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
schiff_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SCHIFF_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(schiff_id, MID_X, MID_Y)
c.move(schiff_id2, MID_X, MID_Y)

# Schritt 3
SCHIFF_GESCHW = 10


def schiff_beweg(event):
    if event.keysym == 'Up':
        c.move(schiff_id, 0, -SCHIFF_GESCHW)
        c.move(schiff_id2, 0, -SCHIFF_GESCHW)
    elif event.keysym == 'Down':
        c.move(schiff_id, 0, SCHIFF_GESCHW)
        c.move(schiff_id2, 0, SCHIFF_GESCHW)
    elif event.keysym == 'Left':
        c.move(schiff_id, -SCHIFF_GESCHW, 0)
        c.move(schiff_id2, -SCHIFF_GESCHW, 0)
    elif event.keysym == 'Right':
        c.move(schiff_id, SCHIFF_GESCHW, 0)
        c.move(schiff_id2, SCHIFF_GESCHW, 0)


c.bind_all('<Key>', schiff_beweg)

# Schtitt 4
bub_id = list()
bub_r = list()
bub_geschw = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_GESCHW = 10
GAP = 100


def erstelle_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_geschw.append(randint(1, MAX_BUB_GESCHW))


# Schritt 7
def hole_koord(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


# Schritt 8
def loesche_bubble(i):
    del bub_r[i]
    del bub_geschw[i]
    c.delete(bub_id[i])
    del bub_id[i]


# Schritt 9
def entf_bubbles():
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = hole_koord(bub_id[i])
        if x < -GAP:
            loesche_bubble(i)


# Schritt 5
def bewege_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_geschw[i], 0)


# Schritt 11
def distanz(id1, id2):
    x1, y1 = hole_koord(id1)
    x2, y2 = hole_koord(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Schritt 14
c.create_text(50, 30, text='ZEIT', fill='white')
c.create_text(150, 30, text='PUNKTE', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')


def zeige_punkte(score):
    c.itemconfig(score_text, text=str(score))


def zeige_zeit(time_left):
    c.itemconfig(time_text, text=str(time_left))


# Schritt 12
def kollision():
    points = 0
    for bub in range(len(bub_id) - 1, -1, -1):
        if distanz(schiff_id2, bub_id[bub]) < (SCHIFF_R + bub_r[bub]):
            points += (bub_r[bub] + bub_geschw[bub])
            loesche_bubble(bub)
    return points


# Schritt 15
BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
ende = time() + TIME_LIMIT
# Schritt 6, 10, 13, 16
# # HAUPTSCHLEIFE
while time() < ende:
    if randint(1, BUB_CHANCE) == 1:
        erstelle_bubble()
    bewege_bubbles()
    entf_bubbles()
    score += kollision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        ende += TIME_LIMIT
    zeige_punkte(score)
    zeige_zeit(int(ende - time()))
    window.update()
    sleep(0.01)

#Schritt 17
c.create_text(MID_X, MID_Y, \
              text='GAME OVER', fill='white', font=('Helvetica', 30))
c.create_text(MID_X, MID_Y + 30, \
              text='Punkte: ' + str(score), fill='white')
c.create_text(MID_X, MID_Y + 45, \
              text='Bonus-Zeit: ' + str(bonus * TIME_LIMIT), fill='white')






# Github Bubble Blaster
# importing necessary libraries for this program
from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

# creates the game window
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()
# creates ship sprite
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
# unified variable for ship speed
SHIP_SPD = 10


# programs the ship movement
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif event.keysym == 'Right':
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)


# implements movement functions to ship sprite
c.bind_all('<Key>', move_ship)

# Initializes the bubble attributes
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100


# code to spawn bubbles
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


# defines bubble movement
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)


def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]


def clean_up_bubs():
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)


def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def collision():
    points = 0
    for bub in range(len(bub_id) - 1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points


c.create_text(50, 30, text='TIME', fill='white')
c.create_text(150, 30, text='SCORE', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')


def show_score(score):
    c.itemconfig(score_text, text=str(score))


def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


BUB_CHANCE = 10
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT

# main game loop
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

c.unbind_all('<Key>')
c.delete(ship_id)
c.delete(ship_id2)

c.create_text(MID_X, MID_Y,
              text='GAME OVER', fill='white', font=('Helvetica', 30))
c.create_text(MID_X, MID_Y + 30,
              text='Score: ' + str(score), fill='white')
c.create_text(MID_X, MID_Y + 45,
              text='Bonus time: ' + str(bonus * TIME_LIMIT), fill='white')

window.mainloop()