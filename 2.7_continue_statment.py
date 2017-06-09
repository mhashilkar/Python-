numbertaken = [2, 4, 6, 7, 10, 22, 25, 72, 30, 28]

print("Here are the numbers are still available")

for n in range(1, 20):
    if n in numbertaken:
        continue
    print(n)

"""
	The number 1 to 20 and it will print all the numbers which are not $numbertaken
it going to check if 1 in ther in $numbertaken if it doesn't it going to stip it

1. the first time n equals 1 so is in the number taken is nop
so it will print 1
2. next, n =2 and the number is taken yes it is so continue what is that any thing after that 
skip it and go back to loop and start it again


"""