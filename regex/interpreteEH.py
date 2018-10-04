import re

def getUserInput():

    return input("Ingrese una expresion: ")

def comprobarCoincidencia(userInput):
    
    expresionInstruccionAttack = '\s*?attack\s*?\(\s*?\d*\s*?\)\s*?'
    expresionInstruccionMove = '\s*?move\s*?\(\s*?\d*\s*?\)\s*?'
    expresionInstruccionTurnLeft = '\s*?turnLeft\s*?\(\s*?\d*\s*?\)\s*?'
    expresionInstruccionTurnRight = '\s*?turnRight\s*?\(\s*?\d*\s*?\)\s*?'

    expresionRegularInstruccionAttack = re.compile(expresionInstruccionAttack)
    expresionRegularInstruccionMove = re.compile(expresionInstruccionMove)
    expresionRegularInstruccionTurnLeft = re.compile(expresionInstruccionTurnLeft)
    expresionRegularInstruccionTurnRight = re.compile(expresionInstruccionTurnRight)

    coincidenciaAttack = expresionRegularInstruccionAttack.match(userInput)
    coincidenciaMove = expresionRegularInstruccionMove.match(userInput)
    coincidenciaTurnLeft = expresionRegularInstruccionTurnLeft.match(userInput)
    coincidenciaTurnRight = expresionRegularInstruccionTurnRight.match(userInput)
    
    if(coincidenciaAttack): return True
    elif(coincidenciaMove): return True
    elif(coincidenciaTurnLeft): return True
    elif(coincidenciaTurnRight): return True
    else: return False

#Si false comprobar coincidencia entra aqui
def identificarIntencion(userInput):

    #Defecto por exceso

    expresionAttack = '\s*?\w*?a\w*?t\w*?t\w*?a\w*?c\w*?k\w*?\s*?\(+\s*?\w*?\d*?\w*?\s*\)+\s*?\w*?'
    expresionMove = '\s*?\w*?m\w*?o\w*?v\w*?e\w*?\s*?\(+?\s*?\w*?\d+\w*?\s*\)+\s*?\w*?'
    expresionTurnLeft = '\s*?\w*?t\w*?u\w*?r\w*?n\w*?L\w*?e\w*?f\w*?t\w*?\s*?\(+\s*?\w*?\d*?\w*?\s*\)+\s*?\w*?'
    expresionTurnRight = '\s*?\w*?t\w*?u\w*?r\w*?n\w*?R\w*?i\w*?g\w*?h\w*?t\w*?\s*?\(+\s*?\w*?\d*?\w*?\s*\)+\s*?\w*?'

    expresionRegularAttack = re.compile(expresionAttack)
    expresionRegularMove = re.compile(expresionMove)
    expresionRegularTurnLeft = re.compile(expresionTurnLeft)
    expresionRegularTurnRight = re.compile(expresionTurnRight)

    if(expresionRegularAttack.search(userInput)): return 1
    elif(expresionRegularMove.search(userInput)): return 2
    elif(expresionRegularTurnLeft.search(userInput)): return 3
    elif(expresionRegularTurnRight.search(userInput)): return 4
    else:
        
        #Defecto por defecto

        cuentaCoincidenciasAttack = 0;
        cuentaCoincidenciasMove = 0;
        cuentaCoincidenciasTurnLeft = 0;
        cuentaCoincidenciasTurnRight = 0;

        for a in range(0, len(userInput)):

            if(userInput[a] == 't'):

                cuentaCoincidenciasAttack += 1
                cuentaCoincidenciasTurnLeft += 1
                cuentaCoincidenciasTurnRight += 1

            elif(userInput[a] == 'a' or userInput[a] == 'c' or userInput[a] == 'k'):

                cuentaCoincidenciasAttack += 1

            elif(userInput[a] == 'm' or userInput[a] == 'v' or userInput[a] == 'o'):

                cuentaCoincidenciasMove += 1

            elif(userInput[a] == 'e'):
                
                cuentaCoincidenciasMove += 1
                cuentaCoincidenciasTurnLeft += 1

            elif(userInput[a] == 'u' or userInput[a] == 'r' or userInput[a] == 'n'):    

                cuentaCoincidenciasTurnLeft += 1
                cuentaCoincidenciasTurnRight += 1

            elif(userInput[a] == 'R' or userInput[a] == 'h' or userInput[a] == 'g' or userInput[a] == 'i'):

                cuentaCoincidenciasTurnRight += 1

            elif(userInput[a] == 'L' or userInput == 'l' or userInput == 'f'):

                cuentaCoincidenciasTurnLeft += 1

            elif(userInput[a] == '(' or userInput[a] == ')'):

                cuentaCoincidenciasAttack += 1
                cuentaCoincidenciasMove += 1
                cuentaCoincidenciasTurnLeft += 1
                cuentaCoincidenciasTurnRight += 1

        if((cuentaCoincidenciasAttack > cuentaCoincidenciasMove) and (cuentaCoincidenciasAttack > cuentaCoincidenciasTurnLeft) and (cuentaCoincidenciasAttack > cuentaCoincidenciasTurnRight)):

            return -1

        elif((cuentaCoincidenciasMove > cuentaCoincidenciasAttack) and (cuentaCoincidenciasMove > cuentaCoincidenciasTurnLeft) and (cuentaCoincidenciasMove > cuentaCoincidenciasTurnRight)):
                
            return -2

        elif((cuentaCoincidenciasTurnLeft > cuentaCoincidenciasMove) and (cuentaCoincidenciasTurnLeft > cuentaCoincidenciasAttack) and (cuentaCoincidenciasTurnLeft > cuentaCoincidenciasTurnRight)):

            return -3

        elif((cuentaCoincidenciasTurnRight > cuentaCoincidenciasMove) and (cuentaCoincidenciasTurnRight > cuentaCoincidenciasTurnLeft) and (cuentaCoincidenciasTurnRight > cuentaCoincidenciasAttack)):   

            return -4

        else: return 0

