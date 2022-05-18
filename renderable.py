#############################################################################################################################
#############################################################################################################################
        #ignorem isto, é simplesmente para desenhar coisas no ecra
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

import pygame
from auxiliary_functions import *
from global_variables import *

class renderable:
    def __init__(self, x, y, width = 40, height = 40):
        self.x, self.y = x, y
        self.pos = (x, y)
        self.width = width
        self.height = height
        
    def draw(self, screen):
        pass
    def get_coordenates(self):
        return [self.x,self.x + self.width,self.y,self.y + self.height]

class renderable_changeble:
    def __init__(self, funx, funy, funwidth = lambda:40, funheight = lambda: 40):
        self.x, self.y = funx, funy
        self.pos = (self.x(), self.y())
        self.width = funwidth
        self.height = funheight
    def draw(self, screen):
        pass
    def get_coordenates(self):
        return (self.x(), self.x() + self.width(), self.y(),self.y() + self.height())
        
class imagerenderable(renderable):
    def __init__(self, x, y, image, width = 40, height = 40):
        super().__init__(x, y, width, height)
        self.image = image
        
        
    def draw (self, screen, adjust = [0,0]):
        if self.image == "no_image":
            pass
        else:
            pos = add_lists(self.pos,adjust)
            #if (gstate.get().vacaboy.position[0] - gstate.get().vacaboy.vision_range) * gstate.get().square_width < pos[0] < (gstate.get().vacaboy.position[0] + gstate.get().vacaboy.vision_range) * gstate.get().square_width and (gstate.get().vacaboy.position[1] - gstate.get().vacaboy.vision_range) * gstate.get().square_height < pos[1] < (gstate.get().vacaboy.position[1] + gstate.get().vacaboy.vision_range) * gstate.get().square_height:
            screen.blit(self.image, pos)
    def get_coordenates(self):
        return (self.x, self.x + self.width, self.y,self.y + self.height)

class imagerenderable_changeble(renderable_changeble):
    def __init__(self, funx, funy, funimage, funwidth = lambda:40, funheight = lambda: 40):
        super().__init__(funx, funy, funwidth, funheight)
        self.image = funimage
        
    def draw (self, screen, adjust = [0,0]):
        if self.image() == "no_image":
            pass
        else:
            pos = add_lists([self.x(),self.y()],adjust)
            screen.blit(self.image(), pos)


class rectrenderable(renderable):
    def __init__(self, x, y, w, h, color = (0,0,0) , width = 40, height = 40):
        super().__init__(x, y, width, height)
        self.w, self.h = w, h
        self.rect = (x, y, w, h)
        self.color = color
    def draw (self, screen, adjust = [0,0]):
        pygame.draw.rect(screen, self.color, (self.x+adjust[0],self.y+adjust[1],self.w,self.h))
        
class rectrenderable_changeble(renderable_changeble):
    def __init__(self, funx, funy, funw, funh, funcolor = lambda: (0,0,0), funwidth = lambda:40, funheight = lambda: 40):
        super().__init__(funx,funy, funwidth, funheight)
        self.w, self.h = funw, funh
        self.rect = (self.x(), self.y(), self.w(), self.h())
        self.color = funcolor
    def draw (self, screen, adjust = [0,0]):
    
        self.rect = (self.x() + adjust[0], self.y() + adjust[1], self.w(), self.h())

        pygame.draw.rect(screen, self.color(), self.rect)
        
class circlerenderable(renderable):
    def __init__(self, x, y, r, color = (0,0,0) , width = 40, height = 40):
        super().__init__(x, y , width, height )
        self.color = color
        self.r = r
    def draw(self, screen, adjust = [0,0]):
        pygame.draw.circle(screen, self.color, add_lists((self.x, self.y),adjust), self.r)
    
class textrenderable(renderable):
    def __init__(self, x, y, color, font, textfun , width = 40, height = 40):
        super().__init__(x, y, width, height)
        self.color = color
        self.font = font
        self.textfun = textfun

    def draw(self, screen, adjust = [0,0]):
        txt = self.font.render(self.textfun(), True, self.color)
        screen.blit(txt, add_lists((self.x, self.y),adjust))
        
class textrenderable_changeble(renderable_changeble):
    def __init__(self, funx, funy, funcolor, funfont, funtext, funwidth = lambda:40, funheight = lambda: 40):
        super().__init__(funx, funy, funwidth, funheight)
        self.color = funcolor
        self.font = funfont
        self.text = funtext

    def draw(self, screen, adjust = [0,0]):
        txt = self.font().render(self.text(), True, self.color())
        screen.blit(txt, add_lists((self.x(), self.y()),adjust))


class textrenderable1(renderable):
    def __init__(self, x, y, color, font, text, width = 40, height = 40):
        super().__init__(x, y, width, height)
        self.color = color
        self.font = font
        self.text = text

    def draw(self, screen, adjust = [0,0]):
        txt = self.font.render(self.text, True, self.color)
        screen.blit(txt, add_lists((self.x, self.y),adjust))

class barrenderable(rectrenderable):
    def __init__(self, x, y, w, h, bgcolor, fgcolor, numfun, bordered = False, width = 40, height = 40):
        super().__init__(x, y, w, h, width, height)
        self.bgcolor, self.fgcolor = bgcolor, fgcolor
        self.bordered = bordered
        self.numfun = numfun

    def draw(self, screen, adjust = [0,0]):
        pygame.draw.rect(screen, self.bgcolor, (self.x + adjust[0], self.y + adjust[1], self.w, self.h), 1 if self.bordered else 0)
        (curr, max) = self.numfun()
        pygame.draw.rect(screen, self.fgcolor, (self.x + adjust[0], self.y + adjust[1], round(self.w * curr / max), self.h))
        

class barrenderable_changeble(rectrenderable_changeble):
    def __init__(self, funx, funy, funw, funh, funbgcolor, funfgcolor, funnum, funbordered = lambda:False, funwidth = lambda:40, funheight = lambda: 40):
        super().__init__(funx, funy, funw, funh, funwidth, funheight)
        self.bgcolor, self.fgcolor = funbgcolor, funfgcolor
        self.bordered = funbordered
        self.funnum = funnum

    def draw(self, screen, adjust = [0,0]):
        pygame.draw.rect(screen, self.bgcolor(), (self.x() + adjust[0], self.y() + adjust[1], self.w(), self.h()), 1 if self.bordered() else 0)
        (curr, max) = self.funnum()
        pygame.draw.rect(screen, self.fgcolor(), (self.x() + adjust[0], self.y() + adjust[1], round(self.w() * curr / max), self.h()))

class playerrenderable(rectrenderable ):
    def __init__(self, plr, width = 40, height = 40):
        super().__init__(plr.x - 50, plr.y - 50, 100, 100, width, height)
        self.plr = plr
    
    def draw(self, screen, adjust = [0,0]):
        #the player:
        if self.plr.stage == 1:
            pygame.draw.circle(screen, self.plr.color, self.plr.pos, 50)
        else:
            pygame.draw.rect(screen, self.plr.color, self.rect)

        #olhinhos
        (x, y) = self.plr.pos
        pygame.draw.circle(screen, (0,0,0), (x-10, y-30), 5)
        pygame.draw.circle(screen, (0,0,0), (x-10, y-30), 1)
        
        pygame.draw.circle(screen, (0,0,0), (x+10, y-30), 5)
        pygame.draw.circle(screen, (0,0,0), (x+10, y-30), 1)
        
        