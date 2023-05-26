#Setting rows to 5 
rows = 5

#Calculating number of stars for first row
num_stars = 2 * rows - 1

for i in range(rows, 0, -1):
    #calculating spaces for every row 
    spaces = (rows - i) 
    #printing the spaces followed by stars
    print(" " * (spaces) + "*" * num_stars)
    #for each precesing row the stars decrease by 2
    num_stars -= 2


