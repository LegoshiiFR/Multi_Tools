import importlib
import subprocess
import os

def is_pip_installed():
    try:
        importlib.import_module('pip')
        return True
    except ImportError:
        return False
    

def is_pygame_installed():
    try:
        importlib.import_module('pygame')
        return True
    except ImportError:
        return False

if is_pip_installed() and is_pygame_installed():
    print("pip et les modules sont déjà installés.")
    os.system("cls")
else:
    if not is_pip_installed():
        print("pip n'est pas installé. Installation en cours...")
        subprocess.check_call(['python', '-m', 'ensurepip', '--default-pip'])
        print("pip a été installé avec succès.")
        os.system("cls")

    if not is_pygame_installed():
        print("Le module tqdm n'est pas installé. Installation en cours...")
        subprocess.check_call(['pip', 'install', 'pygame'])
        print("Le module pygame a été installé avec succès.")
        os.system("cls")

import pygame
import random
pygame.init()

# définir les dimensions de la fenêtre de jeu
screen_width = 800
screen_height = 600

# créer la fenêtre de jeu
screen = pygame.display.set_mode((screen_width, screen_height))

# charger les images pour les personnages et les arrière-plans
background_image = pygame.image.load("background.png").convert()
player_image = pygame.image.load("player.png").convert_alpha()

# définir la position initiale du joueur
player_x = 100
player_y = 400

# boucle de jeu
while True:
    # gérer les événements de clavier
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quitter le jeu si l'utilisateur ferme la fenêtre
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # déplacer le joueur à gauche ou à droite en fonction des touches fléchées
            if event.key == pygame.K_LEFT:
                player_x -= 10
            elif event.key == pygame.K_RIGHT:
                player_x += 10

    # dessiner l'arrière-plan et le joueur sur l'écran
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))

    # mettre à jour l'écran
    pygame.display.update()