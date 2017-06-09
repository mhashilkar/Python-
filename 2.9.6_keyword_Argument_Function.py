"""
    Keyword arguments are related to the function calls
    This allows you to skip arguments or place them out of order.
"""
def printme(args):
    print("args")
    return;

printme(args = "My String")

# 2nd type of keyword function
def printinfo(name,age):
    print("Name: ",name)
    print("Age: ",age)
    return;
printinfo("Suru",18)
printinfo(age=18,name="Muru")
