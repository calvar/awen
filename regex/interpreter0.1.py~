import re


def regCheck(line):
    """Esta funcion recibe una linea y retorna su expresion regular"""
    sp = "(\s*)"
    Exp = "(move|turnLeft|turnRight|attack)"
    Oarg = "(\()"
    Carg = "(\))"
    Num = "(\d+)"
    
    statement = sp + Exp + sp + Oarg + sp + Num + sp + Carg  
    regex = re.compile(statement)
    searchObj = re.search(regex, line)
    return searchObj

def translate(word, num):
    """Esta funcion recibe un comando y el numero de veces que
    se repite, y retorna la instruccion equivalente en tortuga"""
    command = ""
    step = 50
    if word == "move":
        command = "t.forward({0})".format(step)
    elif word == "turnRight":
        command = "t.right(90)"
    elif word == "turnLeft":
        command = "t.left(90)"
    elif word == "attack":
        command = "t.dot()"
    
    output = "for i in range({0}):\n".format(num)
    output += "\t{0}\n".format(command)
    return output
    
def outputCode(command):
    """Esta funcion retorna todo el codigo tortuga"""
    code = "import turtle\n\n"
    code += "wn = turtle.Screen()\n"
    code += "t = turtle.Turtle()\n"
    code += "t.shape(\"turtle\")\n\n"
    code += command+"\n"
    code += "turtle.mainloop()\n"
    return code

#EXECUTION-----------------------------------------

inFile = open("codeAwen.awn","r")
lines = inFile.readlines()#[]
#for l in inFile:
#    lines.append(l)
#inFile.close()

#line = lines[0]#input("")


outFile = open("codeTortu.py","w")

cont = 0
test = True
tr = ""
for line in lines:
    cont += 1
    mo = regCheck(line)
    #print(mo)
    if mo:
        minl = mo.span()[0]
        maxl = mo.span()[1]
        if minl > 0 and line[:minl] != (minl-1)*" ":
            print("Syntax error at line {0}: \"{1}\" is not recognized.".format(cont,line[:minl]))
            outFile.close()
            test = False
            #break
        elif len(line.rstrip()) > maxl:
            print("Syntax error at line {0}: \"{1}\" is not recognized.".format(cont,line[maxl+1:]))
            outFile.close()
            test = False
            #break
        else:
            tr += translate(mo.group(2),int(mo.group(6)))
            #print(tr)
    else:
        print("Syntax error at line {0}: Format is incomprehensible.".format(cont))
        outFile.close()
        test = False
        #break

if test:
    pycode = outputCode(tr)
    outFile.write(pycode)
    #print(pycode)
    outFile.close()
