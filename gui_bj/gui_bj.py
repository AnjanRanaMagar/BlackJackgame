'''
Black Jack Program to learn about python!
Anjan Rana Magar
Date:Sep26,2022
'''

from graphics import *
import random, time

def window():
    ''' GUI WINDOW! '''
    win = GraphWin("BlackJack!",800,800)
    win.setCoords(0,0,900,900)

    # drawing rectangle:
    P1,P2 = Point(250, 250),Point(250+100, 250+100)
    rec = Rectangle(P1,P2)
    rec.setFill('white')
    rec.setOutline('red')
    rec_center = rec.getCenter()
    txt = Text(rec_center,'A')
    txt.setFill('red')
    txt.setSize(25)
    rec.draw(win)
    txt.draw(win)
    win.getMouse()


window()

