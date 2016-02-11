import pygame
import numpy as np 
import time

pygame.init()
width,height = 1000, 1000
screen = pygame.display.set_mode((height , width))
bg = 255,255,255

screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width/nxC
dimCH = height/nyC

#estado de las cerdas vivas
gameState = np.zeros((nxC,nyC))

#automata
gameState[5, 3] = 1

gameState[5, 10] = -1

gameState[4, 12] = -1
gameState[0, 11] = -1
#automata
gameState[0, 12] = -1
gameState[0, 13] = -1
gameState[1, 13] = -1
gameState[2, 13] = -1
gameState[3, 13] = -1
gameState[4, 13] = -1
gameState[5, 13] = -1
gameState[6, 13] = -1
gameState[7, 13] = -1
gameState[8, 13] = -1
gameState[9, 13] = -1
gameState[10, 13] = -1
gameState[11, 13] = -1
gameState[12, 13] = -1
gameState[13, 13] = -1
gameState[14, 13] = -1
gameState[15, 13] = -1
gameState[16, 13] = -1
gameState[16, 12] = -1
gameState[16, 11] = -1
gameState[11, 12] = -1

solido = -1
liquido = 1
aire = 0

pause = False
#bucle de ejecucion
while True:
	time.sleep(0.5)

	screen.fill(bg)
	newGameState=np.copy(gameState)
	#registramos eventos en el teclado y raton
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.KEYDOWN:
			pause = not pause
		mouseClick = pygame.mouse.get_pressed()
		if sum(mouseClick)>0:
			posX,posY = pygame.mouse.get_pos()
			celX,celY = int(np.float(posX / dimCW)), int(np.float(posY / dimCH))
			newGameState[celX,celY] = 1
			if mouseClick[2]==1:
				newGameState[celX,celY] = -1

	
	for y in range(0,nyC):
		for x in range(0,nxC):
			if not pause:
				down  = gameState[(x)% nxC ,(y+1)% nyC]
				up    = gameState[(x)% nxC ,(y-1)% nyC]
				left  = gameState[(x-1)% nxC,(y)% nyC]
				right = gameState[(x+1)% nxC,(y)% nyC]
				#regla 1: si estado es solido entonces permanece igual 
				if gameState[x,y] == solido:
					newGameState[x,y] = solido
				#regla 2: si estado es liquido su vecino de abajo es aire entonces 
				#el vecino de abajo es sutituido por liquido
				if gameState[x,y] == liquido and down==aire:
					yi = y + 1
					newGameState[x,yi] = liquido
				#regla 3: si estado es liquido su vecino de abajo es solido entonces 
				#liquido se detiene y pregunta por sus vecinos laterales 
				if (gameState[x,y] == liquido and down==solido) or (gameState[x,y] == liquido and down==liquido):
					print('regla 3')
					if (left==solido and right==solido) or (left==liquido and right==liquido):
						if up == aire:
							yi = y - 1
							newGameState[x,yi] = liquido
						else:
							newGameState[x,y] = gameState[x,y]

					if (left==solido and right==aire) or (left==liquido and right==aire):
						print('regla 3- solido y aire')
						xi = x + 1
						newGameState[xi,y] = liquido

					if (left==aire and right==solido) or (left==aire and right==liquido):
						print('regla 3- aire y solido',x)
						xi = x- 1
						newGameState[xi,y] = liquido
						print('regla 3- aire y solido',x)

					if left==aire and right==aire:
						print('regla 3- aire y aire')
						xi = x - 1
						xa = x + 1
						newGameState[xi,y] = liquido
						newGameState[xa,y] = liquido


				poly=[
					((x) * dimCW, y * dimCH),
					((x+1) * dimCW, y * dimCH),
					((x+1) * dimCW, (y+1) * dimCH),
					((x) * dimCW, (y+1) * dimCH)
				]
				if newGameState[x,y]==1:

					pygame.draw.polygon(screen,(17, 85, 204),poly,0)
				elif newGameState[x,y]==-1:
					pygame.draw.polygon(screen,(0,0,0),poly,0)


	#actualizar el estado actual
	gameState = np.copy(newGameState)
	#actualizamos la pantalla
	pygame.display.flip()
