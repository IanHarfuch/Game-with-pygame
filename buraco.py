import pygame 
from auxi import *

class Buraco(object):

    def  __init__(self, x,y,image):
        self.x = x
        self.y = y
        self.img = image

    def draw(self):
        gameDisplay.blit(self.img,(self.x, self.y))


  