# coding=utf-8  (obligatoire Python 2.7)

WIDTH ,HEIGHT=1280,720 #Taille de la fenetre de jeu
import pygame
class Paddle():

    def __init__(self,WIDTH,HEIGHT,monEcran): # constructeur
        self.monEcran=monEcran
        self.w = 120  # attribut longueur du paddle
        self.h = 15   # attribut largeur du paddle
        # la position du paddle avec un objet Pvector
        self.pos = pygame.Vector2(WIDTH/2 - self.w/2, HEIGHT - 40) #La position initiale en fonction de la taille de la fenêtre
        self.isMovingLeft = False  # booléen pour mouvement à gauche
        self.isMovingRight = False  # idem à droite
        self.stepSize = 4   # pas pour le déplacement
    # méthode premettant l'affichage
    def display(self):
        # affichage du rectangle rect(x,y,longueur, largeur)
        couleurPaddle=pygame.Color(120, 10, 210)
        pygame.draw.rect(self.monEcran,couleurPaddle,(self.pos.x, self.pos.y, self.w, self.h))
     # méthode qui gère le déplacement
    def move(self, step):
        self.pos.x +=step
    # méthode pour actualiser l'affichage des déplacements
    def update(self):
        if self.isMovingLeft:
            self.move(-self.stepSize)
        elif self.isMovingRight:
            self.move(self.stepSize)

    # méthode qui gère les collisions avec les bords
    def checkEdges(self):
        if self.pos.x <= 0:
            self.pos.x = 0
        elif self.pos.x + self.w >= WIDTH:
            self.pos.x = WIDTH - self.w
