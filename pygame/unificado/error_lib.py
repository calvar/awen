import re
#crea la lista que contiene en orden de llegada las intruccion

#clasifica e imprime el tipo de error
def error(line, l):
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
	if(not(first == "move" or first == "turnLeft" or first== "turnRigth" or first == "attack")):
		print("check the instrucion"+ line+"in line {}".format(l))		
	elif(num == False): 
		print("There is a number problem in the espresion "+ line+"in line {}".format(l))
	
	elif (len(splPar) > 3) :
		print("there is unbalanced parenthesis in the expresion  "+line+"in line {}".format(l) )
		
	elif (len(splPar) < 3  ):
		
		print("there is not a par of parethesis in the expresion "+line+"in line {}".format(l))
	else :
		print ("Unrecognazed expression "+line+"in line {}".format(l))



#Si hay match retorna el searchObj
#Sino llama a la funcion error

def search(line, l):
	spc = '(\s*)'
	action = '(move|turnLeft|turnRight|attack)'
	parOpen = '(\()'
	digit = '(\d+)'
	parClose = '(\))'
	intruction = spc+action+spc+parOpen+spc+digit+spc+parClose
	regex = re.compile(intruction)
	searchObj= re.search(regex, line)
	if (searchObj and len(line)-1==searchObj.end() ):
		return searchObj
		
	else :
		return False
	
#lee el archivo hasta que encuentra un error
def read(file):
	archivo = open(file, "r")
	line = archivo.readlines()
	l=0
	list_intr=[]
	for i in line:
		match = search(line[l], l)
		if(match != False):
			list_intr.append(match.group(2))
			list_intr.append(match.group(6))
			l+=1
		else:
			error(line[l], l+1)
			return False;

	return list_intr



