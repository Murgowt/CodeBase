# You take an integer input from user 
#if the input is less than 0; if negative, print 0 to -10
# if its positive ; print 0 to 10

#Part 1: integer input
#Part 2: finding out the condition ; pos/neg
#Part 3: printing the result

integer = int(input("Enter a value: "))
if(integer<0):
    for i in range(0,-11,-1):
        print(i)
else:
    for i in range(0,11,1):
        print(i)
