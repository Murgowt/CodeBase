# Function to display the final bill
def displayOutput(subTotal, salesTax, total):
    print(f"The Sub Total: ${subTotal}")
    print(f"The Tax: ${salesTax}")
    print(f"The Total: ${total}")

#Function to calculate the final amount
def calculate(price1, price2, price3):
    #Calculating the subtotal
    subTotal = price1 + price2 + price3
    #Tax implied on the items bought
    salesTax = subTotal * 0.0825
    

    # Final price is the sum of the tax and total of the 3 items
    total = subTotal + salesTax

    #Calling the DisplayOutput function to display the end result
    displayOutput(subTotal, salesTax, total)


    
# Main Function
#Input from the user on the amount of each of the three items
price1 = float(input("Please enter the first price: "))
price2 = float(input("Please enter the second price: "))
price3 = float(input("Please enter the third price: "))

# Calling the Calculate function to get the final Price
calculate(price1, price2, price3)