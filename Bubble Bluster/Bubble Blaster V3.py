from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

schiff_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
schiff_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SCHIFF_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT /2
c.move(schiff_id, MID_X, MID_Y)
c.move(schiff_id2, MID_X, MID_Y)

SCHIFF_GESCHW = 10 # So weit bewegt sich das U-Boot, wenn eine Taste gedrückt wird.


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

from random import randint

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

def bewege_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_geschw[i], 0)

from time import sleep, time

BUB_CHANCE = 10
# HAUPTSCHLEIFE
while True:
    if randint(1,BUB_CHANCE) == 1:
        erstelle_bubble()
    bewege_bubbles()
    window.update()
    sleep(0.01) 