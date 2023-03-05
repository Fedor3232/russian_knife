import pygame as p
p.init()
import pygame.freetype as pf
import random as r
import map
from satinbs import*
from sprait import*

class Game:
    def __init__(self):
        self.display = p.display.set_mode((SHIRINA, VISOTA))
        self.sench = Sanek([7345, 6700])
        self.mep = map.Map()
        self.cemmeran = DG(self.sench)

    def event(self):
        event_list = p.event.get()
        for event in event_list:
            if event.type == p.QUIT:
                w = False

    def up(self):
        for T in self.mep.tail:
            self.cemmeran.retyrn(T)
        self.cemmeran.retyrn(self.sench)
        self.sench.up()
        self.cemmeran.up()
        p.display.update()
        # clok.tick(FPS)

    def dref(self):
        self.display.fill((0, 0, 0))
        self.mep.dref(self.display)
        self.sench.drew(self.display)

    def run(self):
        while w:
            pass