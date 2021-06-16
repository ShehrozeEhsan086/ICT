count = 1
final_count = 1

print("Write a number then press enter, enter 0 to finish the sequence: ")

num = int(input())
last_num = num

while num != 0:
    num = int(input())
    if num == last_num:
        count += 1
    elif num != last_num:
        last_num = num
        if count > final_count:
            final_count = count
        count = 1

print(f"Length of widest fragment with elements equal to each other is {final_count}")

# Shehroze Ehsan 086 