#############################################################################################################################
#############################################################################################################################
        #aqui é programado o objeto "sample"
        #basicamente só tem a informação de onde está, de onde vem, se está a ser carried ou não, e como a desenhar
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

import random as R

from renderable import *
from global_variables import *


import math
import pygame


class sample():

    def __init__(self, x, y, carried):
        
        self.x = x
        self.y = y
        
        self.fun_pos = lambda:(self.x,self.y)
        
        self.original_x = x
        self.original_y = y
        
        self.fun_original_pos = lambda:(self.original_x,self.original_y)
        
        self.carried = carried
        
        self.renderables = self.make_renderables()
        
        
        
        
    def make_renderables(self):
        return [rectrenderable_changeble(lambda: self.x * square_width + square_width/3,lambda:self.y * square_height + square_height/3, lambda: square_height/3, lambda: square_width/3,funcolor = lambda: (0,0,0))]
        
        
    def draw(self, screen):
        #pygame.draw.rect(screen, (0,0,0), (0,0, gstate.get().width, gstate.get().current_height))
        #print(len(self.renderables))
        if not self.carried:
            for r in self.renderables:
                
                r.draw(screen)
            
    def effect(self):
        pass