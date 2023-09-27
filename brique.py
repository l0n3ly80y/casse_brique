import pygame

width ,height=1280,720 #Taille de la fenetre de jeu
monEcran=pygame.display.set_mode((width ,height ))

class Brick():
    #Attributs de classe
    color = '70726E'
    pouvoirs = {1 : 'grosse' , 2 : 'perf' , 3 : 'double'}

    def __init__(self, x:int, y:int, pouvoir:int): #Constructeur
        self.largeur = 75 #Attribut longueur
        self.hauteur = 20 #Attribut largeur
        self.pos = pygame.Vector2(x, y) #Attribut position
        self.color = Brick.color #Attribut couleur
        self.pouvoir = Brick.pouvoirs[pouvoir] #Attribut pouvoir

    def display(self):
        """
        Méthode pour afficher la brique
        """
        noir=(0,0,0)
        #Rectangle plein coloré
        pygame.draw.rect(monEcran,self.color,(self.pos.x, self.pos.y, self.largeur, self.hauteur))
        #Rectangle vide dont le contour est d'épaisseur 1
        pygame.draw.rect(monEcran,noir,(self.pos.x, self.pos.y, self.largeur, self.hauteur),1)
