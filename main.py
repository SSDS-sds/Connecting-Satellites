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

def update():
    pass






create_sats()
pgzrun.go()