"""Archivo: CompiladorTurtle
funcion: este programa lee un archivo txt, compila y crea otro archivo(intrucciones.txt) con las intrucciones traducidas a lenguaje turtle .En caso dado de que halla errores en el codigo fuente el programa se queja y arroja error"""
import re




"""regular expressions: space intruccion space (number) space"""
def regularE(world, numL):
	
	spc = '(\s*)'
	action = '(move|turnLeft|turnRight|attack)'
	parOpen = '(\()'
	digit = '(\d*)'
	parClose = '(\))'
	intruction = spc+action+spc+parOpen+spc+digit+spc+parClose+spc
	regex = re.compile(intruction)
	matchObj= regex.match(world) 
	if matchObj :
		return (matchObj)
	else:	
	#	error(numL, world)
		print ('no match')
		
# def error (num, world):
# 	print ("There is a mistake in line : {}".format(num+1))
# 	spc = '(\s*)'
# 	action = '(move|turnLeft|turnRight|attack)'
# 	parOpen = '(\()'
# 	digit = '(\d*)'
# 	parClose = '(\))'
# 	"""encuentra el match de los errores mas comunes"""
# 	error1 = spc +action+spc+parOpen+spc+digit
# 	regex1 = re.compile(error1)
# 	matchObj1 = regex1.match(world)
# 	"""_________________________________"""
# 	error2 = spc +action+spc+digit+parClose
# 	regex2 = re.compile(error2)
# 	matchObj2 = regex1.match(world)
# 	"""__________________________________"""
# 	error3 = spc +action+spc+parOpen+spc+parClose
# 	regex3 = re.compile(error3)
# 	matchObj3 = regex1.match(world)
# 	"""_________________________________"""
# 	error4 = spc+action+spc

# 	if matchObj1 :
# 		print ("Mising close parenthesis at the end of the expresion: "+world)
# 	elif matchObj2 :
# 		print("Mising open parenthesis in the expresion : "+world)
# 	elif matchObj3:
# 		print("There is no number in the expresion: "+world)
# 	else:
# 		print ("Unrecognizable expression: "+world)
		
			
		
archivo = open("codigoTurtle.txt", "r")
salida = open ("instruccionescompliadas.py", "w")
#salida.write ("import turtle \n")
salida.write ("import turtle \n")
salida.write("ana = turtle.Turtle()\n")
salida.write("step = 25\n")
salida.write("angle = 90\n")
line = archivo.readlines()
j=0

for i in line:
	word = line [j]
	match = regularE(word, j)

	j=j+1
	if("move" ==match.group(2)):
		for n in range (int(match.group(6))):
			salida.write("ana.forward(step)\n")
	elif("turnRigth" ==match.group(2)):
		for n in range (int(match.group(6))):
			salida.write("ana.right(angle)\n")
	elif ("turnLeft" ==match.group(2)):
		for n in range (int(match.group(6))):
			salida.write("ana.left(angle)\n")
	elif("attack" ==match.group(2)):
		for n in range (int(match.group(6))):
			salida.write("ana.dot()\n")
salida.write("turtle.mainloop()\n")
	
