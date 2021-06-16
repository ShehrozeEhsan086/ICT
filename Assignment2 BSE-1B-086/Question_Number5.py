password = input("Enter your password: ")
lowercase_aplhabets , uppercase_aplhabets , digits_ , special_character = False, False, False, False

if (len(password)>=6 and len(password)<=16):
    for i in password:
        if i.islower(): # checks for lowercase alphabets in password
            lowercase_aplhabets = True
        elif i.isupper(): # checks for uppercase alphabets in password
            uppercase_aplhabets = True
        elif i.isdigit(): # checks for digits in password
            digits_ = True 
        elif (i == "$") or (i == "#") or (i == "@"):
            special_character = True
        else:
            continue 
else:
    print("Entered password length not allowed!")

if (lowercase_aplhabets == True) and (uppercase_aplhabets == True) and (digits_ == True) and (special_character == True):
    print("Valid Password")
else:
    print("Invalid Password!")

# Shehroze Ehsan 086 