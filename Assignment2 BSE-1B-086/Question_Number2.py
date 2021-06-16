num1, num2, num3 = eval(input("Enter three integers seperated by ',' : "))
if num1 == num2 == num3:
    print(3)
elif num1 == num2 and num2 != num3:
    print(2)
elif num2 == num3 and num2 != num1:
    print(2)
elif num3 == num1 and num2 != num1:
    print(2)
else:
    print(0)  

# Shehroze Ehsan 086  