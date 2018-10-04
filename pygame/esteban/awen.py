import re

nombresDefinidos = []
variablesLocales = []
funciones = []

def checkInstrucciones(continuacionInstruccion):

    instruccionesFuncion = []

    recolector = ""

    for a in range(0, len(str(continuacionInstruccion))):

        if((continuacionInstruccion[a]) == ','):

            instruccionesFuncion.append(recolector)
            recolector = ""
        
        else: recolector += str(continuacionInstruccion[a])

    instruccionesFuncion.append(recolector)

    funciones.append(instruccionesFuncion)

def checkOpenClose(continuacionInstruccion):

    coincidencia = re.match("(\=)(.+)(\;)", continuacionInstruccion)

    if(coincidencia):

        checkInstrucciones(coincidencia.group(2))
        return True

    else: return False

def checkParentesis(continuacionInstruccion):

	coincidencia = re.match("\((\w+)\)(.+)", continuacionInstruccion)
	
	if(coincidencia):

		variableLocal = coincidencia.group(1)		
		variablesLocales.append(variableLocal)

		return checkOpenClose(coincidencia.group(2))		

	else: return False

def checkName(instruccion):

	coincidencia = re.match("(\w+)(.+)", instruccion)

	if(coincidencia): 

		nombre = coincidencia.group(1)
		nombresDefinidos.append(nombre)

		return checkParentesis(coincidencia.group(2))

	else: return False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

gruposInstrucciones = []

def checkFunciones(posicion):

    for a in range(posicion,len(funciones)):

        instrucciones = []

        for e in range(0,len(funciones[a])):

            iterador = 0;
            instruccion = 0;
    
            primeraCoincidencia = re.match(("(\w+)(\()(\w+)(\))"),(funciones[a])[e])

            if(primeraCoincidencia):

                iterador = (primeraCoincidencia.group(1))
                instruccion = (primeraCoincidencia.group(3))

            else:

                segundaCoincidencia = re.match(("(\()(\w+)(\))(\w+)"),(funciones[a])[e])

                if(segundaCoincidencia):

                    instruccion = (segundaCoincidencia.group(2))
                    iterador = (segundaCoincidencia.group(4))                    

                else:

                    terceraCoincidencia = re.match(("(\w+)"),(funciones[a])[e])

                    if(terceraCoincidencia):

                        iterador = '1' 
                        instruccion = (terceraCoincidencia.group(1))

                    else: print("ERROR")
            
            if(ord(iterador) >= 48 and ord(iterador) <= 57):

                for i in range(0,int(iterador)):

                    instrucciones.append(instruccion)
            
            else:

                if(iterador == variablesLocales[len(variablesLocales) - 1]):

                    instrucciones.append(iterador + "(" + instruccion + ")")       

                else: print("Error de variable")

        gruposInstrucciones.append(instrucciones)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
     
def comprobarDefinicion(instruccion, posicion):

    if(checkName(instruccion)):

        print("CORRECTA")
        print(variablesLocales)
        print(nombresDefinidos)
        print(funciones)
        checkFunciones(posicion)
        print("---------------------------------------------------------------")
        print(nombresDefinidos)
        print(gruposInstrucciones)
        
        comprobarDefinicion(input("Ingrese otra instruccion: "), posicion + 1)
        
    else:

        #nombresDefinidos.clear()
        #variablesLocales.clear()
        #funciones.clear()
        print(variablesLocales)
        print(nombresDefinidos)
        print(funciones)
        print("NO")

    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
comprobarDefinicion(input("Ingrese una instruccion: "), 0)
#checkFunciones()
#print("---------------------------------------------------------------")
#print(nombresDefinidos)
#print(gruposInstrucciones)
