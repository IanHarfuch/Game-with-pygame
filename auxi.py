import random
import math
import pygame

from random import randint


# definicao da resolucao
DISPLAY_WIDTH  = 800
DISPLAY_HEIGHT = 600

# definicao das cores (monokai)
gray   = (39,40,34)
white  = (255,255,255)
orange = (253,151,31)
pink   = (249,38,114)
blue   = (102,217,239)
green  = (166,226,46)

# cor dos blocos
blockColors = [orange, pink, blue, green]



###############################################################################
#                                 Constantes
###############################################################################
# definicoes gerais
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Projeto Integrado 1B!")
clock = pygame.time.Clock()



# pega uma cor aleatoria da lista
def random_color():
    return random.choice(blockColors)

Vi = 0
grav = 2450
FPS = 1/60
chao = 600
fall = False
angulo = 0
teta = 0
teta_pos = False
teta_neg = False
center = 0
keys = False
ang = 45*math.pi/180
massa = 20
coeficiente_atrito = 0.02
a = 0
victory = False

#atrito = coeficiente_atrito*massa*grav
foi_lancada = True
#impacto = False
mov_bola_forca = True





 # MELHORIA

###############################################################################
#                                 Texto
###############################################################################
# renderiza o texto
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# apresenta texto na tela
def display_message(text, color):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)

    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image