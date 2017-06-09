def printm(name="Suru",age=18):
    print("Name: ",name)
    print("Age: ",age)
    return

printm("Sur",17)
printm("m",25)
printm(age=52,name="mn")

s = lambda args1,args2:args1+args2
print("VAlues: ",s(10,20))

def many(n,*p):
    print("output: ")
    print(n)
    for v in p:
        print(v)
    return

many(10,20,30)
