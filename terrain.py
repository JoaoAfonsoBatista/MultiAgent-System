#############################################################################################################################
#############################################################################################################################
        #aqui é programado o objeto "terrain"
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

import random as R

from renderable import *
from sample import *
from global_variables import *


import math
import pygame


class terrain():

    def __init__(self, x, y,has_water,has_life):
        
        self.x = x
        self.y = y
        
        self.fun_pos = lambda:(self.x,self.y)
        
        self.samples = []
        
        self.has_water = has_water
        self.has_life = has_life
        
        self.renderables = self.make_renderables()
        

        
        
        
    def make_renderables(self):
        pass
            
    def draw(self, screen):
        for r in self.renderables:
            
            r.draw(screen)
            
        for r in self.samples:
            
            r.draw(screen)
            
    def effect(self):
        pass
        
        

class mountain(terrain):
    def __init__(self, x, y,has_water = False,has_life = False):
        super().__init__(x, y,has_water,has_life)
        self.terrain_type = "mountain"
        
    def make_renderables(self):
        return [imagerenderable(self.x * square_width + 1,self.y * square_height + 1,pygame.image.load("mountain.png"))]
        
        
class flat(terrain):
    def __init__(self, x, y,has_water = False,has_life = False):
        
        super().__init__(x, y,has_water,has_life)
        self.terrain_type = "flat"
        
        
    def make_renderables(self):
        if self.has_water:
            return [imagerenderable(self.x * square_width + 1,self.y * square_height + 1,pygame.image.load("water.png"))]
        elif self.has_life:
            return [imagerenderable(self.x * square_width + 1,self.y * square_height + 1,pygame.image.load("life.png"))]
        else:
            return [imagerenderable(self.x * square_width + 1,self.y * square_height + 1,pygame.image.load("flat.png"))]

class rocky(terrain):
    def __init__(self, x, y,has_water = False,has_life = False):
        super().__init__(x, y,has_water,has_life)
        self.terrain_type = "rocky"
        
    def make_renderables(self):
        return [imagerenderable(self.x * square_width + 1,self.y * square_height + 1,pygame.image.load("rocky.png"))]
        