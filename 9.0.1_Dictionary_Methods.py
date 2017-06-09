print("**Clear() method**")
dict1 = {'Name':'Zara','Age':7}
print("Start Len: ", len(dict1))
dict1.clear()
print('End Len: ',len(dict1))

print("\n")
print("**Copy() method**")
dict2 = {'Subject':['phy','Che']}
dict3 = dict2.copy()
print("New Dictionary: ", str(dict3))

print("\n")
# fromkeys method
print("**fromkeys() Method**")
#creates a new dictionary with keys from seq and values set to value.
seq = ('name','age','sex')
dict = dict.fromkeys(seq)
print("New Dictionary: ", str(dict))
dict = dict.fromkeys(seq,10)# set the values for all the dictionary
print("New Dictionary: ", str(dict))
dict = {'Name':'Suru'}
print(" Values: ", dict.get('Name'))

print("\n")
# get() Method
# if value is not present then it will show "None"
print("**get() method**")
dict4 = {'Name' : 'Suru',}
print("Value: ", dict4.get('Education',"Not contains any value"))

print("\n")
#items() method
# returns a list of vale and keys
print("**items() method**")
dict1 = {'Name':'Suru','Address':'ABC'}
print("Values: ", dict1.items())

print("\n")
#keys()method
#returns a list of all the available keys in the dictionary.
print("**keys() method**")
dict1 = {'Name':'Suru','Age':19}
print('Values: ', dict1.keys())

print("\n")
# setdefault() method
#The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
print("**setdefault() Method**")
dict1 = {'Name':'Suru','Age':19}
print("Values: ",dict1.setdefault('Age',None))
print("Values: ",dict1.setdefault('Gender',None))

print("\n")
#update()Method
# its directly doesn't update, 2 dictionary are added to update
print("**update() Method**")
dict1 = {'Name':'Suru'}
dict2 = {'Age':19}
dict1.update(dict2)
print("Values: ",dict1)

print("\n")
#values() method
#returns a list of all the values available in a given dictionary.
print("**values() method**")
dict0 = {'Name':'Suru','Age':19,'Gender':'M'}
print("Values: ",dict0.values())
