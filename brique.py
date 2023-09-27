import pygame

width ,height=1280,720 #Taille de la fenetre de jeu
monEcran=pygame.display.set_mode((width ,height ))

"""
class Brique :
    def __init__(self, id:int, powerup:str, x:int, y:int) :
        self.id = id #Identifiant de la brique
        self.powerup = powerup #Nom du bonus associé à la brique
        self.posx = x #Abscisse de la brique
        self.posy = y #Ordonnée de la brique
"""

class Brick():
    #attribut de classe un dictionnaire de couleurs
    color = '70726E'

    def __init__(self, x, y, color):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attreibut largeur
        self.pos = pygame.Vector2(x, y) # attribut position
        self.color = color #attribut couleur

    # méthode pour afficher la brique
    def display(self):
        noir=(0,0,0)
        #Rectangle plein coloré
        pygame.draw.rect(monEcran,self.col,(self.pos.x, self.pos.y, self.w, self.h))
        #Rectangle vide dont le contour est d'épaisseur 1
        pygame.draw.rect(monEcran,noir,(self.pos.x, self.pos.y, self.w, self.h),1)
