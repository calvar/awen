import re

def write(searchObj):
	"""Escribe las instrucciones en lenguage tortuga"""
	##archivo = open("codigoTurtle.txt", "r")
        salida = open ("instruccionescompliadas.py", "w")
        salida.write ("import turtle \n")
        #salida.write ("import Tkinter \n")
        salida.write("ana = turtle()\n")
        salida.write("step = 25\n")
        salida.write("angle = 90\n")
        salida.close()
        if("move" ==searchObj.group(2)):
                for n in range (int(searchObj.group(6))):
                        salida.write("ana.forward\(step\)\n")
	elif("turnRigth" == searchObj.group(2)):
                for n in range (int(searchObj.group(6))):
                        salida.write("ana.right\(angle\)\n")
	elif ("turnLeft" == searchObj.group(2)):
                for n in range (int(searchObj.group(6))):
                        salida.write("ana.left\(angle\)\n")
	elif("attack" == searchObj.group(2)):
                for n in range (int(searchObj.group(6))):
                        salida.write("ana.dot\(\)")
                        
	salida.close()

def error(line, l):
        """Informa si hay un error de sintaxis, el tipo de error y la linea."""
        splPar = re.split('(\()|(\))', line)
        contador = 0
        num = False
        first = splPar[0]
        splPar.pop(0)
        
        
	for i in range(len(splPar)):
		if(splPar[i] ==None):
			contador = contador+1	
	                
	for i in range((contador)):
		splPar.remove(None)	
	
	for i in range(len(splPar)):
		if(splPar[i].isdigit()):
			num = True
	if(not (first == "move" or first == "turnLeft" or first == "turnRigth" or first == "attack")):
		print("check the instrucion "+ line.strip()+" in line {}".format(l))		
	elif(num == False): 
		print("There is a number problem in the espresion "+ line+"in line {}".format(l))
	
	elif (len(splPar) > 3) :
		print("there is unbalanced parenthesis in the expresion  "+line+"in line {}".format(l) )
		
	elif (len(splPar) < 3  ):
		
		print("there is not a par of parethesis in the expresion "+line+"in line {}".format(l))
	else :
		print ("Unrecognazed expression "+line+"in line {}".format(l))

	
def search(line, l):
        """Busca un match con la expresion regular"""
	spc = '(\s*)'
	action = '(move|turnLeft|turnRight|attack)'
	parOpen = '(\()'
	digit = '(\d+)'
	parClose = '(\))'
	intruction = spc+action+spc+parOpen+spc+digit+spc+parClose
	regex = re.compile(intruction)
	searchObj= re.search(regex, line)
	if (searchObj and len(line)-1==searchObj.end() ):
		#print ("there is a match")	
		write(searchObj	)
		return True
		
	else :
		error(line, l)
		return False
	

def read(file):
        """Lee el archivo linea por linea y llama la funcion search"""
        archivo = open(file, "r")
        line = archivo.readlines()
        l=0
        for i in line:
		if(search(line[l], l+1)==True):
			l+=1
		else:
			break;
        archivo.close()


read("t.txt")
