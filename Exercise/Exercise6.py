n = int(input("Enter the number you want sum till: "))
total = 0
i = 1
while i <= n:
    total += i 
    i += 1
print(f"Total sum from 1 to {n} is {total}")