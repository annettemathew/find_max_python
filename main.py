num = 1
max = 0
while(num != 0):
    num = int(input("Please enter a number(0 to quit): "))
    if(num > max):
        max = num
    print("Max number so far: ", max)


