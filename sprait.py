import pygame as p
p.init()
import pygame.freetype as pf
import random as r
import map
from satinbs import*
from sprait import*

class Sanek:

    def __init__(self, spavn, bame):
        self.spavn = spavn
        self.animate = p.image.load("player_sheet.png")
        self.player = self.noxnici(32, 32, 64, 0)
        self.player = p.transform.scale(self.player, (100, 100))
        self.rect = self.player.get_rect(topleft = self.spavn)
        self.rect_p = self.player.get_rect(topleft = self.spavn)
        self.dd = 0
        self.game = bame
        self.animates()
        
    def noxnici(self, vis, shir, x, y):
        ANIMATE = self.animate.subsurface(x, y, shir, vis)
        return ANIMATE

    def drew(self, display):
        display.blit(self.player, self.rect_p)

    def kyvalda(self):
        for gf in self.game.mep.tail:
            if gf.rect_p.colliderect(self.rect_p) and gf.nymer in WALL_IDS:
                print("пока")

    def up(self):
        self.speed_VIS = 0
        self.speed_SHIR = 0
        gg = p.key.get_pressed()
        if gg[UP] == True:
            self.speed_VIS = -5
        if gg[DOWN] == True:
            self.speed_VIS = 5
        if gg[LEFT] == True:
            self.speed_SHIR = -5
        if gg[RIGHT] == True:
            self.speed_SHIR = 5

        self.kyvalda()

        self.rect.x = self.rect.x + self.speed_SHIR
        self.rect.y = self.rect.y + self.speed_VIS
        self.aim()

    def animates(self):
        xx = 0
        self.an_r = []
        self.an_l = []
        self.an_u = []
        self.an_d = []
        for ghf in range(1, 5):
            sd = self.noxnici(32, 32, xx, 64)
            sd = p.transform.scale(sd, (100, 100))
            self.an_r.append(sd)
            xx = xx + 32
        xx = 0
        for ghf in range(1, 5):
            sd = self.noxnici(32, 32, xx, 32)
            sd = p.transform.scale(sd, (100, 100))
            self.an_l.append(sd)
            xx = xx + 32
        xx = 0
        for ghf in range(1, 5):
            sd = self.noxnici(32, 32, xx, 0)
            sd = p.transform.scale(sd, (100, 100))
            self.an_d.append(sd)
            xx = xx + 32
        xx = 0
        for ghf in range(1, 5):
            sd = self.noxnici(32, 32, xx, 96)
            sd = p.transform.scale(sd, (100, 100))
            self.an_u.append(sd)
            xx = xx + 32
        xx = 0

    def aim(self):

        aup = []
        if self.speed_VIS != 0 or self.speed_SHIR != 0:
            if self.speed_VIS < 0:
                aup = self.an_u
            if self.speed_VIS > 0:
                aup = self.an_d
            if self.speed_SHIR < 0:
                aup = self.an_l
            if self.speed_SHIR > 0:
                aup = self.an_r
            self.player = aup[self.dd]
            self.dd = self.dd + 1
            if self.dd == 4:
                self.dd = 0

class Tile:
    def __init__(self, spavn, nymer, paint):
        self.paint = paint
        self.p = p.transform.scale(self.paint, (TAIL_SIZE, TAIL_SIZE))
        self.nymer = nymer
        self.spavn = spavn
        self.rect = p.Rect(spavn, (TAIL_SIZE,TAIL_SIZE))
        self.rect_p = p.Rect(spavn, (TAIL_SIZE,TAIL_SIZE))

    def dref(self, display):
        display.blit(self.p, self.rect_p)

class DG:
    def __init__(self, sench):
        self.sench = sench
        self.offset = (7345, 6700)

    def up(self):
        x = -self.sench.rect.x + SHIRINA//2
        y = -self.sench.rect.y + VISOTA//2
        self.offset = [x, y]
    def retyrn(self, tile):
        tile.rect_p = tile.rect.move(self.offset)

class Game:
    
    def __init__(self):
        self.display = p.display.set_mode((SHIRINA, VISOTA))
        self.sench = Sanek(SPAVN, self)
        self.mep = map.Map()
        self.cemmeran = DG(self.sench)
        self.w = True

    def event(self):
        event_list = p.event.get()
        for event in event_list:
            if event.type == p.QUIT:
                self.w = False

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
        while self.w:
            self.event()
            self.up()
            self.dref()