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
    pygame.display.update() #* Atualizando a tela

#* Finalizando o pygame
pygame.quit()
exit()
#* Executando o programa
