# Für dieses Projekt brauchst du alles, was du bisher gelernt hast.
# Da du ein kompliziertes Spiel programmierst, solltest du Schritt für Schritt vorgehen und regelmässig speichern.
# Beginne jeden neuen Schritt erst, wenn du verstanden hast, wie er zu den vorhergehenden passt.
# Am Ende kannst du das Spiel dann spielen und deinen Freunden vorführen.

#//1.1
# Das Ziel des Spiels:
# Bevor du mit dem Programmieren beginnst, solltest du dir den Gesamtplan des Spiels vorstellen und überlegen, was alles geschehen soll.

# Hier sind die wichtigsten Regeln für unser Spiel:
# Der Spieler steuert ein U-Boot.
# Die Pfeiltasten bewegen das U-Boot.
# Das Zerplatzen von Blasen bringt Punkte.
# Ein Timer wird anfangs auf 30 Sek. gestellt.
# Bei 1000 Punkten erhält man mehr Zeit.
# Das Spiel endet nach ablauf der Zeit.

#//1.2
# Das Spielfenster und das U-Boot erstellen.
# Zuerst erschaffst du die Spielumgebung.
# Öffne ein neues Code-Fenster in IDLE und erstelle mit dem folgenden Code das Hauptfenster für das Spiel und das U-Boot, das vom Spieler gesteuert wird.

#//1.2.1
# Mithilfe der Bibliothek Tkinter erstellst du die fragische Benutzeroberfläche (GUI). 
# Der folgende Code erstellt das Hauptfenster für das Spiel.
from tkinter import *
HEIGHT = 500 # Fenster grösse:
WIDTH = 800
window = Tk()
window.title('Bubble Blaster') # Fenster Name.
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue') # Der Hintergrund(background,"bg=") soll dunkelblau sein.
c.pack()

#//1.2.2
# Das U-Boot wird durch eine einfache Grafik dargestellt.
# Dazu brauchst du einige Zeichenfunktionen von Tkinter.
# Schreibe diesen Code und führe ihn aus.
schiff_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
schiff_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SCHIFF_R = 15 # Der Radius (Grösse) des U-Boots.
MID_X = WIDTH / 2 # Die Variablen "MID_X" und "MID_Y" liefern Koordinaten der Bilschirmmitte.
MID_Y = HEIGHT /2
c.move(schiff_id, MID_X, MID_Y) # Bewegz beide Teile des U-Boots in die Mitte des Bilschirms.
c.move(schiff_id2, MID_X, MID_Y)

#//1.3 
# Das U-Boot steuern:
# Im nächsten Schritt schreibst du den Code, der das U-Boot bewegt, wenn die Pfeiltsten gedrückt werden.
# Der Code definiert eine Funktion, die Ereignisse verarbeitet (Event-Handler).
# Sie prüft, welche Taste gedrückt wurde, und bewegt das U-Boot dann in diese Richtung.

#//1.3.1
# Mit dem folgenden Code wird die Funktion "schiff_beweg" erstellt,-
# die das U-Boot in die richtige Richtung bewegt, wenn der Spieler eine Pfeiltaste drückt.
# Führe den code aus, um zu sehen, wie er funktioniert.

SCHIFF_GESCHW = 10 # So weit bewegt sich das U-Boot, wenn eine Taste gedrückt wird. 


def schiff_beweg(event):
    if event.keysym == 'Up':
        c.move(schiff_id, 0, -SCHIFF_GESCHW) # Bewegt die zwei Teile des U-Boots nach oben, wenn der Aufwärtspfeil gedrückt wird.
        c.move(schiff_id2, 0, -SCHIFF_GESCHW)
    elif event.keysym == 'Down':
        c.move(schiff_id, 0, SCHIFF_GESCHW) # Diese Zeilen werden aktiviert, wenn der Abwärtspfeil gedrückt wird.
        c.move(schiff_id2, 0, SCHIFF_GESCHW)
    elif event.keysym == 'Left':
        c.move(schiff_id, -SCHIFF_GESCHW, 0) # Das U-Boot schwimmt nach links, wenn der Linkspfeil gedrückt wird.
        c.move(schiff_id2, -SCHIFF_GESCHW, 0)
    elif event.keysym == 'Right':
        c.move(schiff_id, SCHIFF_GESCHW, 0) # Bewegt das U-Boot nach rechts, wenn der Rechtspfeil gedrückt wird.
        c.move(schiff_id2, SCHIFF_GESCHW, 0)


c.bind_all('<Key>', schiff_beweg) # Python soll die Funktuion "schiff_beweg" ausführen, wenn eine Taste gedrückt wird.

