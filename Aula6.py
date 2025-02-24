#* Importando a biblioteca pygame
import pygame

#* Importando as constantes da biblioteca pygame
from pygame.locals import *

#* from sys import exit
from sys import exit

#* Inicializando o pygame
pygame.init()

#* Importando a ramdom 
from random import randint


#todo: Configurações da tela
width = 640
height = 480
x = width / 2   #? Posição x do retângulo
y = height / 2   #? Posição y do retângulo

#* Posição do retângulo azul
x_blue = randint(40, 600)
y_blue = randint(50, 430)


# Inicializando a fonte
pygame.font.init()

# Criando um objeto de fonte
font = pygame.font.SysFont('arial', 40)


#? Defindo os Pontos
point = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo')

#! clock = fps
clock = pygame.time.Clock()

while True:
    clock.tick(30) #* Configurando a taxa de atualização
    screen.fill((0,0,0)) #* Preenchendo a tela com a cor preta
    msg = f'Ponto: {point}'
    text_format = font.render(msg, True, (255, 255, 255))
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

    #* Desenhando um retângulo vermelhor na tela
    rest_red =  pygame.draw.rect(screen, (255, 0, 0), (x,y,40,50))
    
    #* Desenhando um retângulo azul na tela
    rest_blue = pygame.draw.rect(screen, (0, 0, 255), (x_blue, y_blue, 40, 50))

    #* Verificando se os retângulos colidiram
    if rest_red.colliderect(rest_blue):
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)
        point += 1

    screen.blit(text_format, (450,40))
    pygame.display.update() #* Atualizando a tela

#* Finalizando o pygame
pygame.quit()
exit()
#* Executando o programa