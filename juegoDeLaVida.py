import pygame
from pygame.locals import *
import numpy as np
import time
import sys

pygame.init()

width, height= 600, 600
screen = pygame.display.set_mode((height, width), pygame.RESIZABLE)

bg = 25, 25, 25

screen.fill(bg)

nxC, nyC = 50, 50

dimCW = (width - 1) /nxC
dimCH = (height -1)/nyC

gameState = np.zeros((nxC, nyC))

""" gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1 """

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

pauseExect = False 
while 1:

    newGameState = np.copy(gameState)

    
    
        
    
    ev = pygame.event.get()


    for event in ev:
        if event.type == pygame.KEYDOWN:        # comprobar si se quiera pausar
            pauseExect = not pauseExect

        if event.type == pygame.QUIT:          # comprobar si se quiere cerrar el juego
            sys.exit (0)
        
        mouseClick = pygame.mouse.get_pressed()     #comprobar si se pulso el mouse para modificar estado de celdas

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState [celX, celY]= not mouseClick[2]

    screen.fill(bg)

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:
                

                n_neigh =   gameState[(x-1)% nxC, (y-1) % nyC] + \
                            gameState[(x)% nxC, (y-1) % nyC] + \
                            gameState[(x+1)% nxC, (y-1) % nyC] + \
                            gameState[(x-1)% nxC, (y) % nyC] + \
                            gameState[(x+1)% nxC, (y) % nyC] + \
                            gameState[(x-1)% nxC, (y+1) % nyC] + \
                            gameState[(x)% nxC, (y+1) % nyC] + \
                            gameState[(x+1)% nxC, (y+1) % nyC]
                
                if gameState[x, y] == 0 and n_neigh ==3:
                    newGameState[x, y] = 1
                elif gameState[x, y]== 1 and (n_neigh<2 or n_neigh>3):
                    newGameState[x, y] = 0
                
                
                            

            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]
            
        
            if newGameState[x, y]==0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1) # color rejila
            else:
                pygame.draw.polygon(screen, (128, 228, 50), poly, 0) #color autómatas
            
                
                
                
    time.sleep(1/30)
    gameState = np.copy(newGameState)
    pygame.display.flip()
     

             


    # pass