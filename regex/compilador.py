import re

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def identificarIntencion(userInput):

    expresionRegularInstruccion = re.compile('\s*[A-Za-z]*\s*\(*(\d*)\)*\s*\w*')

    coincidencia = expresionRegularInstruccion.match(userInput)

    parteNumerica = coincidencia.group(1)

    contadorAttack = 0
    contadorMove = 0
    contadorTurnLeft = 0
    contadorTurnRight = 0

    for a in range(0,len(userInput)):

        if(userInput[a] == 'a' or userInput[a] == 'c' or userInput[a] == 'k'): contadorAttack += 1
        elif(userInput[a] == 'm' or userInput[a] == 'v' or userInput[a] == 'o'): contadorMove += 1
        elif(userInput[a] == 'L' or userInput[a] == 'f'): contadorTurnLeft += 1
        elif(userInput[a] == 'R' or userInput[a] == 'h'): contadorTurnRight += 1
        elif(userInput[a] == 't'):

            contadorAttack += 1
            contadorTurnLeft += 1
            contadorTurnRight += 1

        elif(userInput[a] == 'e'):

            contadorMove +=1
            contadorTurnLeft += 1

        elif(userInput[a] == '(' or userInput[a] == ')'):

            contadorAttack += 1
            contadorMove += 1
            contadorTurnLeft += 1
            contadorTurnRight += 1

        else:

            contadorAttack += 0
            contadorMove += 0
            contadorTurnLeft += 0
            contadorTurnRight += 0

        if(contadorAttack > contadorMove and contadorAttack > contadorTurnLeft and contadorAttack > contadorTurnRight): return "attack" + "(" + parteNumerica + ")"
        elif(contadorMove > contadorAttack and contadorMove > contadorTurnLeft and contadorMove > contadorTurnRight): return "move" + "(" + parteNumerica + ")"
        elif(contadorTurnLeft > contadorAttack and contadorTurnLeft > contadorMove and contadorTurnLeft > contadorTurnRight): return "turnLeft" + "(" + parteNumerica + ")"
        elif(contadorTurnRight > contadorAttack and contadorTurnRight > contadorMove and contadorTurnRight > contadorTurnLeft): return "turnRight" + "(" + parteNumerica + ")"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def generarLista(listaPotencial):

    lista = []

    indice = 0

    for i in range(0, len(listaPotencial)):

        lista.append(listaPotencial[indice])

        indice += 1

    return lista

def generarListaIndices(longitudListaPotencial):

	listaIndices = []

	indice = 0

	for a in range(0, longitudListaPotencial):

		listaIndices.append(indice)

		indice += 1

	return listaIndices

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def IdentificarListas(indiceListaUserInput, indiceListaIntencion):

	if(indiceListaIntencion >= (len(listaIntencion) - 1)):

		if(indiceListaUserInput >= len(listaUserInput)): print("Identificacion terminada") #Da por terminada la revision de la lista
		else:

			if(listaUserInput[indiceListaUserInput] == listaIntencion[indiceListaIntencion]):

				listaIndicesIntencion.pop(indiceListaIntencion)
				listaIndicesUserInput.pop(indiceListaUserInput)
				listaIntencion.pop(indiceListaIntencion)
				listaUserInput.pop(indiceListaUserInput)
				
			IdentificarListas((indiceListaUserInput + 1), indiceListaIntencion)

	else:

		if(indiceListaUserInput == len(listaUserInput)): IdentificarListas((0), indiceListaIntencion)
		else: 

			if(listaUserInput[indiceListaUserInput] == listaIntencion[indiceListaIntencion]):

				listaIndicesIntencion.pop(indiceListaIntencion)
				listaIndicesUserInput.pop(indiceListaUserInput)
				listaIntencion.pop(indiceListaIntencion)
				listaUserInput.pop(indiceListaUserInput)

				IdentificarListas((0), indiceListaIntencion)
			
			else: IdentificarListas((indiceListaUserInput + 1), (indiceListaIntencion + 1))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def pulirListas(indiceListaIntencion, indiceListaUserInput):

	if(indiceListaIntencion == (len(listaIntencion))): print("Revision terminada")
	else:

		if(indiceListaUserInput == (len(listaUserInput))): pulirListas((indiceListaIntencion + 1), 0)
		else:

			if(listaIntencion[indiceListaIntencion] == listaUserInput[indiceListaUserInput]):

				listaIndicesIntencion.pop(indiceListaIntencion)
				listaIndicesUserInput.pop(indiceListaUserInput)
				listaIntencion.pop(indiceListaIntencion)
				listaUserInput.pop(indiceListaUserInput)
	
				pulirListas(0,0)

			else: pulirListas(indiceListaIntencion, (indiceListaUserInput + 1))	

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

userInput = input("Ingrese una instruccion: ")
nivelAyuda = input("Ingrese un nivel de ayuda: ")

intencion = identificarIntencion(userInput)

listaIntencion = generarLista(intencion)
listaUserInput = generarLista(userInput)

listaIntencionUno = generarLista(intencion)
listaUserInputUno = generarLista(userInput)

listaIndicesIntencion = generarListaIndices(len(listaIntencion))
listaIndicesUserInput = generarListaIndices(len(listaUserInput))

indiceListaUserInputUno = 0
indiceListaIntencionUno = 0

indiceListaUserInputDos = 0
indiceListaIntencionDos = 0

IdentificarListas(indiceListaUserInputUno, indiceListaIntencionUno)

pulirListas(indiceListaIntencionDos, indiceListaUserInputDos)

if(nivelAyuda == "bajo"): print('quizas quisiste decir: ' + intencion)
elif(nivelAyuda == "medio"): 

	print("Sobra:")
	print(listaUserInput)
	print("Falta:")
	print(listaIntencion)

elif(nivelAyuda == 'alto'):

	print("Sobra:")
	print(listaUserInput)
	print(listaIndicesUserInput)
	print("Falta:")
	print(listaIntencion)
	print(listaIndicesIntencion)
