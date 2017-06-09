age = 12

if age < 21:
    print("No bear to u")
elif age <= 21:
    print("which brand beer you want")
elif age > 21:
    print("which brand beer you want")


name = "surumuru" # will comparing string "is" is used 
if name is "muru":
    print(" Muru")
elif name is "suru":
    print(" Suru")
else:
    print("Suru Muru")


x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print("Negative change to zero")
elif x == 0:
	print("zero")
elif x == 1:
	print("one")
else:
	print("more")