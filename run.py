from calendar import month

from fontTools.misc.cython import returns

import App
from Draw import *
from Motor import *

draw = Draw()
motor = Motor()

run = 1
while run == 1:
    draw.start()
    auswahl = int(input("Geben Sie die Nummer des Menüpunkts ein: "))
    print(auswahl)

    match auswahl:
        case App.menu.straightAhead:
            print("jaaaaaaaa")
            motor.straightAhead()
            draw.straightAhead()
        case App.menu.returns:
            print("jaaaaaaaa")
            motor.returns()


