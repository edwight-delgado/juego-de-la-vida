import pygame
import numpy as np 
import time

pygame.init()
width,height = 1000, 1000
screen = pygame.display.set_mode((height , width))
bg = 25,25,25

screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width/nxC
dimCH = height/nyC

#estado de las cerdas vivas
gameState = np.zeros((nxC,nyC))

#automata
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

#automata
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#bucle de ejecucion
while True:
	time.sleep(0.5)

	screen.fill(bg)
	newGameState=np.copy(gameState)
	for y in range(0,nxC):
		for x in range(0,nyC):

			#calculamos el numero de vecinos cercanos
			n_neigh = gameState[(x-1)% nxC,(y-1)% nyC]+\
					  gameState[(x) % nxC,(y-1)% nyC]+\
					  gameState[(x+1)% nxC,(y-1)% nyC]+\
					  gameState[(x-1)% nxC,(y)% nyC]+\
					  gameState[(x+1)% nxC,(y)% nyC]+\
					  gameState[(x-1)% nxC ,(y+1)% nyC]+\
					  gameState[(x)% nxC ,(y+1)% nyC]+\
					  gameState[(x+1)% nxC ,(y+1)% nyC]
			#regla1 una cedula muerta con exatamente 3 vecinos vivos, revive 
			if gameState[x,y] == 0 and n_neigh == 3:
				newGameState[x,y] = 1
				#print(n_neigh)
				#print(newGameState[x,y])

			#regla2 una cedula viva con menos de 2 o mas de 3 vecinos vivas, mueren
			if gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
				newGameState[x,y] = 0
			poly=[
				((x) * dimCW, y * dimCH),
				((x+1) * dimCW, y * dimCH),
				((x+1) * dimCW, (y+1) * dimCH),
				((x) * dimCW, (y+1) * dimCH)
			]
			if newGameState[x,y]==1:

				pygame.draw.polygon(screen,(255,255,255),poly,0)
			else:
				pygame.draw.polygon(screen,(128,128,128),poly,1)
	#actualizar el estado actual
	gameState = np.copy(newGameState)
	#actualizamos la pantalla
	pygame.display.flip()
