def is_even(num):
    return num%2==0

def is_positive(num):
    return num>=0

def Factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

def main():
    
    num = int(input("Enter a number: "))

    user_options = input("Specify the task you want to perform, write 'even' 'positive' to check their states and 'Factorial' to find factorial of number: ")
    
    if user_options == "even":
        is_even(num)
        if is_even(num):
            print("The value entered is even")
        else:
            print("The value entered is odd")
    elif user_options == "positive":
        is_positive(num)
        if is_positive(num):
            print("The value entered is positive")
        else:
            print("The value entered is negative")
    elif user_options == "factorial":
        Factorial(num)
    else:
        print("unknown task")

main()