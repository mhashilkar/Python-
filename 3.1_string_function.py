#STRING FUNCTION
myStr = 'HelloWorld'

#capitalize
print(myStr.capitalize())

#Swap case
print(myStr.swapcase())

#Get length
print(len(myStr))

#Replace
print(myStr.replace('World' , 'Everyone'))

#String count
sub ='l'
print(myStr.count(sub))

# Startwith
print(myStr.startswith('Hello'))

#Endswith
print(myStr.endswith('World'))

# split to list
my = 'Hellow Everyone There'
print(myStr.split())
print(my.split())

# find
print(myStr.find('x'))

#index (if it not find then show error)
print(myStr.index('H'))

#is all alphanumeric
print(myStr.isalnum())

#is all alphabetic
m = 'Hello12'
print(m.isalpha())
print(myStr.isalpha())

# is all numeric
print(myStr.isnumeric())
u = '1235'
print(u.isnumeric())
