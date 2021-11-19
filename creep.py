import pygame
from pygame.math import Vector2
import random
import core



class Creep:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(random.randint(0,largeur),random.randint(0,hauteur))
        self.taille = 5
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.masse = 5


    def show(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.taille)


