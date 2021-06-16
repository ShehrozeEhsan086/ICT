import sys

list1 = [] 
list2 = [] 
count = 0

len_list1 = int(input("Enter the size of list 1: "))
print("Enter the values of list 1, press enter after every value.")

for lst1 in range(0,len_list1):
    val0 = int(input())
    if count == 0: # Using count to mimic do while loop, as the first values is stored in temporary value without any check.
        tempval = val0
        list1.append(val0)
    if count != 0:
        if tempval > val0:
            print("A smaller number cannot be entered in a list. Rerun the program with correct values.")
            sys.exit() # Will close program if encountered.
        else:
            list1.append(val0)
        tempval = val0
    count += 1

count = 0
tempval = 0

len_list2 = int(input("Enter the size of list 2: "))
print("Enter the values of list 2, press enter after every value.")
for lst2 in range(0,len_list2):
    val1 = int(input())
    if count == 0: # Using count to mimic do while loop, as the first values is stored in temporary varibale without any check.
        tempval = val1
        list2.append(val1)
    if count != 0:
        if tempval > val1:
            print("A smaller number cannot be entered in a list. Rerun the program with correct values.")
            sys.exit()
        else:
            list2.append(val1)
        tempval = val1
    count += 1

print (f" list 1 is : {list1}" ) 
print (f" list 2 is : {list2}" ) 

final_list = [] 
i, j = 0, 0
  
while i < len_list1 and j < len_list2: 
    if list1[i] < list2[j]: 
      final_list.append(list1[i]) 
      i += 1
  
    else: 
      final_list.append(list2[j]) 
      j += 1

for t in range(i, len_list1):
    final_list.append(list1[t])
for k in range(j,len_list2):
    final_list.append(list2[k])

print (f"The combined sorted list is : {final_list}") 

# Shehroze Ehsan 086 