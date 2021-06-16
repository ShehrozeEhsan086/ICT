number_of_value = int(input("Enter the number of values you are going to enter: "))
list1 = []
temp_list = []
for i in range(0,number_of_value):
    val = int(input("Enter the value: "))
    list1.append(val)


list1.sort(reverse=True)
print(list1)
for j in range(0,number_of_value):
    print(list1[j],end="")