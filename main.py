import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Connecting Satellites"

current_sat = 0
total_sat = 8
start_time = 0
total_time = 0
sats = []
lines = []

def create_sats():
    global start_time
    for i in range(total_sat):
        sat = Actor("sat")
        sat.pos = randint(40,760), randint(40,560)
        sats.append(sat)
    start_time = time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    num = 1
    for sat in sats:
        screen.draw.text(str(num),(sat.pos[0],sat.pos[1] + 20))
        sat.draw()
        num = num + 1
    
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    
    if current_sat < total_sat:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
    
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

def update():
    pass

def on_mouse_down(pos):
    global current_sat,lines
    if current_sat < total_sat:
        if sats[current_sat].collidepoint(pos):
            if current_sat:
                lines.append(
                    (
                        sats[current_sat-1].pos,
                        sats[current_sat].pos
                    )
                )
            current_sat = current_sat + 1
        else:
            lines = []
            current_sat = 0




create_sats()
pgzrun.go()