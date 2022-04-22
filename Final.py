from tkinter import *
import random
import os

def saveScore():
    global score, Name
    names = []
    Scores = []
    with open('Highscores.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            line = line.split(':')
            names.append(line[0])
            Scores.append(line[-1])
    a = str(Name) + ":" + str(score)
    b = str(names[0]) + ":" + str(Scores[0])
    c = str(names[1]) + ":" + str(Scores[1])
    d = str(names[2]) + ":" + str(Scores[2])
    with open('Highscores.txt', 'w') as f:
        if score > int(Scores[2]):
            if score > int(Scores[1]):
                if score > int(Scores[0]):
                    f.truncate(0)
                    f.write(a + "\n")
                    f.write(b + "\n")
                    f.write(c + "\n")
                    print("New High Score!!")
                else:
                    f.truncate(0)
                    f.write(b + "\n")
                    f.write(a + "\n")
                    f.write(c + "\n")
                    print("Second highest score.")
            else:
                f.truncate(0)
                f.write(b + "\n")
                f.write(c + "\n")
                f.write(a + "\n")
                print("Third highest score.")
        else:
            f.truncate(0)
            f.write(b + "\n")
            f.write(c + "\n")
            f.write(d + "\n")
    root.destroy()

uTurn = ""
def changeU(e):
    global snake, blocks, uTurn
    if uTurn != 'D':
        snake[head] = 'U'
def changeD(e):
    global snake, blocks, uTurn
    if uTurn != 'U':
        snake[head] = 'D'
def changeR(e):
    global snake, blocks, uTurn
    if uTurn != 'L':
        snake[head] = 'R'
def changeL(e):
    global snake, blocks, uTurn
    if uTurn != 'R':
        snake[head] = 'L'

i = -1
g = 0
def apple(x,y):
    global i, snake, blocks, score, scorespeed
    a0, b0, a1, b1 = canvas.coords(A)
    canvas.move(A,-a0,-b0)
    if g == 0:
        canvas.move(A,x,y)
    i += 1
    if i > 0:
        score += 1
        scorespeed += 1
        block = canvas.create_rectangle(0, 0, 25, 25, fill='lime')
        l = blocks[-1]
        dir = snake[l]
        snake[block] = dir
        blocks.append(block)
        c0, d0, c1, d1 = canvas.coords(l)
        if dir == '':
            canvas.move(block, c0, d0)
        if dir == 'R':
            canvas.move(block, (c0 - 25), d0)
        if dir == 'L':
            canvas.move(block, (c0 + 25), d0)
        if dir == 'D':
            canvas.move(block, c0, (d0 - 25))
        if dir == 'U':
            canvas.move(block, c0, (d0 + 25))
def Snake():
    global snake, head, A, photo, g, i, speed, uTurn
    uTurn = snake[head]
    for k, v in snake.items():
        if v == 'U':
            canvas.move(k, 0, -25)
        if v == 'D':
            canvas.move(k, 0, 25)
        if v == 'R':
            canvas.move(k, 25, 0)
        if v == 'L':
            canvas.move(k, -25, 0)

    x0, y0, x1, y1 = canvas.coords(head)
    a0, b0, a1, b1 = canvas.coords(A)

    if x0 <= -1 or x1 >= 501 and g == 0:
        for block in blocks:
            canvas.move(block, 520, 520)
        canvas.move(A, 520, 520)
        canvas.create_image(250, 200, image=photo, anchor='center')
        g += 1

    if y0 <= -1 or y1 >= 501 and g == 0:
        for block in blocks:
            canvas.move(block, 520, 520)
        canvas.move(A, 520, 520)
        canvas.create_image(250, 200, image=photo, anchor='center')
        g += 1

    for i in blocks[1:]:
        e0, f0, e1, f1 = canvas.coords(i)
        if g == 0:
            if x0 == e0 and x1 == e1 and y0 == f0 and y1 == f1:
                for block in blocks:
                    canvas.move(block, 520, 520)
                canvas.move(A, 520, 520)
                canvas.create_image(250, 200, image=photo, anchor='center')
                g += 1

    if x0 < a1 and y0 < b1:
        if x1 > a0 and y1 > b0:
            y = str(25 * random.randint(0, 19))
            x = str(25 * random.randint(0, 19))
            apple(x, y)

    for i in range(len(blocks) - 1, 0, -1):
        dir = snake[blocks[i - 1]]
        snake[blocks[i]] = dir
    root.after(speed, Snake)
def SandT():
    global score, time, t, g, label, scorespeed, speed, oops
    if g == 0:
        scor = str(score)
        time += 1
        if time == 60:
            t += 1
            time -= 60
        tim = str(time)
        ti = str(t)
        if time < 10:
            label = Label(root, text='Score: ' + scor + ' Apples ate          Time: ' + ti + ' : 0' + tim + ' (secs)').grid(row=0, column=2)
        else:
            label = Label(root, text='Score: ' + scor + ' Apples ate           Time: ' + ti + ' : ' + tim + ' (secs)').grid(row=0, column=2)
    if score <= 72:
        if scorespeed >= 3:
            scorespeed -= 3
            speed -= 15
    root.after(1000, SandT)
def overlay():
    global i, snake, blocks, A, speed, speed1
    a0, b0, a1, b1 = canvas.coords(A)
    if i > 0:
        for block in blocks[1:]:
            e0, f0, e1, f1 = canvas.coords(block)
            if a0 == e0 and a1 == e1 and f0 == b0 and f1 == b1:
                canvas.move(A, -a0, -b0)
                y = str(25 * random.randint(0, 19))
                x = str(25 * random.randint(0, 19))
                canvas.move(A, x, y)
    root.after(speed1, overlay)

class ABC(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.grid()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Snake")
        Entry(self)
root = Tk()
abc = ABC(root)

Name = input("Enter your name to save your score: ")
print("Your Game is waiting on a different window.")
canvas = Canvas(root, height=500, width=500)
photo = PhotoImage(file='over.png')
A = canvas.create_rectangle(275,125,300,150, fill='red', outline='red')
head = canvas.create_rectangle(275,125,300,150,fill='green')
snake = {head: ''}
blocks = list(snake.keys())
score = 0
time = 00
t = 0
speed = 400
speed1 = 10
scorespeed = 0

label = Label(root, text='Score:       Time: ').grid(row=0, column=2)
restart = Button(root, text="Save Score", command=saveScore, width=25).grid(row=2, column=2)
canvas.bind("<Down>", changeD)
canvas.bind("<Up>", changeU)
canvas.bind("<Right>", changeR)
canvas.bind("<Left>", changeL)
canvas.bind("<s>", changeD)
canvas.bind("<w>", changeU)
canvas.bind("<d>", changeR)
canvas.bind("<a>", changeL)
canvas.focus_set()
canvas.grid(row=1, column=2)

root.after(speed, Snake)
root.after(1000, SandT)
root.after(speed1, overlay)
root.mainloop()
