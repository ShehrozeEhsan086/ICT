# Gets intetegers and print them in ascending order.

num1 , num2 , num3 = eval(input("Enter three nummber (seperated by comma): "))

smallest_num = min(num1,num2,num3)
largest_num = max(num1,num2,num3)
middle_num = num1 + num2 + num3 - smallest_num - largest_num

print(f"Ascending Order: {smallest_num},{middle_num},{largest_num}")

# Shehroze Ehsan BSE-1B 086