#//1.4
# Jetzt kommen die Blasen (Bubbles)
# Jetzt erstellst du die Blasen, die der Spieler mit dem U-Boot zerplatzen lassen soll.
# Die Blasen sind unterschiedlich gross und bewegen sich unterschiedlich schnell.

#//1.4.1
# Jede Blase hat eine bestimmte Grösse und eine bestimmte Geschwindigkeit.
# Zudem braucht jede Blase eine ID-Nummer, damit das Programmm sie einzeln identifizieren kann.¨
from random import randint

bub_id = list() 
bub_r = list()# Hier werden drei leere Listen erstellt, in denen ID, Radius(Grösse) und Geschwindigkeit jeder "Bubble" gespeichert werden.
bub_geschw = list()
MIN_BUB_R = 10 # Setzt den Minestwert für den Radius der Blase auf 10 und den Höchstwert auf 30.
MAX_BUB_R = 30
MAX_BUB_GESCHW = 10
GAP = 100

def erstelle_bubble():
    x = WIDTH + GAP # Legt die Position der Blase auf der Leinwand fest.
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R) # Wählt eine Zufällige Grösse für die Blase, die zwischen dem mäglichen Mindest- und Höchstwert liegt.
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')# Diese Zeile erstellt die Form der Blase.
    bub_id.append(id1) # Fügt die ID, den Radius und die Geschwindigkeit der Blase in die drei Listen ein.
    bub_r.append(r)
    bub_geschw.append(randint(1, MAX_BUB_GESCHW))

#//1.4.2
# Bubble-Listen:
# Die Informationen über jede Blase werden in drei Listen gespeichert.
# Anfangs sind sie leer, aber beim Erstellen der Blasen werden Infromationen eingefügt.
# Jede Liste speichert eine andere Information.
# bub_id: speichert die ID-Nummer der Blase, sodass das Programm sie später bewegen kann.
# bub_r: speichert den Radius der Blase.
# bub_geschw: speichert, wie schnell die Blase über den Bildschirm wandert.

#//1.5
# Die "Bubbles" sollen sich bewegen.
# Grösse, ID und Geschwindigkeit der zufällig erzeugten Blasen werden nun in Listen gespeichert.
# Im nächsten Schritt schribst du den Code, mit dem sich die Blasen über den Bildschirm bewegen.

#//1.5.1
# Diese Funktion arbeitet die Liste der Blasen ab und bewegt eine nach der anderen.

def bewege_bubbles():
    for i in range(len(bub_id)): # Arbeitet alle Blasen in der Liste der Reihe nach ab.
        c.move(bub_id[i], -bub_geschw[i], 0) # Bewegt die Blase in ihrer eigenen Geschwindigkeit über den Bildschirm.

#//1.5.2
# Dies wird die Hauptschleife, die während des Spiels laufend weiderholt wird.
# Führe sie einmal probeweise aus!
from time import sleep, time # Importiert die benötigten Funktionen aus der Bibliothek "Time".

BUB_CHANCE = 10
# HAUPTSCHLEIFE
while True:
    if randint(1,BUB_CHANCE) == 1: # Erzeugt eine Zufallszahl zwischen 1 und 10 (Zeile 130).
        erstelle_bubble
    bewege_bubbles() # Führt die Funktion "bewege_bubbles" aus.
    window.update() # Aktualiesiert das Fenster und zeigt die bewegten Blasen nue an.
    sleep(0.01) # Verlangsamt das Spiel, damit der Spieler mitkommt.

#//1.5.3
# Nun erstellst du eine nützliche Funktion, mit deren Hilfe du anhand der ID herausfinden kannst, wo eine bestimmte Blase gerade ist.
# Dieser Code sollte direkt hinter den in Schritt 5 erstellten Zeilen folgen.

def hole_koord(id_num): 
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2 #<--Ermittlet die x-Koordinate des Mittelpunkts der Blase.
    y = (pos[1] + pos[3]) / 2 #<--Ermittlet die y-Koordinate des Mittelpunkts der Blase.
    return x, y

# Blasen aufspüren.
# Die Funktion findet den Mittelpunkt der Blase, indem sie die Mitte der Diagionale durch das umgebende Quadrat errechnet.

#//1.6
# So lässt du Blasen platzen.
# Der Spieler erhält Punkte, wenn er Blasen zerplatzen lässt.
# Das Programm muss also dafür sorgen, dass Blasen vom Bildschirm verschwinden.
# Die folgenden Funktionen bewirken genau das.

