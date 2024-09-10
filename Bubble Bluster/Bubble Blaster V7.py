from tkinter import *
from random import randint
from math import sqrt
from time import sleep, time

    
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()


schiff_id4 = c.create_text(15, -15, text='Player')
schiff_id3 = c.create_oval(0, 0, 30, 30, fill='white')
schiff_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
schiff_id2 = c.create_oval(0, 0, 30, 30, outline='red')


SCHIFF_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(schiff_id, MID_X, MID_Y)
c.move(schiff_id2, MID_X, MID_Y)
c.move(schiff_id3, MID_X, MID_Y)
c.move(schiff_id4, MID_X, MID_Y)

SCHIFF_GESCHW = 10


def schiff_beweg(event):
    if event.keysym == 'w':
        c.move(schiff_id4, 0, -SCHIFF_GESCHW)
        c.move(schiff_id3, 0, -SCHIFF_GESCHW)
        c.move(schiff_id, 0, -SCHIFF_GESCHW)
        c.move(schiff_id2, 0, -SCHIFF_GESCHW)
    elif event.keysym == 's':
        c.move(schiff_id4, 0, SCHIFF_GESCHW)
        c.move(schiff_id3, 0, SCHIFF_GESCHW)
        c.move(schiff_id, 0, SCHIFF_GESCHW)
        c.move(schiff_id2, 0, SCHIFF_GESCHW)
    elif event.keysym == 'a':
        c.move(schiff_id4, -SCHIFF_GESCHW, 0)
        c.move(schiff_id3, -SCHIFF_GESCHW, 0)
        c.move(schiff_id, -SCHIFF_GESCHW, 0)
        c.move(schiff_id2, -SCHIFF_GESCHW, 0)
    elif event.keysym == 'd':
        c.move(schiff_id4, SCHIFF_GESCHW, 0)
        c.move(schiff_id3, SCHIFF_GESCHW, 0)
        c.move(schiff_id, SCHIFF_GESCHW, 0)
        c.move(schiff_id2, SCHIFF_GESCHW, 0)


c.bind_all('<Key>', schiff_beweg)

bub_id = list()
bub_r = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
GAP = 100


def erstelle_bubble():
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)

# Schritt 7
def hole_koord(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


# Schritt 8
def loesche_bubble(i):
    del bub_r[i]
    c.delete(bub_id[i])
    del bub_id[i]


# Schritt 9
def entf_bubbles():
    for i in range(len(bub_id) - 1, -1, -1):
        x, y = hole_koord(bub_id[i])
        if x < -GAP:
            loesche_bubble(i)    

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
            points += (bub_r[bub])
            loesche_bubble(bub)
    return points


BUB_CHANCE = 10000
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
ende = time() + TIME_LIMIT
# HAUPTSCHLEIFE
while True:
    if randint(1, BUB_CHANCE) == 1:
        erstelle_bubble()
    entf_bubbles()
    score += kollision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        ende += TIME_LIMIT
    zeige_punkte(score)
    zeige_zeit(int(ende - time()))
    window.update()

