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

mars = mars(True, 10000)

time_per_iteration = 1000
#time_per_iteration = 0
#time_per_iteration = 100
#time_per_iteration = 500
mars.show_known_samples = True
mars.show_known_map = True

pause = False
#pause = True
#______________________________________________________________________________________________________________________________________________________________________
global run
#main loop
run = True
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
                mars.end()
                run = False
                pause = True
            elif event.key == pygame.K_m:
                mars.clicked_m()
            elif event.key == pygame.K_s:
                mars.clicked_s()
    #game_phase = game_phase.clock()
    if pause:
        pygame.time.wait(500)
    else:
        #mars = mars.effect()
        
        run = mars.effect()[0]
        mars.draw(screen)
        pygame.display.update()

        pygame.time.wait(time_per_iteration)
    

pygame.quit()
