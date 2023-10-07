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
    liste_briques = créer_briques()
    paddle=Paddle(WIDTH ,HEIGHT,monEcran)#creation du paddle
    ball=Balle()
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
        ball.display()
        ball.checkEdges()
        ball.update()
        if (ball.meets(paddle)):
            if (ball.dir.y>0):
                ball.dir.y=-ball.dir.y
            #appel des méthodes pour le paddle
        paddle.display() #affichage
        paddle.checkEdges()#collisions avec les bords
        paddle.update() #actualiser l'affichage des déplacements
        for brique in liste_briques :
            brique.display()
        pygame.display.update()


def créer_briques():
    """
    Renvoie la liste des coordonnées des briques
    """
    liste_cos = [] #Liste des coordonnées des briques
    cox = 0 #Coordonnée x
    coy = -70 #Coordonnée y
    liste_briques = []
    for i in range(5) :
        cox = 0
        coy += 70
        for j in range(10) :
            liste_cos.append((cox,coy))
            cox += 128
    for k in range(len(liste_cos)) :
        brique = Brick(liste_cos[k][0], liste_cos[k][1])
        liste_briques.append(brique)
    return liste_briques



game(monEcran,score_initial)
