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
x = width / 2   #? Posição x do retângulo
y = 0   #? Posição y do retângulo


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo')

#! clock = fps
clock = pygame.time.Clock()

while True:
    clock.tick(30) #* Configurando a taxa de atualização
    screen.fill((0,0,0)) #* Preenchendo a tela com a cor preta
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    #* Desenhando um retângulo na tela
    pygame.draw.rect(screen, (255, 0, 0), (x,y,40,50))

    if y >= height :
        y = 0

    y = y + 1


    pygame.display.update() #* Atualizando a tela

#* Finalizando o pygame
pygame.quit()
exit()
#* Executando o programa
