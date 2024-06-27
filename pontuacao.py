import pygame
import time
import math

from auxi import *
from Bala import *

class Pontuacao(object):
    def __init__(self,Bala):
        self.modulo_posicao = abs(Bala.y)
        self.ponto = 0
        self.distancia_medida = 0
        self.font = pygame.font.SysFont(None, 25)
        self.text = ""


    def distancia(self):
        if self.modulo_posicao < 250:
            self.distancia_medida = 250 - self.modulo_posicao
        else:
            self.distancia_medida = self.modulo_posicao - 250

    def valor_ponto(self):
        if self.distancia_medida > 51:
            self.ponto = 0
        elif self.distancia_medida < 50 and self.distancia_medida > 26:
            self.ponto = 50
        elif self.distancia_medida < 25 and self.distancia_medida > 0:
            self.ponto = 100
        elif self.distancia_medida < 1:
            self.ponto = 500


    def draw(self):
        self.text = self.font.render("Score: {}".format(self.ponto), True, white)
        gameDisplay.blit(self.text, (0,0))
