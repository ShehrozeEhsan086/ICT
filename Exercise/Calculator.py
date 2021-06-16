# Basic Calculator with 2 or 3 operands (INCOMPLETE)
operands = input("Enter the numbers of operands you want to use(2 OR 3): ")
print("Use + , - , x , / when asked for which operation to perform")
if(operands=="2"):
    num1,num2= eval(input("Enters numbers seperated by ',' : "))
    operation = input("Enter which operation you want to perform: ")
    if(operation=="+"):
        answer=num1+num2
    else:
        pass
    if(operation=="-"):
        answer=num1-num2
    else:
        pass
    if(operation=="x"):
        answer=num1*num2
    else:
        pass
    if(operation=="/"):
        answer=num1/num2
    else:
        pass
else:
    pass
if(operands=="3"):
    num1,num2,num3= eval(input("Enters numbers seperated by ',' : "))
    operation = input("Enter which operation you want to perform: ")
    if(operation=="+"):
        answer=num1+num2+num3
    else:
        pass
    if(operation=="-"):
        answer=num1-num2-num3
    else:
        pass
    if(operation=="x"):
        answer=(num1*num2*num3)
    else:
        pass
    if(operation=="/"):
        answer=num1/num2/num3
    else:
        pass
else:
    pass
print(f"Answer = {answer}")
# end of program