import os
import sys
import random as r
import math
import pygame as pg
from pygame import *
import time

class MainGameOperator():
    gameStatus = True
    BGCol = (30, 30, 30)
    
    def __init__(self, screenx = 900, screeny = 900):
        self.screenx = screenx
        self.screeny = screeny
        pg.display.set_mode((self.screenx, self.screeny))
        pg.display.set_caption("Spreding Circle")

        self.FPS = 60
        self.clock = pg.time.Clock()
        self.gameSet()

    def gameSet(self):
        self.Circle = []
    
    def loopMain(self):
        while self.gameStatus == True:
            self.inputControl
            self.updateToCal
            self.draw
'''
            if True:
                self.clock.tick(self.FPS)
            else:
                self.clock.tick()
'''


    def inputControl(self):
        events = pg.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.gameStatus = True
                sys.exit()
            
            elif event.type == KEYDOWN:
                if (event.key == K_ESCAPE):
                    self.gameStatus = False
            
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 :
                pos = pygame.mouse.get_pos()
                self.Circle.append((pos))


    
    def updateToCal(self):
        pass
    
    def draw(self):
        pass

if __name__ == '__main__':
    the = MainGameOperator()
    the.loopMain()