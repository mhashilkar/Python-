"""
1.Comma separated pairs of key and value enclosed in curly braces.
2.Each key is separated from (:)
3.KEY are unique within dictionary
4.Values can be ununique
"""
dict0 = {}#EMPTY DICT
dict1 = {'name':'john','code':123,'Dept':'COMPs'}
print(dict1)
# TO PRINT A VALUE FROM DICTIONARY
print("dict1['name']: ",dict1['name'])
print(dict1['code'])
print("Department of dict1: ",dict1['Dept'])

# UPDATE THE DICTIONARY
print('\n')
print("****UPDATE DICTIONARY****")
dict1 ['code'] = 786 # UPDATE THE EXISTING DICTIONARY
print(dict1['code'])
# ADD NEW ENTRY IN DICTIONARY
dict1['college'] = 'VIVA'
print("dict1['college']: ",dict1['college'])
print("After Update: ",dict1)

# DELETE OF DICTIONARY
dict2 = {'name':'john','code':123,'Dept':'COMPs'}
print("\n")
print("****DELETE DICTIONARY****")
print("Initial dictionary ",dict2)

# REMOVE ENTRY WITH KEY 'NAME'
del dict2['name']
print("Directory after removing elements :",dict2)

# REMOVE ALL ENTRIES IN dictionary
dict2.clear()
print("Directory after removing elements: ",dict2)

# DELETE ENTIRE Directory
del dict2
# print(dict2) it will show error because the dictionaryis delete


# BULID IN FUNCTION IN DICTIONARY
print('\n')
print("****BUILT IN FUNCTION IN DICTIONARY****")
dict3 = {'Name':'Suru','Age':19,'Studing' : 'Engineering'}
print(dict3)
# len() FUNCTION
print("**len() Function**")
print("Length :", len(dict3))# gives no of key in dictionary
# str() Function
print("**str() Function**")# string representation of dictionary
s = str(dict3)
print("equivalent string: ",s)
#type() Function
print("**type() Function**")
# this fuction used to get which type of class is used
print("Variable Type", type(dict3))
