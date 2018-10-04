import re 

line = " turnRight(32 ) "

#regex = r"([a-zA-Z]+) (\d+)"
space = re.compile(" +")
sp = "([\space]*)"
Exp = "(move|turnLeft|turnRight|attack)"
Oarg = "(\()"
Carg = "(\))"
Num = "(\d+)"

statement = sp + Exp + sp + Oarg + sp + Num + sp + Carg  
regex = re.compile(statement)
#regex = r"([\space]*)(move|turnLeft|turnRight|attack)([\space]*)(\()([\space]*)(\d+)([\space]*)(\))" 

"""Look for a match of the regular expression at the beginning of the line provided"""
matchObj = re.match(regex, line)
print(matchObj)
if matchObj:
    print("matchObj.group(): {}".format(matchObj.group()))
    print("matchObj.group(1): {}".format(matchObj.group(1)))
    print("matchObj.group(2): {}".format(matchObj.group(2)))
    print("matchObj.group(3): {}".format(matchObj.group(3)))
    print("matchObj.group(4): {}".format(matchObj.group(4)))
    print("matchObj.group(5): {}".format(matchObj.group(5)))
    print("matchObj.group(6): {}".format(matchObj.group(6)))
    print("matchObj.group(7): {}".format(matchObj.group(7)))
    print("matchObj.group(8): {}".format(matchObj.group(8)))
else:
    print("No match!")

"""Look for the first occurrence of the regular expression in the line provided"""    
searchObj = re.search(regex, line)
print(searchObj)
if searchObj:
    print("searchObj.group(): {}".format(searchObj.group()))
    print("searchObj.group(1): {}".format(searchObj.group(1)))
    print("searchObj.group(2): {}".format(searchObj.group(2)))
    print("searchObj.group(3): {}".format(searchObj.group(3)))
    print("searchObj.group(4): {}".format(searchObj.group(4)))
    print("searchObj.group(5): {}".format(searchObj.group(5)))
    print("searchObj.group(6): {}".format(searchObj.group(6)))
    print("searchObj.group(7): {}".format(searchObj.group(7)))
    print("searchObj.group(8): {}".format(searchObj.group(8)))
else:
    print("Nothing found!")



