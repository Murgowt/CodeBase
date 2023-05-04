print("Calculate 67 - 55 =")
answer = -1
while answer != 12:
    answer = int(input())
    if answer == 12:
        print("Correct Answer.")
    elif answer == 0:
        print("The correct answer is 12.")
        break
    else:
        print("Incorrect Answer.")
        print("Calculate 67 - 55 =")