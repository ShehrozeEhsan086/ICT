# Checks if number is palindrome. 

num = int(input("Enter a three digit integer: "))

first_digit = num // 100
last_digit = num % 10


if first_digit == last_digit:
    print(f"The number {num} is a palindrome.")
else:
    print(f"The number {num} is not a palindrome.")

# Shehroze Ehsan BSE-1B 086