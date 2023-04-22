#Function to calculate tax and then output the tip and the toal bill
def calculateTipAndDisplayTotalBill(foodBill):
    #Calculating the tip as 20% of the cost of food
    tip = foodBill * 0.20

    #Calculating the total bill including the cost of food and tip
    total = foodBill + tip

    #Displaying the output
    print("The tip given is: $", tip)
    print("Total bill is : $", total)

#Taking the food bill input from the user
foodBill = int(input("Please Enter the cost of the food: "))

#calling the function to calculate the tip and display the total bill
calculateTipAndDisplayTotalBill(foodBill)