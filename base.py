import pygame 
from auxi import *

class Base(object):

    def  __init__(self, x,y,w,h,image):
        self.w = w 
        self.h = h
        self.x = x
        self.y = y
        self.img = image

    def draw(self):
        gameDisplay.blit(self.img,(self.x, self.y))


  