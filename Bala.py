import pygame
import time
import math

from auxi import *
#from canhao import *
#from impulso import Impulso
from barra_de_forca import Bola_forca



class Bala(object):

    def __init__(self, x,y,w,h,image):
        self.w = w 
        self.h = 100
        self.x = x
        self.y = y
        self.Vx = 0
        self.Vy = 0
        self.ax = 0
        self.ay = 0
        self.angul = 0
        self.forc = 0
        self.img = image
        self.at = 0
        self.forca_movimento = 0
        self.a = 0
        self.forca_atrito = 0
        self.atrito = 0
        self.impacto = False
        self.forca = 0
        self.atritox = 0
        self.atritoy = 0
        
      

    def throw(self, canhao, forca_resultante):
        self.ay = grav
        self.angul = canhao.angulo*math.pi/180
        self.Vx = math.cos(self.angul)*forca_resultante
        self.Vy = -math.sin(self.angul)*forca_resultante
        self.atrito = self.forca_atrito
        self.forca = forca_resultante

    def incrementoVelocidade(self):
        self.Vy += (self.forca + self.ay + self.atritoy) * FPS
        if self.Vx > 0:
            self.Vx -= (self.ax - self.atritox) * FPS
        elif self.Vx < 0:
            self.Vx += (self.ax + self.atritox) * FPS
            
    def incrementoPosicao(self):  
        self.x += (self.Vx)*FPS
        if self.impacto == False:
            self.y += (self.Vy)*FPS
        else:
            self.y = self.y

    def update(self):
        self.incrementoVelocidade()
        self.incrementoPosicao()
        self.ground()
        self.wall()
        self.forcaa()
        self.vento()
        self.atrito_vel()
        print ('vy=', self.Vx)
        print ( self.y)
        print ( self.ay)
        print ('a = ', self.a)
        print ('vx = ', self.Vx)
        print('atrito', self.forca_atrito)
        print('y = ', self.y)
        print('Vx = ',self.Vx)
        print ('atrito x=', self.atritox)
      #  print (canhao.angulo)

    def draw(self):
        gameDisplay.blit(self.img,(self.x, self.y))

    ## incrementos 


#saber se chegou no chao
    def ground(self):
        if self.y + self.h >= 650:
            self.y = 550
            self.Vy = -(self.Vy + self.atrito) 
            #if self.x >= 650:
            #    self.Vx -= self.forca_atrito 
            #if self.Vx == 0:
            #    self.at = 0

    def wall(self):
        if self.x <= 0:
            self.impacto = True
            self.x = 0
            self.ay = 0
            self.Vy = 0
             
        elif self.x + self.w >= 850:
            self.x = 850 - self.w 
            if self.Vx > 0:
                self.Vx = self.Vx - self.forca_atrito
                self.Vx = -self.Vx
            elif self.Vx == 0:
                self.Vx = 0 
           

    def forcaa(self):
        self.forca_atrito = coeficiente_atrito*massa*self.Vx

    def vento(self):
        if self.Vy > 0:

            if self.x > 200 and self.x < 350 and self.y > 350 and self.y < 590:
                self.Vy += 70
            elif self.x > 200 and self.x < 350 and self.y > 10 and self.y < 250:
                self.Vy -= 70
            elif self.x > 450 and self.x < 600 and self.y > 350 and self.y < 590:
                self.Vy -= 70
            elif self.x > 450 and self.x < 600 and self.y > 10 and self.y < 250:
                self.Vy += 70
        else:
            if self.x > 200 and self.x < 350 and self.y > 350 and self.y < 590:
                self.Vy -= 70
            elif self.x > 200 and self.x < 350 and self.y > 10 and self.y < 250:
                self.Vy += 70
            elif self.x > 450 and self.x < 600 and self.y > 350 and self.y < 590:
                self.Vy += 70
            elif self.x > 450 and self.x < 600 and self.y > 10 and self.y < 250:
                self.Vy -= 70

    def atrito_vel(self):
        self.atritox = (1.6*0.28*0.001225*((self.forca)/FPS))/2
        self.atritoy = ((1.6*0.28*0.001225*((self.ay)/FPS))/2)
