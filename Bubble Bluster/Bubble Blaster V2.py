from tkinter import *
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

window.mainloop()
