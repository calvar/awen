import re

def BasicWrite(image_path):
	intr=["turnRigth", "move"]
	times=["1","2"]
	print("Basic Write Done")
	x1=50
	y1=50
	
	salida = open ("AwenCode.py", "w")
	salida.write("import pygame, sys \nfrom pygame.locals import*\n")
	salida.write("pygame.init()\nventana = pygame.display.set_mode((500,500))\n")
	salida.write("pygame.display.set_caption(\"Awen\")\n")
	salida.write("ColorF=(240,248,255)\nColorL=(0,0,0)\n")
	salida.write("x1 = 50\ny1=50\nx2= 50\ny2=450\n")
	salida.write("posX=50\nposY=50\n")
	salida.write("Barco = pygame.image.load(\""+image_path+"BARCO.png\")\nreSize = pygame.transform.scale(Barco, [40,40])\n")
	salida.write("vel=1\nnum=3\ncontador=0\ndirecion =1\n")
	salida.write("while(True):\n")
	salida.write("\tventana.fill(ColorF)\n")
	for i in range (0,9):
		salida.write("\tpygame.draw.line(ventana, ColorL, ("+str(x1)+","+str(50)+"), ("+str(x1)+","+str(450)+"),"+str(2)+")\n")
		salida.write("\tpygame.draw.line(ventana, ColorL, ("+str(50)+","+str(y1)+"), ("+str(450)+","+str(y1)+"),"+str(2)+")\n")
		x1=x1+50
		y1=y1+50
	salida.write("\tventana.blit(reSize,(posX, posY))\n")
	salida.write("\tfor evento in pygame.event.get():\n")
	salida.write("\t \tif evento.type==QUIT:\n")
	salida.write("\t \t \tpygame.quit()\n")
	salida.write("\t \t \tsys.exit()\n")


	
	for i in range(0, len(times)):
		print("Instruction Write Done")
		if(intr[i] =="turnRigth"):
			for j in range(0,int(times[i])):
				salida.write("\tdirecion +=1\n\tdirecion = direcion %4\n")
		elif(intr[i]=="turnLeft"):
			for j in range(0, int(times[i])):
				salida.write("\tif(direcion ==0):\n\t\t	direcion = 4\n\tdirecion -=1\n\tdirecion = direcion %4\n")
		elif (intr[i]=="move"):
			for j in range(0, int(times[i])):
				salida.write("\twhile(contador<50):\n\t\tif(direcion==0):\n\t\t\tposY-=1\n\t\telif(direcion==1):")
				salida.write("\n\t\t\tposX+=1\n")
				salida.write("\t\telif(direcion==2):\n\t\t\tposY+=1\n\t\telif(direcion==3):\n")
				salida.write("\t\t\tposX-=1\n\t\tcontador+=1\n")
				salida.write("\t\tpygame.time.wait(100)\n\tcontador=0\n")
	salida.write("\tpygame.display.update()")


image_path = "/home/carlos/Documents/Materias_MACC/semillero/awen/pygame/isabela/"
        

BasicWrite(image_path)

