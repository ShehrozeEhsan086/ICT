sum_ = 0
for number in range(1,10001):
    for i in range(1, number):
        if(number % i == 0):
            sum_ = sum_ + i
    if (sum_ == number):
        print(f"{number}\tis a Perfect Number" )
    sum_ = 0

# Shehroze Ehsan 086 