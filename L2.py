import pgzrun 
from random import randint

WIDTH = 600 
HEIGHT = 500
TITLE = "Protect the nest"
score = 0
game_over = False

ant1 = Actor ("ant1")
ant1.pos = 50,280
ant2 = Actor ("ant2")
ant2.pos = 290,200

def draw ():
    screen.fill("green")
    ant1.draw()
    ant2.draw()
    screen.draw.text("score:"+str(score),color = "black",midtop = (300,10))

    if game_over :
        screen.fill("white")
        screen.draw.text("Times up your final score is "+str(score),color = "black",midtop = (300,100),fontsize = 40)


def place_ant2():
    ant2.x = randint(50,550)
    ant2.y = randint(50,450)
    

def update():
    global score
    if keyboard.left:
        ant1.x = ant1.x-2

    if keyboard.right:
        ant1.x = ant1.x+2

    if keyboard.up:
        ant1.y = ant1.y-2
    
    if keyboard.down:
        ant1.y = ant1.y+2


    ant_touched = ant1.colliderect(ant2)
    if ant_touched:
        place_ant2()
        score = score+5

def times_up():
    global game_over
    game_over = True

clock.schedule(times_up,15.0)        

    
pgzrun.go()









































