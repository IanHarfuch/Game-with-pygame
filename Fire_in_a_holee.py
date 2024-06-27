import pygame


from auxi import *
from Bala import Bala
from base import Base
from canhao import Canhao
from barra_de_forca import Barra_forca
from barra_de_forca import Bola_forca
from buraco import Buraco

#from Bala import Impulso
#from impulso import Impulso

pygame.init()


###############################################################################
#                                 Loop
###############################################################################


    
##
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))


clock = pygame.time.Clock()

largeText = pygame.font.Font('freesansbold.ttf',115)

#exibindo black hole
buracao = pygame.image.load('imagem/buracao.png')
hole = Buraco(-40,100,buracao)



## exibindo bola
bala1 = pygame.image.load('imagem/bola_preta.png')
bala = Bala(170,540,100,100,bala1)

#exibindo barra de força
barra_forca = pygame.image.load('imagem/barra_de_forca.png')
barra_de_forca = Barra_forca(690, 570, barra_forca)


#exibindo bola da barra de força
bola_forca = pygame.image.load('imagem/bolinha.png')
bola_de_forca = Bola_forca(690, 570, bola_forca)


#exibindo canhao
canhao1 = pygame.image.load('imagem/canhaotest.png')
canhao = Canhao(50,440,canhao1)

#exibindo base
base1 = pygame.image.load('imagem/base_do_canhao.png')
base = Base(40, 500, 0, 0, base1)


while True:
    teta = 0
    ff = bola_de_forca.x2 * 5.2 
    print('ff =', ff)
    #detecta eventos
    for event in pygame.event.get():
        
        #verifica evento de fechamento
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()   
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bala.throw(canhao,(ff))
                    

        if event.type == pygame.KEYUP:
                
            if event.key == pygame.K_UP:
                canhao.movimentando = False

            if event.key == pygame.K_f:       
                mov_bola_forca = False
            
        
    if bala.y > 90 and bala.y < 160 and bala.x < 60:
        victory = True
         
    #preencher a tela
    fundo = pygame.image.load("imagem/fundoo.png")
    gameDisplay.blit(fundo,(0, 0))

    #adicionando barra de força
    barra_de_forca.draw()

    #adicionando bola da barra de força
    bola_de_forca.draw()

    #update da barra de força
    if mov_bola_forca == True:
        bola_de_forca.update() 


    if victory == True:
        TextSurf, TextRect = text_objects("You win", largeText, gray)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
        gameDisplay.blit(TextSurf, TextRect)
        
    #adicionando bola
    bala.draw()

    #movimentos
    bala.update()

    #adicionando canhao
    canhao.draw()

    #adicionando base
    base.draw()

    #adicionando buaco
    hole.draw()

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()


