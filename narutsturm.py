###########################################
#           SNT - M. Elophe - 2020        #
###########################################

# Ici on va importer les modules que nous allons utiliser.
# C'est comme le from robot import * de France IOI
import pygame
from pygame.locals import *
from deplacement import move
# Import des constantes du jeu
from configuration import *
from random import choice

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode(TAILLE_FENETRE)
# On peut ajouter un titre à la fenêtre.
pygame.display.set_caption("Narusturm !")

# Chargement du personnage
perso_bas = pygame.image.load(MARIO['Bas']).convert_alpha()
perso_bas = pygame.transform.scale(perso_bas, (CARRE, CARRE))
perso_haut = pygame.image.load(MARIO['Haut']).convert_alpha()
perso_haut = pygame.transform.scale(perso_haut, (CARRE, CARRE))
perso_droite = pygame.image.load(MARIO['Droite']).convert_alpha()
perso_droite = pygame.transform.scale(perso_droite, (CARRE, CARRE))
perso_gauche = pygame.image.load(MARIO['Gauche']).convert_alpha()
perso_gauche = pygame.transform.scale(perso_gauche, (CARRE, CARRE))
perso= perso_bas
position = perso_bas.get_rect()
# Il faut penser à rafraichir l'écran ! (Surtout en été)
pygame.display.flip()

#########################
# Chargement des images
#########################
mur = pygame.image.load(WALL).convert_alpha()
mur = pygame.transform.scale(mur, (CARRE, CARRE))
caisse = pygame.image.load("images/caisse.jpg").convert_alpha()
caisse = pygame.transform.scale(caisse, (CARRE, CARRE))
but = pygame.image.load("images/objectif.png").convert_alpha()
but = pygame.transform.scale(but, (CARRE, CARRE))
sol = pygame.image.load("images/fond.png").convert_alpha()
# On redimensionne l'image en 20 px de large et 50 de haut
sol = pygame.transform.scale(sol, (CARRE, CARRE))
####################################

####################################
# Lecture de la map
#################################"
with open(choice(MAP), 'r') as file:
    data = file.read()
    print(data)
structure = data.split("\n")
print(structure)
###################################
# Boucle de jeu, "infinie", parce que le jeu doit continuer tant que je ne l'arrête pas
continuer = True
pygame.key.set_repeat(500, 30)
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                perso = perso_droite
                move(structure, position, "droite")
            if event.key == K_LEFT:
                perso = perso_gauche
                move(structure, position, "gauche")

            if event.key == K_UP:
                perso = perso_haut
                move(structure, position, "haut")

            if event.key == K_DOWN:
                perso = perso_bas
                move(structure, position, "bas")

    fenetre.fill(COULEUR)

    num_ligne = 0
    num_col = 0
    for ligne in structure:
        num_col = 0
        for case in ligne:
            if case == 'm':
                fenetre.blit(mur, (num_col * CARRE, num_ligne * CARRE))
            elif case == "#":
                fenetre.blit(caisse, (num_col * CARRE, num_ligne * CARRE))
            elif case == "x":
                fenetre.blit(sol, (num_col * CARRE, num_ligne * CARRE))
                fenetre.blit(but, (num_col * CARRE, num_ligne * CARRE))
            else:
               fenetre.blit(sol, (num_col * CARRE, num_ligne * CARRE))
            num_col += 1
        num_ligne += 1
        #ICI RAJOUTER LES AUTRES DEPLACEMENT
    fenetre.blit(perso, position)
    pygame.display.flip()