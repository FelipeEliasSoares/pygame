#* Importando a biblioteca pygame
import pygame

#* Importando as constantes da biblioteca pygame
from pygame.locals import *

#* from sys import exit
from sys import exit

#* Inicializando o pygame
pygame.init()


#todo: Configurações da tela
width = 640
height = 480


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #* Desenhando um retângulo na tela
    pygame.draw.rect(screen, (255, 0, 0), (200,300,40,50))

    #* Desenhando um círculo na tela
    pygame.draw.circle(screen, (0, 0, 255), (300, 260), 40)

    #* Desenhando uma linha na tela
    pygame.draw.line(screen, (255, 255, 0), (390,0), (390,600), 5)


    pygame.display.update() #* Atualizando a tela

#* Finalizando o pygame
pygame.quit()
exit()
#* Executando o programa
