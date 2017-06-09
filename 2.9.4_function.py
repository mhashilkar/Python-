# Function defination is here
def printme(str):
    print(str)
    return

printme("This is first call to the user defined functions")

# In Python parameter pass bye refrense only
def changeme(mylist):
    # id() is default function in python which give unique id
    print(id(mylist))
    print("Value inside the function before change: ",mylist)
    mylist[2] = 50
    print("Values inside the function after change: ",mylist)
    return

mylist = [10,20,30]
print(id(mylist))
changeme(mylist)
print("Values outside the function: ", mylist)
