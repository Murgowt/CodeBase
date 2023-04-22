#Taking the distance and time inputs from the user
distance = int(input("Enter the distance travelled in miles: "))
time = int(input("Enter the time travelled in hours: "))

#Calulcating the speed of the car as distance divided by time
speed = distance/time

#Comparing the speed with the 60mph speed limit
if(speed < 60):
    #if the speed is less than the limit
    print("Below the speed limit!")
elif(speed == 60 ):
    #if the speed equals the limit
    print("At the speed limit!")
else:
    #If the speed exceeds the limit
    print("Above the speed limit!")