#//1.6.1
# Mit dieser Funktion werden Blasen aus dem Spiel entfernt.
# Sie werden aus allen Listen und von der Leinwand gelöscht.
# Dieser Code sollte direkt hinter dem Code folgen, den du in Schritt 7 eingegeben hast.

def loesche_bubble(i): #<-- Die Funktion löscht die Blase mit der ID "i"
     del bub_r[i]
     del bub_geschw[i] #<-- Löscht die Blase aus den Listen für Radius und Geschwindigkeit.
     c.delete(bub_id[i]) #<-- Löscht die Blase von der Leinwand.
     del bub_id[i] #<-- Löscht die Blase aus der ID-Liste.

#//1.6.2
# Hier wird eine Funktion erstellt, die die Blasen löscht, die über den ganzen Bildschirm gewandert sind.
# Dieser Code sollte direkt hinter dem aus Schritt 8 folgen.

def entf_bubbles():
    for i in range(len(bub_id) - 1, -1, -1): #<- Arbeitet sich von hinten durch die Blasen-Liste, damit die "for"-Schleife beim Löschen keine Fehler meldet.
        x, y = hole_koord(bub_id[i]) #<- Ermittelt die Position der Blase.
        if x < -GAP:
            loesche_bubble(i) #<- Verschwindet die Blase vom Bildschirm, wird sie gelöscht. Sie würde sonst das Spiel verlangsamen.

#//1.6.2
# Nun muss die Hauptschleife des Spiels (aus //1.5.2) so aktualisiert werden, dass sie die gerade erstellten Funktionen umschliesst.
# Führe sie probeweise aus, um Fehler auszuschliessen.

# HAUPTSCHLEIFE
while True:
    if randint(1, BUB_CHANCE) == 1: # Erstellt eine neue Blase.
        erstelle_bubble() 
    bewege_bubbles() # Aktualisiert die Positionen aller Blasen.
    entf_bubbles() # Entfernt Blasen, die vom Schirm wandern.
    window.update() # Zeichnet das Fenster mit allen Veränderungen neu.
    sleep(0.01)

#//1.7
# Die Entfernung zwischen Punkten ermitteln.
# In diesem Spiel - wie auch in vielen anderen - muss der Abstand zwischen zwei Gegenständen bekannt sein.
# Hier verwendest du eine bekannte mathematische Formel, mit der der Computer ihn berechnen kann.

#//1.7.1
# Diese Funktion berechnet den Abstand zwischen zwei Objekten.
# Der code muss direkt hinter dem Code aus Schritt 9 folgen.

from math import sqrt # Lädt die Funktion "sqrt" (square root, Quadratwurzel) aus der Bibliothek "math".

def distanz(id1, id2):
    x1, y1 = hole_koord(id1) # Ermittelt die Position des ersten Objekts.
    x2, y2 = hole_koord(id2)  # Ermittelt die Position des zwieten Objekts.
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Liefert die Entfernung zwischen Ihnen.

#//1.7.2
# Die Blasen platzen lasse.
# Für jede geplatzte Blase erhält der Spieler Punkte.
# Je grösser und schneller sie sind, desto mehr Punkte gibt es.
# Der folgende Codeabschnitt errechnet jeweils anhand des Radius (Abstand vom Mittelpunkt zum Rand) einer Blase, wann sie zerplatzt.

# Wenn das U-Boot mit einer Blase zusammenstösst, muss das Programm die Blase platzen lassen und die Punktzahl erhöhen.
# Der folgende Code sollte direkt hinter Schritt 11 folgen.

def kollision():
    points = 0 # Diese Variable verfolgt die Punktzahl.
    for bub in range(len(bub_id) - 1, -1, -1): # Die Schleife arbeitet die gessamte Blasenliste ab (rückwärts, damit beim Löschen keine Fehler gemeldet werden).
        if distanz(schiff_id2, bub_id[bub]) < (SCHIFF_R + bub_r[bub]): # Sucht nach Kollisionen zwischen U-Boot und Blasen.
            points += (bub_r[bub] + bub_geschw[bub]) # Errechnet die Punktzahl für diese spezielle Blase und addiert sie zu "points".
            loesche_bubble(bub) # Löscht die Blase.
    return points # Gibt die Gesamtpuktzahl aus.

#//1.7.3
# Nun muss die Hauptschleife des Spiels so aktualisiert werden, dass sie die gerade erstellten Funktionen einschliesst.
# Denke daran, dass die Reihenfolge wichtig ist: Alles muss an der richtigen Stelle stehen.
# Führe dann den Code aus. Wenn die Blasen auf das U-Boot treffen, müssten sie nun platzen.


