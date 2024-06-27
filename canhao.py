import pygame
from auxi import *
import math


class Canhao(object):

    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.img = image
        self._img = image

        self.movimentando = True

        self.angulo = 0
        self.up = True
    


    def draw(self):
        if self.movimentando:
            self.movimento()
        gameDisplay.blit(self.img,(self.x, self.y))
        print ('self.angulo=', self.angulo)


    def movimento(self):
        if self.up:
            self.angulo += 1
            if self.angulo == 90:
                self.up = False

        if not self.up:
            self.angulo -= 1
            if self.angulo == 0:
                self.up = True

    
    
        #center = self.img.get_rect(60,440).center
        self.img = rot_center(self._img, self.angulo)
        #new_rect = self.img.get_rect(center = center)        

    ##angulo_canhao = angulo



