###########################################
#           SNT - M. Elophe - 2020        #
###########################################

# Ici on va importer les modules que nous allons utiliser.
# C'est comme le from robot import * de France IOI
import pygame
from pygame.locals import *

# Ouverture de la fenêtre Pygame
TAILLE_FENETRE = (640, 480)
fenetre = pygame.display.set_mode(TAILLE_FENETRE)
# On peut ajouter un titre à la fenêtre.
pygame.display.set_caption("Narusturm !")

# Couleur de fond au format RGB : (Rouge, Vert, Bleu)
# En l'occurence, ici, j'ai jeté mon dévolu sur un petit violet pâle pas trop agrgessif.
couleur = (92, 107, 192)
fenetre.fill(couleur)

# Chargement du personnage
perso = pygame.image.load("images/narut0.png").convert_alpha()
# On redimensionne l'image en 20 px de large et 50 de haut
perso = pygame.transform.scale(perso, (32, 32))
# On colle le personnage
fenetre.blit(perso, (32, 32))
position = perso.get_rect()
# Il faut penser à rafraichir l'écran ! (Surtout en été)
pygame.display.flip()

#########
mur = pygame.image.load("images/mur.jpg").convert_alpha()
sol = pygame.image.load("images/gazon.jpg").convert_alpha()
# On redimensionne l'image en 20 px de large et 50 de haut
sol = pygame.transform.scale(sol, (32, 32))
####################################
def move(structure, position, direction):
    x = position[0]
    y = position[1]
    colonne = x // 32
    ligne = y // 32
    if direction == "droite":
        if structure[ligne][colonne + 1] == "m":
            print("Bim le mur")
            return position
        else:
            position[0] += 32
            #position = position.move(32, 0)
    if direction == "gauche":
        if structure[ligne][colonne - 1] == "m":
            print("Bim le mur")
            return position
        else:
            position[0] -= 32
            #position = position.move(32, 0)
    if direction == "bas":
        if structure[ligne + 1][colonne] == "m":
            print("Bim le mur")
            return position
        else:
            position[1] += 32
            #position = position.move(32, 0)
    if direction == "haut":
        if structure[ligne - 1][colonne] == "m":
            print("Bim le mur")
            return position
        else:
            position[1] -= 32
            #position = position.move(32, 0)
    print(f"Le personne se trouve actuellement en colonne {colonne} et ligne {ligne}")
    return position

####################################
# Lecture de la map
#################################"
with open("maps/map1.txt", 'r') as file:
    data = file.read()
    print(data)
structure = data.split("\n")
print(structure)

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
                move(structure, position, "droite")
            if event.key == K_LEFT:
                move(structure, position, "gauche")

            if event.key == K_UP:
                move(structure, position, "haut")

            if event.key == K_DOWN:
                move(structure, position, "bas")

    fenetre.fill(couleur)

    num_ligne = 0
    num_col = 0
    for ligne in structure:
        num_col = 0
        for case in ligne:
            if case == 'm':
                fenetre.blit(mur, (num_col * 32, num_ligne * 32))
            else:
               fenetre.blit(sol, (num_col * 32, num_ligne * 32))
            num_col += 1
        num_ligne += 1
        #ICI RAJOUTER LES AUTRES DEPLACEMENT
    fenetre.blit(perso, position)
    pygame.display.flip()