BUB_CHANCE = 10
score = 0 # Setzt die Punktzahl beim Start auf null.
# HAUPTSCHLEIFE
while True:
    if randint(1, BUB_CHANCE) == 1: # Erstellt neue Blasen.
        erstelle_bubble
    bewege_bubbles()
    entf_bubbles()
    score += kollision() # Addiert die Punktzahl für diese Blase zur Gesamtpunktzahl.
    print(score) # Zeigt die Punktzahl im Shell-Fenster an. Später sorgst du novh dafür, dass sie ordentlich angezeigt wird.
    window.update()
    sleep(0.01) # Diese Zeile lässt das Spiel fpr eine winzigen Zeitraum pausieren. Probiere ruhig aus, was passiert wenn du sie entfernst.

#//1.8
# Der letzte Feinschliff.
# Die wichtigsten Teile des Spiels funktionieren nun so, wie sie sollen.
# Jetzt musst du nur noch zwei letzte Dinge erledigen:
# Die Punktzahl des Spielers muss richtig angezeigt werden und das Spiel braucht ein Zeitllimit für das Ende, damit es interessant wird.

#//1.8.1
# Gib folgenden Code hinter den Code aus Schritt 12 ein. 
# Er weist den Computer an, die Punktzahl und die verbleibende Spielzeit am Bildaschirm anzuzeigen.

c.create_text(50, 30, text='ZEIT', fill='white') #  Erstellt die Beschrifungen "Zeit" und "Punkte", damit der Spieler weiss, was die Zahlen bedeuten.
c.create_text(150, 30, text='PUNKTE', fill='white')#^
time_text = c.create_text(50, 50, fill='white') # Legt die Punktzahl und die verbleibende Zeit fest.
score_text = c.create_text(150, 50, fill='white')#^

def zeige_punkte(score):
    c.itemconfig(score_text, text=str(score)) # Zeigt die Punktzahl an.


def zeige_zeit(time_left):
    c.itemconfig(time_text, text=str(time_left)) # Zeigt verbleibende Zeit an.

#//1.8.2
# Nun folgen das Zeitlimit und die Punktzahl, bei der der Spieler einen Zeitbonus bekommt.
# Dazu wird auch ein neues Spielende errechnet.
# Dieser Code sollte direkt vor der Hauptschleife stehen.

BUB_CHANCE = 10
TIME_LIMIT = 30 # Das Spiel beginnt mit einem Zeitlimit von 30 Sekunden.
BONUS_SCORE = 1000 # Legt fest, wann das Zeitlimit erhöht wird (wenn der Spieler 1000 Punkte erreicht hat).
score = 0
bonus = 0
ende = time() + TIME_LIMIT # Speichert den Endzeitpunkt in einer Variablen namens "ende".

#//1.8.3
# Aktualisiere die Hauptschleife des Spiels so, dass die neuen Funktionen für Punktzahl und Zeit mit einschliesst.

# HAUPTSCHLEIFE
while time() < ende: # Wiederholt die Hauptschleife, bis das Spiel endet.
    if randint(1, BUB_CHANCE) == 1:
        erstelle_bubble()
    bewege_bubbles()
    entf_bubbles()
    score += kollision()
    if (int(score / BONUS_SCORE)) > bonus: # Errechnet, wann das Zeitlimit verlängert werden muss.
        bonus += 1
        ende += TIME_LIMIT
    zeige_punkte(score) # "print(score)"wird durch "show_score(score)" ersetzt, sodass die Punktzahl nun im Fenster des Spiels angezeigt wird.
    zeige_zeit(int(ende - time())) # Zeigt die verbleibende Zeit an.
    window.update()
    sleep(0.01)

#//1.8.4
# Nun fehlt noch eine "Game Over"-Anzeige, die eingeblendet wird, wenn die Zeit abgelaufen ist.
# Dieser code Steht ganz am Ende des Programms.

#c.create_text(MID_X, MID_Y, \  # Setzt die Grafik in die mitte des Bilschirms.
#              text='GAME OVER', fill='white', font=('Helvetica', 30)) # Legt die Schriftart fest:"Helvetica" eignet sich gut für grosse Buschtaben.
#c.create_text(MID_X, MID_Y + 30, \
#              text='Punkte: ' + str(score), fill='white') # Gibt die Gesamtpunktzahl an.
#c.create_text(MID_X, MID_Y + 45, \
#              text='Bonus-Zeit: ' + str(bonus * TIME_LIMIT), fill='white') # Die Textfarbe ist weiss.
#                                         ^Zeigt an, wie viel zusätzliche Zeit sich der Spieler verdient hat.  



