from io import open
import re

archivoTexto = open("codeAwen.awn", "r")

userInputInstructions = archivoTexto.readlines();

for e in range(0, (len(userInputInstructions)), 1):

    print("Linea: " + str(e))

    userInput = userInputInstructions[e]

    archivoTexto.close()

    ExpresionInstruccion = '\s*(attack|move|turnLeft|turnRight)\d*(\({1})(\s*\d+\s*)(\){1})\s*'

    ExpresionRegularInstruccion = re.compile(ExpresionInstruccion)

    coincidenciaAcertada = ExpresionRegularInstruccion.match(userInput)

    if(coincidenciaAcertada):
    
        print("¡EXPRESION CORRECTA!")

        print("Parte literal: " + coincidenciaAcertada.group(1))
        print("Parentesis abierto: " + coincidenciaAcertada.group(2))
        print("Parte numerica: " + coincidenciaAcertada.group(3))
        print("Parentesis cerrado: " + coincidenciaAcertada.group(4))

    else:

        print("ERROR!")

        ExpresionIncomprensible = '\s*([A-Z|a-z]*)\s*(\(*)(\d*)(\)*)'

        ExpresionRegularIncomprensible = re.compile(ExpresionIncomprensible)

        coincidenciaErronea = ExpresionRegularIncomprensible.match(userInput)

        contadorGrupos = 0

        if(coincidenciaErronea):

            print("Grupo Literal: " + coincidenciaErronea.group(1))
            print("Parentesis Abierto: " + coincidenciaErronea.group(2))
            print("Grupo Numerico: " + coincidenciaErronea.group(3))
            print("Parentesis Cerrado: " + coincidenciaErronea.group(4))

            grupoLiteral = coincidenciaErronea.group(1)
            parentesisAbierto = coincidenciaErronea.group(2)
            grupoNumerico = coincidenciaErronea.group(3)
            parentesisCerrado = coincidenciaErronea.group(4)

            if(not(grupoLiteral)):

                print("Error de literalidad")
                                
            if(not(parentesisAbierto)):

                print("Error Estructural")
                
            if(not(grupoNumerico)):

                print("Error Numerico")
                
            if(not(parentesisCerrado)):

                print("Error Estructural")

            else:

                attackReferencia = '\w*?a\w*?t\w*?t\w*?a\w*?c\w*?k\w*?\(*\d*\)*'
                moveReferencia = '\w*?m\w*?o\w*?v\w*?e\w*?\(*\d*\)*'
                turnLeftReferencia = '\w*?t\w*?u\w*?r\w*?n\w*?L\w*?e\w*?f\w*?t\w*?\(*\d*\)*'
                turnRightReferencia = '\w*?t\w*?u\w*?r\w*?n\w*?R\w*?i\w*?g\w*?h\w*?t\w*?\(*\d*\)*'

                expresionRegularAttackReferencia = re.compile(attackReferencia)
                expresionRegularMoveReferencia = re.compile(moveReferencia)
                expresionRegularTurnLeftReferencia = re.compile(turnLeftReferencia)
                expresionRegularTurnRightReferencia = re.compile(turnRightReferencia)

                attackComparison = "attack(4)"
                moveComparison = "move(4)"
                turnLeftComparison = "turnLeft(1)"
                turnRightComparison = "turnRight(4)"
                
                listaErrores = []

                listaPosicionErrores = []

                if(expresionRegularAttackReferencia.search(userInput)):

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
                                                    
                elif(expresionRegularMoveReferencia.search(userInput)):

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

                elif(expresionRegularTurnLeftReferencia.search(userInput)):

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

                elif(expresionRegularTurnRightReferencia.search(userInput)):
        
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

                    print("La instruccion no tiene sentido")

        else: print("Texto Incomprensible")

    print('//------------------------------------------------------------------------------------------------------------------------------------------------------------------//')










