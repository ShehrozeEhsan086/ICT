import sys

def is_prime(num):
    div = 2
    while div <= num / 2:
        if num % div == 0:    
            return False
        div += 1
    return True

def is_pelindrome(num):
    temp_var = str(num)
    reversed_variable = temp_var[::-1]
    if reversed_variable ==  temp_var:
        return True
    else:
        return False

palindrome_condition = False
prime_condition = False
count = 0
total_count = 0

for num in range (2,94100):
    prime_condition = is_prime(num)
    palindrome_condition = is_pelindrome(num)

    if prime_condition == True and palindrome_condition == True:
        print(format(num,"6d"),end=" ")
        count += 1
        total_count += 1
    if count == 10:
        print()
        count = 0
    if total_count == 100:
        sys.exit()

# Shehroze Ehsan 086 