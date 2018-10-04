import re


def regCheck(line):
    #space = re.compile(" +")
    sp = "(\s*)"#"([\space]*)"
    Exp = "(move|turnLeft|turnRight|attack)"
    Oarg = "(\()"
    Carg = "(\))"
    Num = "(\d+)"

    statement = sp + Exp + sp + Oarg + sp + Num + sp + Carg  
    regex = re.compile(statement)
    matchObj = re.match(regex, line)

    return matchObj

def translate(word, num):
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
        tr += translate(mo.group(2),int(mo.group(6)))
        #print(tr)
    else:
        print("Syntax error at line {0}".format(cont))
        outFile.close()
        test = False
        break

if test:
    pycode = outputCode(tr)
    outFile.write(pycode)
    #print(pycode)
    outFile.close()

# if mo:
#     #print("mo.group(): {}".format(mo.group()))
#     #print("mo.group(1): {}".format(mo.group(1)))
#     print("mo.group(2): {}".format(mo.group(2)))
#     #print("mo.group(3): {}".format(mo.group(3)))
#     #print("mo.group(4): {}".format(mo.group(4)))
#     #print("mo.group(5): {}".format(mo.group(5)))
#     print("mo.group(6): {}".format(mo.group(6)))
#     #print("mo.group(7): {}".format(mo.group(7)))
#     #print("mo.group(8): {}".format(mo.group(8)))
# else:
#     print("No match!")
