import meny 
import screeninfo as s
import pygame as p
import hhj
dd = s.get_monitors()
w = dd[0]

SHIRINA = w.width * float(meny.z_reed["skreen_size"])
VISOTA = w.height * float(meny.z_reed["skreen_size"])
FPS = 100
TAIL_SIZE = int(meny.z_reed["size"])
NAME = meny.z_reed["name"]
SPAVN = hhj.spavner(NAME)
if TAIL_SIZE == 32:
    SPAVN = [SPAVN[0]//2, SPAVN[1]//2]
# SPAVN = [0, 0]

if meny.z_reed["wasd"] == True:
    UP = p.K_w
    DOWN = p.K_s
    LEFT = p.K_a
    RIGHT = p.K_d
else:
    UP = p.K_UP
    DOWN = p.K_DOWN
    LEFT = p.K_LEFT
    RIGHT = p.K_RIGHT

if meny.s_reed == "start":
    W = True
    G = False
elif meny.s_reed == "bye":
    W = False

WALL_IDS = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
            18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
            35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            52, 53, 54, 58, 59, 60, 61, 52, 53, 54, 65, 66, 67,
            69, 70, 75, 76, 77, 78, 79, 81, 82, 83, 84,
            92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
            107, 108, 109, 110, 11, 112, 113, 114, 115, 116, 227, 118,
            119, 120, 121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135]
