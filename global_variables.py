#############################################################################################################################
#############################################################################################################################
        #este tem variáveis e funções auxiliares, consideradas "globais" que podem ser acedidas por todos os módulos
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

from math import *
import random as R

screen_width = 1200
screen_height = 720


number_of_squares_width = 30
number_of_squares_height = 18


square_height = screen_height / number_of_squares_height
square_width = screen_width / number_of_squares_width


range_major_messages = 80
range_minor_messages = 80

cost_major_messages = 2
cost_minor_messages = 1

#x_global = R.randint(-2,2)
#y_global = R.randint(-2,2)
#x1_global = R.randint(-2,2)
#y1_global = R.randint(-2,2)
        
water_x = 2 #+ x_global
water_y = 2 #+ y_global

life_x = 27 #+ x1_global
life_y = 8 #+ y1_global

                
#square_width = 42
#square_height = 42

#number_of_squares_width = floor(screen_width / square_width)
#number_of_squares_height = floor(screen_height / square_height)

print(square_height)
print(square_width)

def manhatan_distance(x1,y1,x2,y2):
    if x1 > x2:
        if y1 > y2:
            return x1 - x2 + y1 - y2
        else:
            return x1 - x2 + y2 - y1
    else:
        if y1 > y2:
            return x2 - x1 + y1 - y2
        else:
            return x2 - x1 + y2 - y1


            