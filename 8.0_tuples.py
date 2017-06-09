#A tuple is a sequence of immutable Python objects.

tup0 =(); #Empty tuple
# Value tuple
tup0 = (50,); # SIngle Value tuple
tup1 = ('Physics','Chemistry',1997,1998,2000);
tup2 = (1,2,3,4,5);
tup3 = "a","b","c";
print(tup1, tup2, tup3)
print("\n")

# Following action is not valid for tuples
# tup1[0] = 100;

# Updating tuple
print("****UPDATING TUPLE*****")
tup1 = (12, 34, 56);
tup2 = ('abc', 'xyz');
tup3 = tup1 + tup2;
print(tup3)

# Deleting tuples
print("\n")
print("****DELETING TUPLES****")
tup = ('phycis','Chemstry',1997,20017);
print(tup)
print("After Deleting Tuples:", tup)
del tup;
#print(tup) # THIS WILL SHOW ERROR TO YOU BECZ WE HAVE DELETED TUP & THEN ACCESING IT


# BASIC OPERATION ON TUPLES
print("\n")
print("****BASIC OPERATION ON TUPLE****")
tup1=('abcd',1234,'john','4567','70.2',3)
tup2 = ('john',1235)
print( tup1, tup2) #PRINT COMPLETE LIST OF TUPLE
print(tup1 * 2) #PRINT THE TUPLE LIST TWO TIMES)
print(len(tup1))# PRINT THE LENGHT OF TUPLE
print(3 in tup1) # TO CHECK THAT VALUE IS PRESENT IN TUPLE
print(tup1 + tup2) #Concatination of tuple

# Indexing And Slicing Of Tuples
print("\n")
print("**** Indexing And Slicing Of Tuples****")
t = "c++","Python","PHP"
print(t)
print( t[2])#Offsets start at zero
print( t[1:] )# Slicing fetches sections
print(t[-2]) #Negative: count from the right

# Built In Function in Python
tup1, tup2 = ('abc','xyz','zara'), (456,123)
print("\n")
print("****Built In () for tuple****")
# len()
print("****len() function ****")
print("First tuple length: ",len(tup1))
print("Second tuple length: ",len(tup2))
# max()
print("\n")
print("****max() function ****")
print("First tuple Max elements: ", max(tup1))
print("Second tuple Max elements: ", max(tup2))
# min()
print("\n")
print("****min() function ****")
print("First tuple Min elements: ", min(tup1))
print("Second tuple Min elements: ", min(tup2))
# seq() Converting list into tuple
print("\n")
list1= ['maths', 'che', 'phy', 'bio']
print("****tuple() function ****")
tuple1 = tuple(list1)
print("tuple elements: ", tuple1)
