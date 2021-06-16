import sys

list1 = []
original_list = []

for i in range(0,4):
    val = int(input("enter the value: "))
    list1.append(val)
    original_list.append(val)

count= 0
state = True

while state== True:
    val0 = abs(list1[0]-list1[1])
    val1 = abs(list1[1]-list1[2])
    val2 = abs(list1[2]-list1[3])
    val3 = abs(list1[3]-list1[0])
    count += 1
    # print(count)
    list1[0] = val0
    list1[1] = val1
    list1[2] = val2
    list1[3] = val3
    # print(f"{val0} {val1} {val2} {val3}")
    if val0==val1 and val1== val2 and val2==val3:
        print(f"{original_list} required {count} iteration to reach common number.That is {list1}")
        sys.exit()