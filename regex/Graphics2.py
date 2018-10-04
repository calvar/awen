from tkinter import *
from io import open

"""
    Creado por: Isabela Caceres Palma, Carlos Eduardo Alvarez Cabrera y Esteban Hernandez.

    Descripcion:
    El siguiente programa fue diseñado e implementado con el objetivo de permitirle al usuario
    verificar la consecuencia a causa de sus decisiones en el lenguaje de programacion AWEN y
    reemplazar las largas e innevitablemente inadecuadas listas de error y posicion.
    Por ahora dicha verificacion se limita solo a mostrar graficamente de una manera muy sencilla
    y pretensiosamente concisa; las tres instrucciones basicas que componen el lenguaje AWEN.
    Y por el momento se excluyen otro tipo de declaraciones como: los ciclos, los condicionales o las operaciones aritmeticas.

    Desarrollo: Python|'Tkinter module'|

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def identificarIntencion(userInput):

    expresionRegularInstruccion = re.compile('\s*[A-Za-z]*\s*\(*(\d*)\)*\s*\w*')

    coincidencia = expresionRegularInstruccion.match(userInput)

    parteNumerica = coincidencia.group(1)

    contadorAttack = 0
    contadorMove = 0
    contadorTurnLeft = 0
    contadorTurnRight = 0

    if(parteNumerica == ""): parteNumerica = '1'

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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def empaquetarInstrucciones():

    archivoEntrada = open("C:/Users/User/Desktop/texto_1.txt", 'r')

    instrucciones = archivoEntrada.readlines()

    listaInstrucciones = []

    contadorCabezalesInterno = 0

    for i in range(0, (len(instrucciones))):

        if(instrucciones[i] == 'start:\n'):

            print('BEGINNING OF EXECUTION')

        elif(instrucciones[i] == 'end;'):

            print('END OF EXECUTION')

        else:

            intencion = identificarIntencion(instrucciones[i])

            listaInstrucciones.append(intencion)

        i += 1

    archivoEntrada.close()

    return listaInstrucciones 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def comprobarCabezales():

    archivoEntrada = open("C:/Users/User/Desktop/texto_1.txt", 'r')

    instrucciones = archivoEntrada.readlines()

    contador = 0

    if(instrucciones[0] == 'start:\n'):

        contador += 1    

    else: contador += 0
    
    if(instrucciones[len(instrucciones) - 1] == 'end;'):

        contador += 1  

    else: contador += 0

    return contador

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def reescribirInstrucciones(listaInstrucciones, contador):

    archivoSalida = open("C:/Users/User/Desktop/texto_2.txt", 'w')

    expresionRegularInstruccion = re.compile('\s*[A-Za-z]*\s*\(*(\d*)\)*\s*\w*')

    if(contador == 2): archivoSalida.write('start:\n')
    else: archivoSalida.write("START\n")

    for i in range(0,len(listaInstrucciones)):

        coincidencia = expresionRegularInstruccion.match(listaInstrucciones[i])

        parteNumerica = coincidencia.group(1)

        for e in range(0, int(parteNumerica)):

            if((listaInstrucciones[i])[0] == 'm'):

                archivoSalida.write('move')
                archivoSalida.write('\n')

            elif((listaInstrucciones[i])[0] == 't' and (listaInstrucciones[i])[4] == 'L'):

                archivoSalida.write('turnLeft')
                archivoSalida.write('\n')
                
            elif((listaInstrucciones[i])[0] == 't' and (listaInstrucciones[i])[4] == 'R'):

                archivoSalida.write('turnRight')
                archivoSalida.write('\n')

    if(contador == 2): archivoSalida.write('end;')
    else: archivoSalida.write("END")
    
    archivoSalida.close()


listaInstrucciones = empaquetarInstrucciones()
contador = comprobarCabezales()
print(contador)
reescribirInstrucciones(listaInstrucciones, contador)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def main():

    archivoTexto = open("C:/Users/User/Desktop/texto_2.txt",'r')

    instrucciones = archivoTexto.readlines()

    archivoTexto.close()

    ventana = Tk()
    ventana.geometry('500x700')
        
    lienzo = Canvas(ventana, width = '250', height = '550', bg = "#000")  
    lienzo.place(x = 500/5, y = 500/5)
    
    puntoX = 120
    puntoY = 0

    if(instrucciones[0] == 'START\n' or instrucciones[len(instrucciones) - 1] == 'END'):

        print("MISSING: BEGINNING OR END OF EXECUTION")

        lienzo.create_oval(puntoX - 10, puntoY, puntoX - 10 + 20, puntoY + 20, fill = "yellow")

    else:  

        for i in range(1, len(instrucciones) - 1):

            if(instrucciones[i] == 'move' or instrucciones[i] == 'move\n'):

                lienzo.create_line(puntoX, puntoY, puntoX, (puntoY + 15), fill = "#fff", width = 3.0)

                puntoY += 15
            
            elif(instrucciones[i] == 'turnLeft' or instrucciones[i] == 'turnLeft\n'):

                if((i < (len(instrucciones) - 1)) and (instrucciones[i + 1] == 'move' or instrucciones[i + 1] == 'move\n')):
                
                    lienzo.create_rectangle((puntoX - 20), puntoY, ((puntoX)+ 20), (puntoY + 15), fill = "#fff")

                    puntoX -= 15
            
                    lienzo.create_line(puntoX, (puntoY + 5), puntoX, (puntoY + 25), fill = "#fff", width = 3.0)

                    lienzo.create_rectangle((puntoX + 10), (puntoY + 6), (puntoX + 30), (puntoY + 5 + 4), fill = '#f00', width = 0)
                    lienzo.create_polygon((puntoX), (puntoY + 7), ((puntoX + 10)), ((puntoY - 5 + 7)), ((puntoX + 10)), ((puntoY  + 5 + 7)), fill = 'red')

                    puntoY += 15

                else:

                    lienzo.create_rectangle((puntoX - 20), puntoY, ((puntoX)+ 20), (puntoY + 15), fill = "#fff")

                    lienzo.create_rectangle((puntoX - 15 + 10), (puntoY + 6), (puntoX - 15 + 30), (puntoY + 5 + 4), fill = '#f00', width = 0)
                    lienzo.create_polygon((puntoX - 15), (puntoY + 7), ((puntoX -15 + 10)), ((puntoY - 5 + 7)), ((puntoX - 15 + 10)), ((puntoY  + 5 + 7)), fill = 'red')

                    puntoY += 15
            
            elif(instrucciones[i] == 'turnRight' or instrucciones[i] == 'turnRight\n'):

                if((i < (len(instrucciones) - 1)) and (instrucciones[i + 1] == 'move' or instrucciones[i + 1] == 'move\n')):

                    lienzo.create_rectangle((puntoX - 20), puntoY, (puntoX + 20), (puntoY + 15), fill = '#fff')

                    puntoX += 15

                    lienzo.create_line(puntoX, (puntoY + 5), puntoX, (puntoY + 25), fill = "#fff", width = 3.0)

                    lienzo.create_rectangle((puntoX - 10), (puntoY + 6), (puntoX - 30), (puntoY + 5 + 4), fill = '#f00', width = 0)
                    lienzo.create_polygon(puntoX, (puntoY + 7), (puntoX - 10), (puntoY + 5 + 7), (puntoX - 10), (puntoY - 5 + 7), fill = 'red')
                    
                    puntoY += 15

                else:

                    lienzo.create_rectangle((puntoX - 20), puntoY, (puntoX + 20), (puntoY + 15), fill = '#fff')

                    lienzo.create_rectangle((puntoX + 15 - 10), (puntoY + 6), (puntoX + 15 - 30), (puntoY + 5 + 4), fill = '#f00', width = 0)
                    lienzo.create_polygon(puntoX + 15, (puntoY + 7), (puntoX + 15 - 10), (puntoY + 5 + 7), (puntoX + 15 - 10), (puntoY - 5 + 7), fill = 'red')
                    
                    puntoY += 15

            else:

                lienzo.create_oval(puntoX - 10, puntoY, puntoX - 10 + 20, puntoY + 20, fill = "yellow")
                break;

            i += 1

    ventana.mainloop()

main()
