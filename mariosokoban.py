# importation des modules nécessaires
import pygame
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLEU = (0, 0, 255)


fenetre = pygame.display.set_mode((640, 480))

fond = pygame.image.load("images/gazon.jpg").convert()
fenetre.blit(fond, (0, 0))




pygame.display.flip()
continuer = True

while continuer:
    continuer = int(input())


