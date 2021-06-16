# Gets an integer and adds its digits.

num = int(input("Enter a number between 0-1000: "))

temporary_var1 = num % 10
num = num // 10
temporary_var2 = num % 10
num = num // 10

print(f"The sum of the digits is { temporary_var1 + temporary_var2 + num }")

# Shehroze Ehsan BSE-1B 086