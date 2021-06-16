year = int(input("Enter the year: "))
first_day=int(input("Choose the first day of the year:\n1 for Monday\n2 for Tuesday\n3 for Wednesday\n4 for Thursday\n5 for Friday\n6 for Saturday\n7 for Sunday.\nNow Enter: "))
def day_assign(n):
    if n == 1:
        return "Monday"
    elif n == 2:
        return "Tuesday"
    elif n == 3:
        return "Wednesday"
    elif n == 4:
        return "Thursday"
    elif n == 5:
        return "Friday"
    elif n == 6:
        return "Saturday"
    elif n == 7:
        return "Sunday"
month = ["February","March","April","May","June","July","August","September","Octuber","November","December"]

h = first_day
t = day_assign(h)
print(f"January 1, {year} is {t}") # prints the initial date.

for i in range(0,11):
    
    if i == 0: 
        
        for t in range(1,32): 
            h+=1
            if h>7:
                h=1       
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of febraury
    if i == 1:
        if year % 4 != 0: # check for lunar year.
            
            for t in range(1,29):
                h+=1
                if h>7:
                    h=1
        else:
             
            for t in range(1,30):
                h+=1
                if h>7:
                    h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of march
    if i == 2:
        
        for t in range(1,32):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of april
    if i == 3:
        
        for t in range(1,31):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of may
    if i == 4:
        
        for t in range(1,32):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of june
    if i == 5:
        
        for t in range(1,31):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of july
    if i == 6:
        
        for t in range(1,32):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of august
    if i == 7:
        
        for t in range(1,32):
            h += 1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of september
    if i == 8:
        
        for t in range(1,31):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of octuber
    if i == 9:
        
        for t in range(1,32):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of november 
    if i == 10:
        
        for t in range(1,31):
            h+=1
            if h>7:
                h=1
        p = h
        p = day_assign(h)
        print(f"{month[i]}  1, {year} is {p}") # will print first day of december


# Shehroze Ehsan 086 