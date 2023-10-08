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
police = pygame.font.Font("pixel-font.TTF", 30)
x, y = monEcran.get_rect().center
x_tps_restant, y_tps_restant = x, y #Coordonnées des textes à afficher
y -= 325
x -= 400
x_tps_restant += 400
y_tps_restant -= 325


def game(monEcran):#fonction qui est lancée au debut d'une partie
    """Cette fonction est toute la partie gameplay du jeu"""
    running=True#cette variable permet d'arreter la partie quand on meurt ou on quitte
    liste_briques = creer_briques()
    paddle=Paddle(WIDTH ,HEIGHT,monEcran)#creation du paddle
    ball=Ball()

    start_time = time.time()
    game_time = 200 # Temps en secondes pour le timer

    gameplay_background = pygame.image.load("Images/background.png")
    gameplay_background = pygame.transform.scale(gameplay_background, (WIDTH, HEIGHT)) #Affichage du fond d'écran*

    pygame.mixer.music.load("sasageyo.mp3")
    pygame.mixer.music.play(-1) #Lancement de la musique
    pygame.mixer.music.set_volume(1)

    while running:
        monEcran.blit(gameplay_background, (0, 0))

        for evenement in pygame.event.get():# Boucle sur les evenements
            if evenement.type==pygame.QUIT: #Si l'evenement est quitter
                pygame.quit()  #arret de pygame
                running=False #arret de la boucle
            if evenement.type==pygame.KEYDOWN:
                if evenement.key==pygame.K_LEFT:
                    paddle.isMovingLeft = True
                    paddle.isMovingRight = False

                elif evenement.key==pygame.K_RIGHT:
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
            print(ball.vitesse.x)
            print(ball.vitesse.y)

            if (ball.dir.y>0):
                ball.dir.y=-ball.dir.y
            if paddle.isMovingRight:
                if ball.dir.x>0:
                    ball.vitesse.x+=0.4
                else:
                    ball.vitesse.x-=0.5


            elif paddle.isMovingLeft:
                if ball.dir.x>0:
                    ball.vitesse.x-=0.4
                else:
                    ball.vitesse.x+=0.5




            #appel des méthodes pour le paddle

        paddle.display() #affichage
        paddle.checkEdges()#collisions avec les bords
        paddle.update() #actualiser l'affichage des déplacements
        for i in range(len(liste_briques)):
            liste_briques[i].display()   #Affichage des liste_briques
        for i in range(len(liste_briques)-1,-1,-1):#Parcours de la liste inversée
            if (ball.meetBricks(liste_briques[i])):#collision avec la balle
                #balle.vitesse.x=pygame.Vector2(1, 1)*1.5
                if ball.dir.y>0:
                    if ball.pos.x>liste_briques[i].pos.x+5 and ball.pos.x < liste_briques[i].pos.x-5+liste_briques[i].l:
                        ball.dir.y*=-1

                        print('collison de la balle avec le haut dune brique')
                    else:
                        ball.dir.x*=-1
                        print("collision avec un cote vers le bas")
                else:

                    if ball.pos.x>liste_briques[i].pos.x+5 and ball.pos.x < liste_briques[i].pos.x-5+liste_briques[i].l:
                        ball.dir.y*=-1
                        print('collison de la balle avec le bas dune brique')
                    else:
                        ball.dir.x*=-1
                        print("collision avec un cote vers le bas")

                liste_briques.pop(i)     #Suppression de la brique touchée

        texte = police.render("Briques restantes : "+ str(len(liste_briques)), 1, (120, 10, 210))
        texte_rect = texte.get_rect()
        texte_rect.center = (x,y)
        monEcran.blit(texte, texte_rect) #Affichage du nombre de briques restantes

        elapsed_time = time.time() - start_time
        temps_restant = game_time - elapsed_time
        tr = int(temps_restant//1) #Calcul du temps restant
        if tr <= 0 :
            tr = 0
        temps = police.render(f"Temps restant : {tr}", 1, (120, 10, 210))
        temps_rect = temps.get_rect()
        temps_rect.center = (x_tps_restant, y_tps_restant)
        monEcran.blit(temps, temps_rect) #Affichage du temps restant

        pygame.display.update()




def homescreen(monEcran) :
    homescreen_background = pygame.image.load("Images/homescreen.png")
    homescreen_background = pygame.transform.scale(homescreen_background, (WIDTH, HEIGHT)) #Création du fond d'écran

    pygame.mixer.music.load("op1.mp3")
    pygame.mixer.music.play(-1) #Lancement de la musique
    pygame.mixer.music.set_volume(0.15)
    running = True

    while running :
        monEcran.blit(homescreen_background, (0, 0))
        for evenement in pygame.event.get():# Boucle sur les evenements
                if evenement.type==pygame.QUIT: #Si l'evenement est quitter
                    pygame.quit()  #arret de pygame
                    running=False #arret de la boucle
                if evenement.type==pygame.MOUSEBUTTONDOWN:
                    running = False
                    game(monEcran)
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


if __name__=='__main__':
    homescreen(monEcran)
