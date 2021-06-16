print("Guessing GAME!!!")
import random # imports 'random' module
num = (random.randint(0,10)) # assigns a random number b/w 0-10 to variable
user = int(input("Enter a number between 0-10: "))
if(num==user):
    print("CONGRATUALATION you guessed correct.")
else:
    if(user<num):
        print("Too low better luck next time")
    else:
        print("Too high better luck next time")
print(f"The randomly generated number this time was: {num}")
# end of program 