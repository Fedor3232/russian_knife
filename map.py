import pygame as p
import csv
import sprait
from satinbs import*

class  Map:
    def __init__(self):
        self.map_png = p.image.load("rpg_tileset.png")
        self.map_png1 = []
        self.d = 0
        self.b = 0
        self.boroholka()
        self.perevodchik()
        self.tail = []
        self.g()

    def noxnici(self, vis, shir, x, y):
        ANIMATE = self.map_png.subsurface(x, y, shir, vis)
        return ANIMATE

    def boroholka(self):
        for gfgf in range(1, 9):
            for fdf in range(1, 18):
                f = self.noxnici(16, 16, self.d, self.b)
                self.map_png1.append(f)
                self.d = self.d + 16
            self.d = 0
            self.b = self.b + 16
        
    def perevodchik(self):
        self.hp = []
        gg = open("levle1..csv")
        self.hp = list(csv.reader(gg))

    def g(self):
        x = 0
        y = 0
        for gf in self.hp:
            for ggf in gf:
                
                ff = self.map_png1[int(ggf)]
                ffg = sprait.Tile((x,y), ggf, ff)
                self.tail.append(ffg)
                x = x + TAIL_SIZE
            x = 0
            y = y + TAIL_SIZE
            
    def dref(self, display):
        for f in self.tail:
            f.dref(display)