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
y = height / 2   #? Posição y do retângulo


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

        '''
            #* Movimentando o retângulo
            if event.type == KEYDOWN:
                if event.key == K_w:
                    y = y - 20
                if event.key == K_s:
                    y = y + 20
                if event.key == K_a:
                    x = x - 20
                if event.key == K_d:
                    x = x + 20
        '''

    #* Movimentando o retângulo pressionando a tecla    
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:        
        y = y + 10  
    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10

    #* Desenhando um retângulo na tela
    pygame.draw.rect(screen, (255, 0, 0), (x,y,40,50))




    pygame.display.update() #* Atualizando a tela

#* Finalizando o pygame
pygame.quit()
exit()
#* Executando o programa
