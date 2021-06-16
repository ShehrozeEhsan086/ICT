Exapmle = input("Enter a number more than one digit: ")
n = len(Exapmle)
i = 0
total = 0
while i <= (n-1):
    total += int(Exapmle[i])
    i += 1
print(f"Total is {total}")