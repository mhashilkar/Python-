"""
Use the lambda keyword to create small anonymous function
These function are called anonymous because they are not declared in "def"
"""
sum = lambda args1,args2,args3:args1 + args2 * args3

# Now you can call sum as a function
print("Value of total: ",sum(10,20,30))
print("Value of total: ",sum(10,20,40))