def UbicarErrores(userInput, numeroIdentificador):

    if(numeroIdentificador > 0):

        attackComparison = "attack(4)"

        moveComparison = "move(4)"
        turnLeftComparison = "turnLeft(1)"
        turnRightComparison = "turnRight(4)"
                
        listaErrores = []

        listaPosicionErrores = []

        if(numeroIdentificador == 1):

            print("Quizas quisiste decir: attack")

            indiceLetraUserInput = 0
            indiceLetraAttackComparison = 0

            while(indiceLetraUserInput < len(userInput)):

                letraUserInput = userInput[indiceLetraUserInput]
                letraAttackComparison = attackComparison[indiceLetraAttackComparison]

                if(indiceLetraAttackComparison <= 6):
                            
                    if(letraUserInput == letraAttackComparison):

                        indiceLetraUserInput += 1
                        indiceLetraAttackComparison += 1

                    else:

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                else:

                    if((indiceLetraUserInput != len(userInput) - 1) and (letraUserInput != '0' and letraUserInput != '1' and letraUserInput != '2' and letraUserInput != '3' and letraUserInput != '4' and letraUserInput != '5' and letraUserInput != '6' and letraUserInput != '7' and letraUserInput != '8' and letraUserInput != '9')):                            

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                    elif(letraUserInput == ')' and (indiceLetraUserInput == len(userInput) - 1)):

                        break;

                    else:
                                
                        indiceLetraUserInput += 1
                                      
            indice = 0;

            for e in listaErrores:

                print("Error: " + listaErrores[indice] + " en " + listaPosicionErrores[indice])            

                indice += 1;
                                                    
        elif(numeroIdentificador == 2):

            print("Quizas quisiste decir: move")
                    
            indiceLetraUserInput = 0
            indiceLetraMoveComparison = 0

            while(indiceLetraUserInput < len(userInput)):

                letraUserInput = userInput[indiceLetraUserInput]
                letraMoveComparison = moveComparison[indiceLetraMoveComparison]

                if(indiceLetraMoveComparison <= 4):
                            
                    if(letraUserInput == letraMoveComparison):

                        indiceLetraUserInput += 1
                        indiceLetraMoveComparison += 1

                    else:

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                else:

                    if((indiceLetraUserInput != len(userInput) - 1) and (letraUserInput != '0' and letraUserInput != '1' and letraUserInput != '2' and letraUserInput != '3' and letraUserInput != '4' and letraUserInput != '5' and letraUserInput != '6' and letraUserInput != '7' and letraUserInput != '8' and letraUserInput != '9')):                            

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                    elif(letraUserInput == ')' and (indiceLetraUserInput == len(userInput) - 1)):

                        break;

                    else:
                                
                        indiceLetraUserInput += 1
                                
                              
            indice = 0;

            for e in listaErrores:

                print("Error: " + listaErrores[indice] + " en " + listaPosicionErrores[indice])            

                indice += 1;

        elif(enumeroIdentificador == 3):

            print("Quizas quisiste decir: turnLeft")

            indiceLetraUserInput = 0
            indiceLetraTurnLeftComparison = 0

            while(indiceLetraUserInput < len(userInput)):

                letraUserInput = userInput[indiceLetraUserInput]
                letraTurnLeftComparison = turnLeftComparison[indiceLetraTurnLeftComparison]

                if(indiceLetraTurnLeftComparison <= 8):
                            
                    if(letraUserInput == letraTurnLeftComparison):

                        indiceLetraUserInput += 1
                        indiceLetraTurnLeftComparison += 1

                    else:

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                else:

                    if((indiceLetraUserInput != len(userInput) - 1) and (letraUserInput != '0' and letraUserInput != '1' and letraUserInput != '2' and letraUserInput != '3' and letraUserInput != '4' and letraUserInput != '5' and letraUserInput != '6' and letraUserInput != '7' and letraUserInput != '8' and letraUserInput != '9')):                            

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                    elif(letraUserInput == ')' and (indiceLetraUserInput == len(userInput) - 1)):

                        break;

                    else:
                                
                        indiceLetraUserInput += 1
                                
                              
            indice = 0;

            for e in listaErrores:

                print("Error: " + listaErrores[indice] + " en " + listaPosicionErrores[indice])            

                indice += 1;

        elif(numeroIdentificador == 4):
        
            print("Quizas quisiste decir: turnRight")            

            indiceLetraUserInput = 0
            indiceLetraTurnRightComparison = 0

            while(indiceLetraUserInput < len(userInput)):

                letraUserInput = userInput[indiceLetraUserInput]
                letraTurnRightComparison = turnRightComparison[indiceLetraTurnRightComparison]

                if(indiceLetraTurnRightComparison <= 9):
                            
                    if(letraUserInput == letraTurnRightComparison):

                        indiceLetraUserInput += 1
                        indiceLetraTurnRightComparison += 1

                    else:

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                else:

                    if((indiceLetraUserInput != len(userInput) - 1) and (letraUserInput != '0' and letraUserInput != '1' and letraUserInput != '2' and letraUserInput != '3' and letraUserInput != '4' and letraUserInput != '5' and letraUserInput != '6' and letraUserInput != '7' and letraUserInput != '8' and letraUserInput != '9')):                            

                        listaErrores.append(letraUserInput)
                        listaPosicionErrores.append(str(indiceLetraUserInput))

                        indiceLetraUserInput += 1

                    elif(letraUserInput == ')' and (indiceLetraUserInput == len(userInput) - 1)):

                        break;

                    else:
                                
                        indiceLetraUserInput += 1
                                
                              
            indice = 0;

            for e in listaErrores:

                print("Error: " + listaErrores[indice] + " en " + listaPosicionErrores[indice])            

                indice += 1;

    else:

        expresionReferencia = '\s*([A-Za-z]*)\({0,1}(\d*)\){0,1}\s*'

        expresionRegularReferencia = re.compile(expresionReferencia)

        coincidencia = expresionRegularReferencia.match(userInput)

        grupoNumerico = coincidencia.group(2)
        
        listaFaltas = []
        listaPosicionFaltas = []

        if(numeroIdentificador == -1):

            palabraReferencia = 'attack()'

            indiceUserInput = 0
            indicePalabraReferencia = 0

            while(indicePalabraReferencia != (len(palabraReferencia)- 1)):

                if(indiceUserInput == ((len(userInput) - len(grupoNumerico)) - 1)):

                    if(userInput[indiceUserInput + 1] == palabraReferencia[indicePalabraReferencia]):

                        indiceUserInput += len(grupoNumerico) + 1
                        indicePalabraReferencia += 1
                        
                    else:

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1

                else:

                    if(userInput[indiceUserInput + 1] != palabraReferencia[indicePalabraReferencia]):

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1
                        
                    else:

                        indiceUserInput += 1
                        indicePalabraReferencia += 1


        elif(numeroIdentificador == -2):

            palabraReferencia = 'move()'

            indiceUserInput = 0
            indicePalabraReferencia = 0

            while(indicePalabraReferencia != (len(palabraReferencia)- 1)):

                if(indiceUserInput == ((len(userInput) - len(grupoNumerico)) - 1)):

                    if(userInput[indiceUserInput + 1] == palabraReferencia[indicePalabraReferencia]):

                        indiceUserInput += len(grupoNumerico) + 1
                        indicePalabraReferencia += 1
                        
                    else:

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1

                else:

                    if(userInput[indiceUserInput + 1] != palabraReferencia[indicePalabraReferencia]):

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1
                        
                    else:

                        indiceUserInput += 1
                        indicePalabraReferencia += 1


        elif(numeroIdentificador == -3):

            palabraReferencia = 'turnLeft()'

            indiceUserInput = 0
            indicePalabraReferencia = 0

            while(indicePalabraReferencia != (len(palabraReferencia)- 1)):

                if(indiceUserInput == ((len(userInput) - len(grupoNumerico)) - 1)):

                    if(userInput[indiceUserInput + 1] == palabraReferencia[indicePalabraReferencia]):

                        indiceUserInput += len(grupoNumerico) + 1
                        indicePalabraReferencia += 1
                        
                    else:

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1

                else:

                    if(userInput[indiceUserInput + 1] != palabraReferencia[indicePalabraReferencia]):

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1
                        
                    else:

                        indiceUserInput += 1
                        indicePalabraReferencia += 1


        elif(numeroIdentificador == -4):    

            palabraReferencia = 'turnRight()'

            indiceUserInput = 0
            indicePalabraReferencia = 0

            while(indicePalabraReferencia != (len(palabraReferencia)- 1)):

                if(indiceUserInput == ((len(userInput) - len(grupoNumerico)) - 1)):

                    if(userInput[indiceUserInput + 1] == palabraReferencia[indicePalabraReferencia]):

                        indiceUserInput += len(grupoNumerico) + 1
                        indicePalabraReferencia += 1
                        
                    else:

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1

                else:

                    if(userInput[indiceUserInput + 1] != palabraReferencia[indicePalabraReferencia]):

                        listaFaltas.append(palabraReferencia[indicePalabraReferencia])
                        listaPosicionFaltas.append(indiceUserInput)

                        indicePalabraReferencia += 1
                        
                    else:

                        indiceUserInput += 1
                        indicePalabraReferencia += 1


        listaFaltas.pop(0)

        indice = 0

        for i in range(0, len(listaFaltas)):

            print("Falta la letra: " + listaFaltas[indice])

            indice += 1

userInput = getUserInput()
coincidencia = comprobarCoincidencia(userInput)

if(not(coincidencia)):

    numeroIdentificador = identificarIntencion(userInput)
    print(numeroIdentificador)

    UbicarErrores(userInput,numeroIdentificador)

else: print("expresion correcta")    
