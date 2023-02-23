import pygame as p
p.init()
import pygame.freetype as pf
import random as r
import map
from satinbs import*
from sprait import*

sench = Sanek((SHIRINA/2, VISOTA/2))
display = p.display.set_mode((SHIRINA, VISOTA))
w = True
mep = map.Map()

while w:
    event_list = p.event.get()
    for event in event_list:
        if event.type == p.QUIT:
            w = False
    
    display.fill((0, 0, 0))
    mep.dref(display)
    sench.drew(display)
    sench.up()
    p.display.update()
    
    # clok.tick(FPS)