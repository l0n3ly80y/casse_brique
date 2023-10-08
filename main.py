#!/usr/bin/python3
from brique import *
import time
from paddle import *
from balle import *
import pygame
from balle import *
pygame.init()
WIDTH ,HEIGHT=1280,720 #Taille de la fenetre de jeu

monEcran=pygame.display.set_mode((WIDTH ,HEIGHT ))
score_initial=0

background_image = pygame.image.load("Images/background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

pygame.mixer.music.load("sasageyo.mp3")
pygame.mixer.music.play(-1)

police = pygame.font.Font("LiberationSerif.ttf", 30)
x, y = monEcran.get_rect().center
x2, y2 = x, y
y -= 325
x -= 475
x2 += 475
y2 -= 325

def game(monEcran,score_initial):#fonction qui est lancée au debut d'une partie
    """Cette fonction est toute la partie gameplay du jeu"""
    running=True#cette variable permet d'arreter la partie quand on meurt ou genre on quitte tu vois ?
    liste_briques = creer_briques()
    paddle=Paddle(WIDTH ,HEIGHT,monEcran)#creation du paddle
    ball=Ball()
    start_time = time.time()
    game_time = 100 # Temps en secondes pour le timer
    while running:
        monEcran.blit(background_image, (0, 0))

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
        for i in range(len(liste_briques)):
            liste_briques[i].display()   #Affichage des liste_briques
        for i in range(len(liste_briques)-1,-1,-1):#Parcours de la liste inversée
            if (ball.meetBricks(liste_briques[i])):#collision avec la balle
                liste_briques.pop(i)     #Suppression de la brique touchée
                #del liste_briques[i]
                ball.dir.y*=-1    #Redirection de la balle
        texte = police.render("Briques restantes : "+ str(len(liste_briques)), 1, (120, 10, 210))
        texte_rect = texte.get_rect()
        texte_rect.center = (x,y)
        monEcran.blit(texte, texte_rect)
        temps = police.render("Temps restant : "+ str(int(game_time + (start_time - time.time()))), 1, (120, 10, 210))
        temps_rect = temps.get_rect()
        temps_rect.center = (x2, y2)
        monEcran.blit(temps, temps_rect)
        pygame.display.update()


def creer_briques():
    """
    Renvoie la liste des coordonnées des briques
    """
    liste_cos = [] #Liste des coordonnées des briques
    cox = 0 #Coordonnée x
    coy = -70 #Coordonnée y
    liste_briques = []
    for i in range(6) :
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
