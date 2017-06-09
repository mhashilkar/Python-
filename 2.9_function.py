# function

# Create a function
def sayHello(name = 'muru'):
    print('hello', name)


sayHello('suru')

#RETURN A VALUE
def getSum(num1,num2):
    total = num1 + num2
    return total

numSum = getSum(1,2)
print(numSum)

# immusable function
def addOneToNum(num):
    num = num + 1
    print('value inside function: ',num)
    return

num = 5
addOneToNum(num)
print('Value outside function :', num)

# immusable function with list
def addOneToList(myList):
    mylist.append(4)
    print('value inside the list: ',mylist)
    return

mylist = [1,2,3]
addOneToList(mylist)
print('value outside the list: ',mylist)
