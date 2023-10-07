#!/usr/bin/python3
from brique import *
import time
from paddle import *
from balle import *
import pygame
pygame.init()
WIDTH ,HEIGHT=1280,720 #Taille de la fenetre de jeu

monEcran=pygame.display.set_mode((WIDTH ,HEIGHT ))
score_initial=0

def game(monEcran,score_initial):#fonction qui est lancée au debut d'une partie
    """Cette fonction est toute la partie gameplay du jeu"""
    running=True#cette variable permet d'arreter la partie quand on meurt ou genre on quitte tu vois ?
    paddle=Paddle(WIDTH ,HEIGHT,monEcran)#creation du paddle
    ball=Ball()
    while running:
        monEcran.fill((100))


        for evenement in pygame.event.get():# Boucle sur les evenements
            if evenement.type==pygame.QUIT: #Si l'evenement est quitter
                pygame.quit()  #arret de pygame
                running=False #arret de la boucle
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
            # appel des méthodes pour la balle
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
        pygame.display.update()


def placer_briques(monEcran):

    return 0
game(monEcran,score_initial)
