# When you need to give more number of arguments to the function
# " *  "used this symbol tho the argument that means it will take multiple value
# it will be a tuple and to print that args you have to used the for loop

def printinfo(args1, *vartuple):
    print("Output is: ")
    print(args1)
    for var in vartuple:
        print(var)

printinfo(10,20)
printinfo(10,20,30,40)

def test_var_args(f_args, *argvs):
    print("First normal args:", f_args)
    for var in argvs:
        print("another arg through *argvs: ",var)

test_var_args('yahoo','Google','Python','PHP','Angular.js')
