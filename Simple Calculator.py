def add(x,y):
    return x + y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print ("Enter any operator:")
print ("Add")
print ("sub")
print ("mul")
print ("div")
cho_opr = input ("choice any operator 1,2,3,4")

firstvalue = float(input ("Enter the first value"))
secondvalue = float(input ("enter the second value"))

if cho_opr == "1":
    print (firstvalue, "+", secondvalue, "=", add(firstvalue,secondvalue))
elif cho_opr == "2":
    print (firstvalue,"-", secondvalue, "=", sub(firstvalue,secondvalue))
elif cho_opr == "3":
    print (firstvalue, "*", secondvalue, "=", mul(firstvalue,secondvalue))
elif cho_opr == "4":
    print (firstvalue, "/", secondvalue, "=",div(firstvalue,secondvalue ))
else:
    print ("invalid syntax")
