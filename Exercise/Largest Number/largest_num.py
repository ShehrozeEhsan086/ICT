lst = []
n = int(input("Enter the number of elemsts: "))
for i in range(0,n):
    element = int(input(" enter number: "))
    lst.append(element)
print(f"list = {lst}")

import utils
print(f"Largest value enetered is: {utils.find_largest(lst)}")