#############################################################################################################################
#############################################################################################################################
        #aqui é programado o ambiente, o planeta de marte
        
        #o objeto "mars" é chamado antes da simulação começar e inicializa o mapa, os agentes e os tempos aleatorios para a proxima tempestade e a sua duração
        
        #em cada iteração... é chamada a funçao "effect", que calcula tudo o que acontece numa iteração, e depois é chamada a "draw" que muda a imagem vista.
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

import random as R

from renderable import *
from global_variables import *
from terrain import *
from agent import *

from math import *
import pygame
#import numpy as np
import pandas as pd


class mars():

    def __init__(self,with_prints = True, number_of_iterations = 50000):
        self.name = "0"
        self.renderables = []
        
        self.terrain = self.make_map()
        
        self.agents = self.make_agents()
        
        self.time_until_storm = R.randint(50,80)
        
        self.storm_duration = 0
        
        self.is_storm_active = False
        
        self.iteration = 0
        
        self.show_known_map = False
        self.show_known_samples = False
        
        
        self.with_prints = with_prints
        
        self.number_of_iterations = number_of_iterations
        
        #self.make_map()

    def make_map(self):
        r = []
        
        #vamos adicionar montanhas todas à volta do mapa para eles nao poderem sair:
        r.append(mountain(-1,-1))
        r.append(mountain(-1,number_of_squares_height))
        r.append(mountain(number_of_squares_width,-1))
        r.append(mountain(number_of_squares_width,number_of_squares_height))
        for i in range(number_of_squares_width):
            r.append(mountain(i,-1))
            r.append(mountain(i,number_of_squares_height))
            
        for i in range(number_of_squares_height):
            r.append(mountain(-1,i))
            r.append(mountain(number_of_squares_width,i))

                
        for i in range(number_of_squares_width):
            for j in range(number_of_squares_height):
            
                
                if (i,j) == (life_x,life_y):
                    r.append(flat(i,j, has_life = True))
                    #print("a vida é em " + str((i,j)))
                    

                #elif (i,j) == (floor(number_of_squares_width/4) , floor(number_of_squares_height/4)):
                #    r.append(flat(i,j, has_water = True))
                    
                #elif (i,j) == (floor(number_of_squares_width/4) , floor(3*number_of_squares_height/4)):
                #    r.append(flat(i,j, has_water = True))
                    
                #elif (i,j) == (floor(3*number_of_squares_width/4) , floor(3*number_of_squares_height/4)):
                #    r.append(flat(i,j, has_water = True))
                
                #elif (i,j) == (floor(3*number_of_squares_width/4) , floor(number_of_squares_height/4)):
                #    r.append(flat(i,j, has_water = True))
                    
                  
                elif (i,j) == (water_x,water_y):
                    r.append(flat(i,j, has_water = True))
                    #print("a agua é em " + str((i,j)))
                
                elif 22 <= i <= 24 and  2 <= j <= 14:
                    r.append(mountain(i, j))
                    
                elif 25 <= i <= 28 and  11 <= j <= 14:
                    r.append(mountain(i, j))
                    
                elif 2 <= i <= 4 and  7 <= j <= 8:
                    r.append(mountain(i, j))
                
                elif 19 <= i <= 28 and  1 == j :
                    r.append(rocky(i, j))
                    
                elif 3 <= i <= 6 and  13 <= j <= 16:
                    r.append(rocky(i, j))

                elif 6 <= i <= 6 and  1 <= j <= 8:
                    r.append(rocky(i, j))
                    
                elif (i,j) in [(10,8),(15,13),(16,2),(4,17),(3,9),(18,19),(7,4),(20,10),(17,7),(12,15), (13,13),(13,5),(9,2),(16,12),(9,14)]:
                    r.append(rocky(i, j))
                
                else:
                    r.append(flat(i, j))
                    #r.append(terrain(i, j, "flat")) #self.renderables.append(rectrenderable(rect_height*i + 5,rect_width*j + 5,rect_height - 10,rect_width - 10, (0,0,150)))
        
        
        return r

    def make_agents(self):
        r = []
        
        
        #r.append(reactive_rover2(14,8,self))
        
        #r.append(reactive_rover4(14,8,self))
        
        r.append(rover_warning_storm(14,8,self))
        
        #r.append(learning_rover5(14,8,self))
        
        #r.append(learned_rover5(14,8,self))
        
        return r

    def draw(self, screen):
        for r in self.renderables:
            r.draw(screen)
            
        for t in self.terrain:
            t.draw(screen)
            
        for a in self.agents:
            #isto é para desenhar quando se quer ver qual é o mapa conhecido do rover ou as samples que ele sabe
            if a.agent_type == "rover":
                a.draw(screen, self.show_known_map, self.show_known_samples)
            else:
                a.draw(screen)
    def effect(self):
        #cenas a ver com tempestade:
        
        #iterar os tempos:
        self.time_until_storm -= 1
        self.storm_duration -= 1
        
        #aqui começa a storm: calculamos os tempos até ela terminar e até a próxima começar
        if self.time_until_storm <= 0:
            
            storm_duration = R.randint(5,15)
            
            #time_until_storm = R.randint(10,30)
            time_until_storm = R.randint(50,80)
            
            self.time_until_storm = storm_duration + time_until_storm
        
            self.storm_duration = storm_duration
            
            self.is_storm_active = True
            
        #aqui é quando a storm termina:
        if self.storm_duration <= 0 and self.is_storm_active:
            self.is_storm_active = False
            
            
        #print("time_until_storm: " +str(self.time_until_storm))
        #print("storm_duration: " +str(self.storm_duration))
        #print("is_storm_active: " +str(self.is_storm_active))
        
        for i in self.terrain:
            i.effect()
            
        for i in self.agents:
            i.effect()
            
        #print()
        self.iteration += 1
        if self.iteration%25000 == 0:
            print("ITERATION: " + str(self.iteration))
        #print()
        
        #verificar se a simulação acabou:
        for i in self.agents:
            if i.agent_type == "rover":
                if (i.found_life and i.found_water): #or (i.miners_eliminated == 2):
                    
                    return self.end() #False
        if self.iteration > self.number_of_iterations:
            #print("MAIS DE "+str(self.number_of_iterations)+" ITERAÇOES ###################################################################################################")
            return self.end()
        return True,0,0,0,0,0,0
        
        
        
    def create_sample(self, x, y):
        pass
        
    def end(self):
        if self.with_prints:
            print()
            print()
            print()
            print("RESULTADO DA SIMULAÇÃO!")
            print()
            print()
            print()
            print()
        for i in self.agents:
            if i.agent_type == "rover":
                known_terrain = len(i.known_terrain)
                if self.with_prints:
                    print("terreno conhecido pelo rover: " + str(known_terrain))
                    print()
                #ver se ele descobriu a vida e a agua
                found_water = False
                found_life = False
                for j in i.known_terrain:
                    if j[3] == 0:
                        found_water = True
                        water_position = (j[1],j[2])
                    if j[4] == 0:
                        found_life = True
                        life_position = (j[1],j[2])
                if self.with_prints:        
                    if found_water:
                        print("THE SYSTEM FOUND WATER AT " + str(water_position))
                    else:
                        print("The system did not find water...")
                    print()
                    if found_life:
                        print("THE SYSTEM FOUND LIFE AT " + str(life_position))
                    else:
                        print("The system did not find life...")
                    print()
            #ver se ele descobriu a vida e a agua
        
        energia_total = 0
        for i in self.agents:
            energia_total += i.energy_spent
            if i.agent_type == "rover":
                for j in i.carried_drones + i.carried_miners:
                    energia_total += j.energy_spent
        if self.with_prints:
            print("energia total gasta pelo sistema: " + str(energia_total))
            print()
            print("número total de iterações: " + str(self.iteration))
            print()
        score = -1 * self.iteration -2*energia_total + 20*known_terrain
        water = 0
        life = 0
        if found_water:
            score += 10000
            water = 1
        if found_life:
            score += 10000
            life = 1
        if self.with_prints:
            print("SCORE TOTAL: " + str(score))
        
        for i in self.agents:
            if i.agent_type == "rover" and i.im_learning:
                if i.Q_matrix != []:
                    print("GUARDEI A Q_matrix!!!!!!!")
                    df = pd.DataFrame(data=i.Q_matrix)#.astype(float))
                    df.to_csv('Q_matrix.csv', sep=' ', header=False, float_format='%.2f', index=False)
                    
                    
                    policy = []
                    for j in i.Q_matrix:
                        policy.append(  i.possible_actions[j.index(max(j))]  )
                    df2 = pd.DataFrame(data=policy)#.astype(float))
                    df2.to_csv('policy.csv', sep=' ', header=False, float_format='%.2f', index=False)
            
            

        
        return False,life,water,energia_total,self.iteration,known_terrain,score
        
    def clicked_m(self):
        self.show_known_map = not self.show_known_map
        
    def clicked_s(self):
        self.show_known_samples = not self.show_known_samples
            
            
