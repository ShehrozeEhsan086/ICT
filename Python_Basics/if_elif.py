# ticket prices
age = int(input("Please enter your age: "))
if(age>0):
    if(0<age<=3):
        print("Ticekt is free")
    elif(4<=age<=10):
        print("Ticket price is Rs.150")
    elif(11<=age<=60):
        print("Ticket price is Rs.200")
    else:
        print("Ticket price is Rs.250")
else:
    print("Wrong Input")