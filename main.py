#!/usr/bin/python3
from brique import *
import time
from paddle import *
import pygame
pygame.init()
WIDTH ,HEIGHT=1280,720 #Taille de la fenetre de jeu

monEcran=pygame.display.set_mode((WIDTH ,HEIGHT ))
score_initial=0

def game(monEcran,score_initial):#fonction qui est lancée au debut d'une partie
    """Cette fonction est toute la partie gameplay du jeu"""
    running=True#cette variable permet d'arreter la partie quand on meurt ou genre on quitte tu vois ?
    paddle=Paddle(WIDTH ,HEIGHT,monEcran)#creation du paddle
    while running:
        monEcran.fill((100))


        for evenement in pygame.event.get():# Boucle sur les evenements
            if evenement.type==pygame.QUIT: #Si l'evenement est quitter
                pygame.quit()  #arret de pygame
                running=False #arret de la boucle
            if evenement.type==pygame.MOUSEBUTTONDOWN:
                monClic=True
            else:
                monClic=False
            if evenement.type==pygame.KEYDOWN:
                if evenement.key==pygame.K_q:
                    paddle.isMovingLeft = True
                    paddle.isMovingRight = False

                elif evenement.key==pygame.K_d:
                    paddle.isMovingRight = True
                    paddle.isMovingLeft = False

            elif evenement.type==pygame.KEYUP:
                paddle.isMovingRight = False
                paddle.isMovingLeft = False
            #appel des méthodes pour le paddle
            paddle.display() #affichage
            paddle.checkEdges()#collisions avec les bords
            paddle.update() #actualiser l'affichage des déplacements
            pygame.display.update()


def cos_briques():
    """
    Renvoie la liste des coordonnées des briques
    """
    liste_cos = [] #Liste des coordonnées des briques
    cox = 100 #Coordonnée x
    coy = 10 #Coordonnée y
    for i in range(3) :
        coy += 30
        for j in range(10) :
            cox += 85
            liste_cos.append((cox,coy))
    return liste_cos

def placer_briques(): #Affichage des briques
    liste_cos = cos_briques()
    liste_briques = []
    for i in range(len(liste_cos)) :
        brique = Brick(liste_cos[i][0], liste_cos[i][1])
        brique.display()
        liste_briques.append(brique)
    return liste_briques

print(placer_briques())


game(monEcran,score_initial)