#############################################################################################################################
#############################################################################################################################
        #informações que os agentes podem precisar do ambiente:
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
    
    
    def is_occupied(self, x, y):
        r = False
        for i in self.terrain:
            if i.terrain_type == "mountain" and i.fun_pos() == (x,y):
                r = True
        #se se tirar este ciclo, então agents podem passar uns por cima dos outros:
        #for i in self.agents:
        #    if i.fun_pos() == (x,y):#and i.agent_type == "rover": <- isto seria se quisessemos que "só não podem estar em cima do rover" 
        #        r = True
        
        #if x < 0 or x >= number_of_squares_width or y < 0 or y >= number_of_squares_height:
            #isto é para eles n sairem do mapa
        #    r = True
        return r
        
    #def time_until_storm(self):
    #    return self.time_until_storm
        
    def is_storm_active(self):
        return self.is_storm_active
        
        
    #a informaçao que os agentes vao ter sobre o mapa sao informaçoes do tipo
    #[terrain type, x, y, distance to water, distance to life],
    #distance to water e life sao -1 se o agente nao souberem nada
    
    def what_terrain(self,x,y):
        for i in self.terrain:
            if i.fun_pos() == (x,y):
                return [i.terrain_type,x,y,-1,-1]
                
        
    def get_samples(self,x,y):
        r = []
        for i in self.terrain:
            for j in i.samples:
                if j.fun_pos() == (x,y):
                    r.append(j)
        return r
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
            
    # def receiveevent(self, event):
        # print("cliquei aqui: " + str(event.pos))
        # return self
        
    # def receiveevent1(self, event, screen):
        # return self
        
    # def key_type(self, key):
        # #print(key)
        
        # if key == pygame.K_q:
            # w, h = pygame.display.get_surface().get_size()
            # print("tamanho aqui!: "+str(w) + " x " + str(h))
            # print([gstate.get().width, gstate.get().height,gstate.get().current_width, gstate.get().current_height,gstate.get().full_width, gstate.get().full_height])
            
        # elif key == pygame.K_F4:
            # pygame.display.quit()
            # pygame.display.init()
            # if gstate.get().fullscreen:
                # gstate.get().screen = pygame.display.set_mode((gstate.get().width, gstate.get().height))
                # gstate.get().current_width, gstate.get().current_height = gstate.get().width, gstate.get().height
            # else:
                # gstate.get().screen = pygame.display.set_mode((gstate.get().full_width,gstate.get().full_height),pygame.FULLSCREEN)
                # gstate.get().current_width, gstate.get().current_height = gstate.get().full_width, gstate.get().full_height
                
            # gstate.get().arena_width = gstate.get().current_width - 300
            # gstate.get().arena_height = gstate.get().current_height - 60
            
            # gstate.get().arena = gstate.get().arena.recreate_arena()
            
            # gstate.get().fullscreen = not gstate.get().fullscreen

        
        
    # def write(self, surface, te, pos, width , font, color=(200,0,0)):
        # words = [word.split(' ') for word in te.splitlines()]  # 2D array where each row is a list of words.
        # space = font.size(' ')[0]  # The width of a space.
        # x, y = pos
        # max_width = x + width
        # for line in words:
            # for wo in line:

                # wo_surface = font.render(wo, 0, color)
                # wo_width, wo_height = wo_surface.get_size()
                # if x + wo_width >= max_width:
                    # x = pos[0]  # Reset the x.
                    # y += wo_height  # Start on new row.
                # a = textrenderable1(x, y, color, font, wo)
                # self.renderables.append(a)
                # #self.temporaryrenderables.append(a)
                # x += wo_width + space
            # x = pos[0]  # Reset the x.
            # y += wo_height  # Start on new row.
            
    # def write_centered(self, surface, te, pos, width , font, color=(200,0,0)):
        # self.write(surface, te, [pos[0]-width/2,pos[1]],width,font,color)
       
        

            


