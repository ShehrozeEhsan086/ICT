number_list = []
temporary_list = []
final_list = []
count = 0

n = int(input("Enter the length of list: "))

print("Enter a number then press enter.")

for i in range(0,n):
    numbers = int(input())
    number_list.append(numbers)

temporary_list = number_list

for j in range(0,n):
    for k in range(0,n):
        if temporary_list[j] == number_list[k]:
            count += 1 
    if count == 1 :
        final_list.append(temporary_list[j])
    count = 0

print(f"Original list {number_list}")
print(f"List {final_list}")

# Shehroze Ehsan 086 