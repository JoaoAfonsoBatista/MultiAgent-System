#############################################################################################################################
#############################################################################################################################
        #esta é a função "main", a que é chamada, tem um ciclo onde chama todas as outras, para calcular o que acontece numa iteraçao,
        #e atualiza o ecra. tb define o que acontece quando se clica em teclas,
        #se se clicar em "p", a simulaçao entre/sai em pausa,
        #se se clicar nos numeros 1,2,3,4,...,9,0, muda a velocidade da simulaçao, onde 1 é o mais lento e 0 é o mais rapido
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

import random as R
import sys
import pygame

from mars import *
from global_variables import *

from time import time 

#import ctypes
#user32 = ctypes.windll.user32
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#print(screensize)

pygame.init()

#full_width, full_height = screensize

#ctypes.windll.user32.SetProcessDPIAware()
#true_res = (windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1))
#pygame.display.set_mode(true_res,pygame.Fullscreen)

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#current_width = 600
#current_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#screen = pygame.display.set_mode((200, 60))

#mars1 = mars()

#time_per_iteration = 1000
time_per_iteration = 0
#time_per_iteration = 100


pause = False
#pause = True

number_of_simulations = 10

added_score = 0
number_of_found_life = 0
number_of_found_water = 0
added_energy = 0
added_steps = 0
added_map = 0
clicked_e = False

time_start = time()
#______________________________________________________________________________________________________________________________________________________________________
global run
#main loop
run = True
i = 0
while i < number_of_simulations:
    print("simulação: " + str(i))
    run = True
    mars1 = mars(False)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #nao sei como ver se se clicou no lado esquerdo ou direito do rato... o lado esquerdo é 1 e o lado esquerdo é 3
                    pass
                    #fazer coisas game_phase = game_phase.receiveevent(event)

                elif event.button == 3:
                    print(str(event.pos))
                    #game_phase = game_phase.receiveevent1(event, gstate.get().screen)
                    
            if event.type == pygame.KEYDOWN:
                    
                #game_phase = game_phase.key_type(event.key)

                if event.key == pygame.K_DELETE:
                    run = False
                #elif event.key == pygame.K_o:
                #    game_phase.renderables.append(rectrenderable(100,100,200,200,(255,0,0,150)))
                #elif event.key == pygame.K_i:
                #    print(game_phase.name)
                elif event.key == pygame.K_F2:
                    pass
                elif event.key == pygame.K_p:
                    pause = not pause
                elif event.key == pygame.K_1:
                    time_per_iteration = 1000
                elif event.key == pygame.K_2:
                    time_per_iteration = 700
                elif event.key == pygame.K_3:
                    time_per_iteration = 400
                elif event.key == pygame.K_4:
                    time_per_iteration = 200
                elif event.key == pygame.K_5:
                    time_per_iteration = 100
                elif event.key == pygame.K_6:
                    time_per_iteration = 50
                elif event.key == pygame.K_7:
                    time_per_iteration = 25
                elif event.key == pygame.K_8:
                    time_per_iteration = 10
                elif event.key == pygame.K_9:
                    time_per_iteration = 1
                elif event.key == pygame.K_0:
                    time_per_iteration = 0
                    
                elif event.key == pygame.K_e:
                    mars1.end()
                    run = False
                    pause = True
                    i = number_of_simulations
                    print("clicked e")
                elif event.key == pygame.K_m:
                    mars1.clicked_m()
                elif event.key == pygame.K_s:
                    mars1.clicked_s()
        #game_phase = game_phase.clock()
        if pause:
            pygame.time.wait(500)
        else:
            #mars = mars.effect()
            
            run,life_1,water_1,energy_1,steps_1,map_1,score_1 = mars1.effect()
            added_score += score_1
            number_of_found_life += life_1
            number_of_found_water += water_1
            added_energy += energy_1
            added_steps+= steps_1
            added_map += map_1
            #mars1.draw(screen)
            #pygame.display.update()

            pygame.time.wait(time_per_iteration)
    i += 1
print("over " + str(number_of_simulations) + " simulations: " )
print("found life " +str(number_of_found_life*100/number_of_simulations) + "% of the times")
print("found water " + str(number_of_found_water*100/number_of_simulations) + "% of the times")
print("found, on average, " + str(added_map/number_of_simulations) + " tiles")
print("spent, on average, " + str(added_energy/number_of_simulations) + " energy")
print("took, on average, " + str(added_steps/number_of_simulations) + " steps")
print()
print("average score is: " + str(added_score/number_of_simulations))

print("took, on average: " + str((time()-time_start) / number_of_simulations) + " seconds to simulate")

pygame.quit()
