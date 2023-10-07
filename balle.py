import pygame

width ,height=1280,720 #Taille de la fenetre de jeu
monEcran=pygame.display.set_mode((width ,height ))

class Ball():

    def __init__(self):#Constructeur
        self.rayon = 10 #Attribut rayon
        self.vitesse = pygame.Vector2(1, 1)*0.2 #Attribut vitesse
        self.dir = pygame.Vector2(1, 1) #Attribut dir
        self.pos = pygame.Vector2(width/2, height/2) #Attribut position initiale


    def update(self):
        """
        Méthode pour l'actualisation de la position
        """
        self.pos.x += self.vitesse.x*self.dir.x
        self.pos.y += self.vitesse.y*self.dir.y

    def display(self):
        """
        Méthode pour afficher la balle
        """
        couleurBall=pygame.Color('#FFAA00')

        pygame.draw.circle(monEcran,couleurBall,(self.pos.x, self.pos.y),self.rayon)


    def checkEdges(self):
        """
        Méthode pour les collision avec les bords
        """
        #Bord droit
        if (self.pos.x > width - self.rayon and self.dir.x > 0):
            self.dir.x *= -1 # on change le signe de la dir
        #Bord gauche
        if (self.pos.x < self.rayon and self.dir.x < 0):
            self.dir.x *= -1
        #Bord haut
        if (self.pos.y < self.rayon and self.dir.y < 0):
            self.dir.y *= -1
        #Bord bas
        if (self.pos.y > height - self.rayon and self.dir.y > 0):
            self.dir.y *= -1

    def meets(self, paddle):
        """
        Méthode pour détecter la collision avec le paddle
        """
        if (self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.rayon and
            self.pos.x > paddle.pos.x - self.rayon and
            self.pos.x < paddle.pos.x + paddle.w + self.rayon):
            return True
        else:
            return False
