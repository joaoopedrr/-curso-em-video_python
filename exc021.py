import pygame as pg
pg.init()
pg.mixer.music.load('./musicat.mp3')
pg.mixer.music.play()
input()
pg.event.wait()