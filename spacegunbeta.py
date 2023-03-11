from random import *
from math import *
from bot import bot
from shipgo import ship 
import pygame
from pygame.locals import *
from bulletclass import *
import os
pygame.init()


#display
screen = pygame.display.set_mode((800,700),0,32)
pygame.display.set_caption('Space Gun beta')
shipsurface = pygame.image.load('ship.png').convert_alpha()
botsurface = pygame.image.load('bot.png').convert_alpha()

#gun data
mousepos = [600,0]
r = 150000
p2x = 1500
p2y = 0

#ship data
ship_size = shipsurface.get_size()
(w,h) = ship_size
w = w/2
h = h/2
lx = 400.
ly = 300.

#bullet data
gamebullet = []
trigger = False

#bot data
bot_size = botsurface.get_size()

rect1 = [(100,100),(300,300)]
rect2 = [(400,400),(600,500)]

gamebots = {'a':bot('name1'),'b':bot('name2'),'c':bot('name3'),'d':bot('name4')}
spaceship = ship('main ship',(lx,ly))

# bots position
start_pos = [(50,0),(600,50),(50,500),(600,500)]


a = 0
for _ in gamebots:
    gamebots[_].set_pos(start_pos[a])
    a +=1
print shipsurface.get_size()

while True and spaceship.alive :
    clock = pygame.time.Clock()
    time_passed = clock.tick(60)
    event = pygame.event.poll()
    if event.type == QUIT:
        os._exit(0)
    screen.fill((255,255,255))
    pressed_keys = pygame.key.get_pressed()

    if event.type == MOUSEMOTION:
        mousepos = pygame.mouse.get_pos()
        x1,y1 = spaceship.get_pos()
        x2,y2 = mousepos
        dx = x2-x1
        dy = y2-y1
        angle = atan2(dy,dx)
        p2x = r*cos(angle)
        p2y = r*sin(angle)



    if pressed_keys[K_w]:
        ly-= 3
    if pressed_keys[K_s]:
        ly+= 3
    if pressed_keys[K_a]:
        lx-= 3
    if pressed_keys[K_d]:
        lx+= 3

    
    spaceship.set_pos((lx,ly))

    x,y = spaceship.get_pos()
    lblit = [(x+w),(y+h)]

    mp = pygame.mouse.get_pressed()

    if mp[0]:
        trigger = True


    if not mp[0]:
        if trigger:
            [x,y] = lblit
            gamebullet.append(bullet([x,y],angle))
            gamebullet[-1].cfpos(cos(angle),sin(angle))
            trigger = False

    for _ in gamebullet:
        _.newpos()

    
    for _ in gamebots:
        gamebots[_].gen_pos(spaceship.get_pos())

    for b in gamebots:
        for a in gamebullet:
            gamebots[b].calive(a.get_p1())

    #draw game bots
    for _ in gamebots:
        if gamebots[_].alive:
            screen.blit(botsurface,gamebots[_].get_pos())

    x3,y3 = spaceship.get_pos()

    for _ in gamebots:
        if not gamebots[_].alive:
            x = randint(0,3)
            gamebots[_].alive = True
            gamebots[_].set_pos(start_pos[x])
    
    #draw space ship
    screen.blit(shipsurface,spaceship.get_pos())

    #draw aim line
    pygame.draw.line(screen,(255,0,0),(p2x,p2y),lblit)

    #draw game bullets
    for _ in gamebullet:
        pygame.draw.line(screen,(0,0,0),_.get_p1(),_.get_p2())

    pygame.display.update()
    for _ in gamebots:
        spaceship.calive(gamebots[_].get_pos())

while not spaceship.alive:
    event = pygame.event.poll()
    if event.type == QUIT:
        os._exit(0)
    screen.fill((0,0,0))
    font = pygame.font.SysFont("arial",20)
    text = "Game Over"
    text_surface =  font.render(text,True,(255,0,0))
    x,y = text_surface.get_size()
    screen.blit(text_surface,((400-x),(300-y)))
    pygame.display.update()
        
