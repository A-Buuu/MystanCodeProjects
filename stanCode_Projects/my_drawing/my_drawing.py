"""
File: my_drawing.py
Name: A-Bu
----------------------
This file creates a drawing
that is going to compete for the Best
Drawing Award for SC101.
It will combine various GObjects
(including but not limited to GOval,
GRect, GLine, GLabel...) to create the drawing!
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

DELAY = 1
window = GWindow(800, 550, title="Vision Test")


def main():
    """
    創作理念：我不是美術系，我是深度近視。
    """
    onmouseclicked(get_position)
    background()
    sky_and_grass()
    house()
    flower(5000)
    line()
    jungle()
    fix()


def get_position(mouse):
    print("("+str(mouse.x)+", "+str(mouse.y)+")")


def background():
    bg = GRect(800, 550)
    bg.filled = True
    window.add(bg)


def sky_and_grass():
    sky = GOval(540, 540)
    sky.filled = True
    sky.fill_color = "dodgerblue"
    sky.color = "dodgerblue"
    window.add(sky, (window.width-sky.width)/2, (window.height-sky.height)/2)

    grass = GArc(540, 1050, 0, -180)
    grass.filled = True
    grass.fill_color = "olivedrab"
    grass.color = "olivedrab"
    window.add(grass, (window.width-sky.width)/2, 20)


def house():
    house_1 = GPolygon()
    house_1.add_vertex((391, 261))
    house_1.add_vertex((376, 273))
    house_1.add_vertex((376, 282))
    house_1.add_vertex((404, 282))
    house_1.add_vertex((404, 274))
    house_1.filled = True
    house_1.fill_color = "white"
    house_1.color = "white"
    window.add(house_1)

    house_2 = GRect(18, 8, x=404, y=274)
    house_2.filled = True
    house_2.fill_color = "white"
    house_2.color = "white"
    window.add(house_2)

    door_1 = GPolygon()
    door_1.add_vertex((389, 269))
    door_1.add_vertex((384, 273))
    door_1.add_vertex((384, 282))
    door_1.add_vertex((394, 282))
    door_1.add_vertex((394, 273))
    door_1.filled = True
    door_1.fill_color = "black"
    door_1.color = "black"
    window.add(door_1)

    door_2 = GRect(5, 9, x=385, y=273)
    door_2.filled = True
    door_2.fill_color = "white"
    door_2.color = "white"
    window.add(door_2)

    doorknob = GOval(2, 2, x=385, y=274)
    doorknob.filled = True
    doorknob.fill_color = "black"
    doorknob.color = "black"
    window.add(doorknob)

    roof_1 = GPolygon()
    roof_1.add_vertex((391, 261))
    roof_1.add_vertex((404, 274))
    roof_1.add_vertex((422, 274))
    roof_1.add_vertex((422, 261))
    roof_1.filled = True
    roof_1.fill_color = "red"
    roof_1.color = "red"
    window.add(roof_1)

    roof_2 = GLine(392, 259, 374, 275)
    roof_2.color = "red"
    window.add(roof_2)

    roof_3 = GLine(391, 261, 405, 275)
    roof_3.color = "red"
    window.add(roof_3)


def flower(quanty):
    for i in range(quanty):
        size = random.randint(1, 5)
        dot = GOval(size, size)
        dot.filled = True
        dot.fill_color = "darkkhaki"
        dot.color = "darkkhaki"
        random_x = random.randint(130, 670)
        random_y = random.randint((window.height/2)+10, window.height)
        window.add(dot, random_x, random_y)
        pause(DELAY)


def line():
    line_1 = GLine(132, 317, 326, 284)
    window.add(line_1)
    line_2 = GLine(137, 369, 358, 284)
    window.add(line_2)
    line_3 = GLine(146, 393, 370, 286)
    window.add(line_3)
    line_4 = GLine(156, 413, 377, 285)
    window.add(line_4)
    line_5 = GLine(168, 429, 379, 285)
    window.add(line_5)
    line_6 = GLine(176, 442, 380, 287)
    window.add(line_6)
    line_7 = GLine(191, 458, 384, 285)
    window.add(line_7)
    line_8 = GPolygon()
    line_8.add_vertex((198, 473))
    line_8.add_vertex((209, 482))
    line_8.add_vertex((387, 285))
    line_8.filled = True
    window.add(line_8)
    line_9 = GPolygon()
    line_9.add_vertex((272, 514))
    line_9.add_vertex((287, 521))
    line_9.add_vertex((398, 285))
    line_9.filled = True
    window.add(line_9)
    line_10 = GPolygon()
    line_10.add_vertex((312, 538))
    line_10.add_vertex((325, 540))
    line_10.add_vertex((400, 287))
    line_10.filled = True
    window.add(line_10)
    line_11 = GPolygon()
    line_11.add_vertex((363, 543))
    line_11.add_vertex((373, 545))
    line_11.add_vertex((405, 285))
    line_11.filled = True
    window.add(line_11)
    line_12 = GPolygon()
    line_12.add_vertex((423, 546))
    line_12.add_vertex((439, 543))
    line_12.add_vertex((407, 285))
    line_12.filled = True
    window.add(line_12)
    line_13 = GLine(488, 532, 409, 286)
    window.add(line_13)
    line_14 = GPolygon()
    line_14.add_vertex((546, 505))
    line_14.add_vertex((560, 496))
    line_14.add_vertex((412, 286))
    line_14.filled = True
    window.add(line_14)
    line_15 = GPolygon()
    line_15.add_vertex((589, 479))
    line_15.add_vertex((599, 472))
    line_15.add_vertex((415, 286))
    line_15.filled = True
    window.add(line_15)
    line_16 = GLine(610, 448, 417, 285)
    window.add(line_16)
    line_17 = GLine(636, 414, 419, 285)
    window.add(line_17)
    line_18 = GLine(654, 372, 425, 284)
    window.add(line_18)
    line_19 = GLine(665, 336, 458, 284)
    window.add(line_19)
    line_20 = GLine(670, 307, 496, 285)
    window.add(line_20)


def jungle():
    l_jungle = GArc(117, 30, 0, 180)
    l_jungle.filled = True
    l_jungle.fill_color = "forestgreen"
    l_jungle.color = "forestgreen"
    window.add(l_jungle, x=130, y=274)

    r_jungle = GArc(100, 30, 0, 180)
    r_jungle.filled = True
    r_jungle.fill_color = "forestgreen"
    r_jungle.color = "forestgreen"
    window.add(r_jungle, x=569, y=274)


def fix():
    fig = GPolygon()
    fig.add_vertex((671, 286))
    fig.add_vertex((671, 297))
    fig.add_vertex((669, 321))
    fig.add_vertex((665, 345))
    fig.add_vertex((658, 368))
    fig.add_vertex((653, 381))
    fig.add_vertex((643, 404))
    fig.add_vertex((634, 420))
    fig.add_vertex((626, 433))
    fig.add_vertex((614, 448))
    fig.add_vertex((605, 457))
    fig.add_vertex((589, 474))
    fig.add_vertex((568, 493))
    fig.add_vertex((557, 501))
    fig.add_vertex((542, 510))
    fig.add_vertex((524, 519))
    fig.add_vertex((515, 523))
    fig.add_vertex((490, 533))
    fig.add_vertex((459, 541))
    fig.add_vertex((419, 547))
    fig.add_vertex((383, 548))
    fig.add_vertex((350, 544))
    fig.add_vertex((330, 539))
    fig.add_vertex((311, 533))
    fig.add_vertex((294, 527))
    fig.add_vertex((279, 521))
    fig.add_vertex((261, 510))
    fig.add_vertex((237, 494))
    fig.add_vertex((225, 485))
    fig.add_vertex((205, 468))
    fig.add_vertex((193, 454))
    fig.add_vertex((174, 429))
    fig.add_vertex((155, 397))
    fig.add_vertex((145, 370))
    fig.add_vertex((138, 346))
    fig.add_vertex((132, 323))
    fig.add_vertex((132, 320))
    fig.add_vertex((130, 304))
    fig.add_vertex((130, 285))

    fig.add_vertex((0, 284))
    fig.add_vertex((0, window.height))
    fig.add_vertex((window.width, window.height))
    fig.add_vertex((window.width, 284))
    fig.filled = True
    fig.fill_color = "black"
    fig.color = "black"
    window.add(fig)


if __name__ == '__main__':
    main()
