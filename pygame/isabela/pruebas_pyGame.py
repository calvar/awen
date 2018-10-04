import pygame, sys 
from pygame.locals import*
#pygame.init() obligatoria
pygame.init()
#crea la ventana
ventana = pygame.display.set_mode((500,500))
#imprime un mensaje en la ventana
#pygame.display.set_caption("hola mundo")
ColorF = (240,248,255)
ColorL = (89,100,120)
x1 = 50
y1=50
x2= 50
y2=450
posX = 50
posY = 50
Barco = pygame.image.load("BARCO.png")
reSize = pygame.transform.scale(Barco, [100,100])
vel =1
intrucion = "turnLeft"
num = 3
contador =0;
direcion =1;
#(lienzo, color, cordenada inicio, cordendasfinal)
#pygame.draw.line(ventana, ColorL, (50,450),(80,40),2)
#mostrar la ventana loop infinito
while(True):
	ventana.fill(ColorF)
	pygame.draw.line(ventana, ColorL, (50,50), (50,450),2)
	pygame.draw.line(ventana, ColorL, (100,50), (100,450),2)
	pygame.draw.line(ventana, ColorL, (150,50), (150,450),2)
	pygame.draw.line(ventana, ColorL, (200,50), (200,450),2)
	pygame.draw.line(ventana, ColorL, (250,50), (250,450),2)
	pygame.draw.line(ventana, ColorL, (300,50), (300,450),2)
	pygame.draw.line(ventana, ColorL, (350,50), (350,450),2)
	pygame.draw.line(ventana, ColorL, (400,50), (400,450),2)
	pygame.draw.line(ventana, ColorL, (450,50), (450,450),2)
	ventana.blit(reSize,(posX, posY))
			
	
	for evento in pygame.event.get():	
		#esta pendiente de que se cierre la ventana
		if evento.type ==QUIT:
			pygame.quit()
			sys.exit()
	if(intrucion=="turnRigth"):
		direcion +=1
		direcion = direcion %4
	if(intrucion=="turnLeft"):
		if(direcion ==0):
			direcion = 4
		direcion -=1
		direcion = direcion %4
		
	if(intrucion=="move"and contador<50*num):
		if(direcion == 0):
			posY-=1
		elif(direcion ==1):
			posX+=1
		elif(direcion==2):
			posY+=1
		elif(direcion==3):
			posX-=1
		contador+=1
		pygame.time.wait(100)
	contador=0;
	intrucion = "move"
	#pygame.quit()	
	pygame.display.update()
	#eventos
	
