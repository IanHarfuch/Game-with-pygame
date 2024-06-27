import pygame
import math

from auxi import *

class Barra_forca(object):

    def __init__(self, x, y, image_barra):
        self.x = x
        self.y = y
        self.image_barra = image_barra
    
    def draw(self):
        gameDisplay.blit(self.image_barra,(self.x, self.y))

class Bola_forca(object):

    def __init__(self, x2, y, image_bola):
        self.x2 = x2 + 1
        self.y = y
        self.image_bola = image_bola
        self.movimento = False
        self.bolax = 0

    def draw(self):
        gameDisplay.blit(self.image_bola,(self.x2, self.y))
    
    def movimento_bola(self):
        if self.movimento == True:
            self.x2 -= 11
            if self.x2 <= 690:
                self.movimento = False

        if self.movimento == False:
            self.x2 += 11
            if self.x2 > 768:
                self.movimento = True
        
    

    def update(self):
        self.movimento_bola()
        
        print ('bolax=', self.x2)
        
    