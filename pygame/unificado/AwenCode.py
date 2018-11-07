import pygame, sys 
from pygame.locals import*
pygame.init()
ventana = pygame.display.set_mode((500,500))
pygame.display.set_caption("Awen")
ColorF=(240,248,255)
ColorL=(0,0,0)
x1 = 50
y1=50
x2= 50
y2=450
posX=50
posY=50
paso = 50
Barco = pygame.image.load("/home/carlos/Documents/Materias_MACC/semillero/git_repo/awen/pygame/unificado/barco1.png")
reSize = pygame.transform.scale(Barco, [40,40])
vel=1
num=3
#contador=0
direcion =1
while(True):
	ventana.fill(ColorF)
	pygame.draw.line(ventana, ColorL, (50,50), (50,450),2)
	pygame.draw.line(ventana, ColorL, (50,50), (450,50),2)
	pygame.draw.line(ventana, ColorL, (100,50), (100,450),2)
	pygame.draw.line(ventana, ColorL, (50,100), (450,100),2)
	pygame.draw.line(ventana, ColorL, (150,50), (150,450),2)
	pygame.draw.line(ventana, ColorL, (50,150), (450,150),2)
	pygame.draw.line(ventana, ColorL, (200,50), (200,450),2)
	pygame.draw.line(ventana, ColorL, (50,200), (450,200),2)
	pygame.draw.line(ventana, ColorL, (250,50), (250,450),2)
	pygame.draw.line(ventana, ColorL, (50,250), (450,250),2)
	pygame.draw.line(ventana, ColorL, (300,50), (300,450),2)
	pygame.draw.line(ventana, ColorL, (50,300), (450,300),2)
	pygame.draw.line(ventana, ColorL, (350,50), (350,450),2)
	pygame.draw.line(ventana, ColorL, (50,350), (450,350),2)
	pygame.draw.line(ventana, ColorL, (400,50), (400,450),2)
	pygame.draw.line(ventana, ColorL, (50,400), (450,400),2)
	pygame.draw.line(ventana, ColorL, (450,50), (450,450),2)
	pygame.draw.line(ventana, ColorL, (50,450), (450,450),2)
        
	for evento in pygame.event.get():
	 	if evento.type==QUIT:
	 	 	pygame.quit()
	 	 	sys.exit()

        #move
        contador = 0
	while(contador<150):
                ventana.blit(reSize,(posX, posY))
		if(direcion==0):
			posY-=paso
		elif(direcion==1):
			posX+=paso
		elif(direcion==2):
			posY+=paso
		elif(direcion==3):
			posX-=paso
		contador+=paso
                pygame.display.update()
	        pygame.time.wait(1000)


        
        # # #move
        # contador=0
	# while(contador<100):
	# 	if(direcion==0):
	# 		posY-=paso
	# 	elif(direcion==1):
	# 		posX+=paso
	# 	elif(direcion==2):
	# 		posY+=paso
	# 	elif(direcion==3):
	# 		posX-=paso
	# 	contador+=paso
	#         pygame.time.wait(100)

        # ventana.blit(reSize,(posX, posY))
        
        # #turnLeft
	# if(direcion ==0):
	# 		direcion = 4
	# direcion -=1
	# direcion = direcion %4

        # #turnRight
	# direcion +=1
	# direcion = direcion %4
	# direcion +=1
	# direcion = direcion %4

        # #move
        # contador=0
	# while(contador<100):
	# 	if(direcion==0):
	# 		posY-=paso
	# 	elif(direcion==1):
	# 		posX+=paso
	# 	elif(direcion==2):
	# 		posY+=paso
	# 	elif(direcion==3):
	# 		posX-=paso
	# 	contador+=paso
	#         pygame.time.wait(100)
        
	
