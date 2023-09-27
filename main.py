#!/usr/bin/python3
from objects import *
import pygame
pygame.init()
width ,height=1280,720 #Taille de la fenetre de jeu
monEcran=pygame.display.set_mode((width ,height ))
def game(monEcran):#fonction qui est lancée au debut d'une partie
    """Cette fonction est toute la partie gameplay du jeu"""
    running=True#cette variable permet
    while running:
        monEcran.fill((100))


        pygame.display.update()
def placer_briques(monEcran):
    
    return 0
