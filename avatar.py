import random

import pygame
from pygame.math import Vector2

import core


class Avatar:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400,200)
        self.taille = 10
        self.couleur = (255,0,0)
        self.masse = 10
        self.vel = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
        self.acc = Vector2()
        self.maxAcc = 300
        self.maxVel = 4
        self.count = 0
        self.force = 0
        self.complete = False



    def show(self, screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.taille)



    def deplacement(self,target):






        if core.getKeyPressList(276):
            if core.memory("monVecteur").angle_to(Vector2(0, 1)) > -45:
                core.memory("monVecteur", core.memory("monVecteur").rotate(1))
        elif core.getKeyPressList(275):
            if core.memory("monVecteur").angle_to(Vector2(0, 1)) < 45:
                core.memory("monVecteur", core.memory("monVecteur").rotate(-1))
        else:
            if abs(core.memory("monVecteur").angle_to(Vector2(0, 1))) > 0.00001:
                if core.memory("monVecteur").angle_to(Vector2(0, 1)) < 0:
                    core.memory("monVecteur", core.memory("monVecteur").rotate(-1))
                else:
                    core.memory("monVecteur", core.memory("monVecteur").rotate(1))

        if core.getKeyPressList(273):
            core.memory("monVecteur",
                        core.memory("monVecteur").scale_to_length(core.memory("monVecteur").magnitude() + 10))
        elif core.getKeyPressList(274) and core.memory("monVecteur").magnitude() > 10:
            core.memory("monVecteur",
                        core.memory("monVecteur").scale_to_length(core.memory("monVecteur").magnitude() - 10))
        else:
            if core.memory("monVecteur").magnitude() != core.memory("magnitude"):

                if abs(core.memory("monVecteur").magnitude() - core.memory("magnitude")) > 0.0001:
                    if core.memory("monVecteur").magnitude() - core.memory("magnitude") < 0:
                        core.memory("monVecteur", core.memory("monVecteur").scale_to_length(
                            core.memory("monVecteur").magnitude() + 10))
                    else:
                        core.memory("monVecteur", core.memory("monVecteur").scale_to_length(
                            core.memory("monVecteur").magnitude() - 10))

