# Taking input for miles per gallon and stopping value
mpg = int(input("Enter the number of miles per gallon: "))
stop = int(input("Enter the stopping value: "))

# Printing heading
print("Gallons\tMiles")

# Initializing gallons to 1
gallons = 1

# Looping through until stopping value
while gallons <= stop:
    miles = mpg * gallons
    # Printing detail line if gallons is divisible by 10
    if gallons % 10 == 0:
        print(f"For {gallons} the car can travel {miles} miles")
    else:
        print(f"{gallons}\t{miles}")
    gallons += 1
