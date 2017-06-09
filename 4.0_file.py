#open a file
fo = open('test.txt', 'w')
#Get some info
print('Name: ', fo.name)
print('Is Closed: ', fo.closed)
print('Opening Mode: ', fo.mode)
# WRITE IN TEST.TXT FILE FROM PYTHON
fo.write('I Love Python')
fo.write(' and javascript')
fo.close()

#AFTER CLOSEING FILE WE HAVE TO AGAIN OPEN THAT FILE
# THIS CODE WILL ERASE THE DATA PRESENT IN THE FILE BECAUSE WE ARE IN OPEN MODE
#write file
fo = open('test.txt', 'w')
fo.write('I also like PHP')
#close file
fo.close()

#open to append
fo = open('test.txt', 'a')
fo.write(' AND PYTHON ')
fo.close()

# Read from file
fo = open('test.txt', 'r+')
text = fo.read(10)# we can also put limit
text1 = fo.read()
print(text)
print(text1)
fo.close()

#Create file from script
fo = open('test1.txt', 'w+')
fo.write('This is my new file')
fo.close()
