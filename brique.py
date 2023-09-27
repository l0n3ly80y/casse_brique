import pygame

class Brique :
    def __init__(self, id:int, powerup:str, x:int, y:int) :
        self.id = id #Identifiant de la brique
        self.powerup = powerup #Nom du bonus associé à la brique
        self.posx = x #Abscisse de la brique
        self.posy = y #Ordonnée de la brique

class Brick(): 
    #attribut de classe un dictionnaire de couleurs
    COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}

    def __init__(self, x, y, hits):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attreibut largeur
        self.pos = pygame.Vector2(x, y) # attribut position
        self.hits = hits #attribut clé pour la couleur
        self.col = Brick.COLORS[hits] # la couleur

    # méthode pour afficher la brique
    def display(self):
        noir=(0,0,0)
        #Rectangle plein coloré
        pygame.draw.rect(monEcran,self.col,(self.pos.x, self.pos.y, self.w, self.h))
        #Rectangle vide dont le contour est d'épaisseur 1
        pygame.draw.rect(monEcran,noir,(self.pos.x, self.pos.y, self.w, self.h),1)

