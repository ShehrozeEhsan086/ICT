import math
x1 , y1 = eval(input("Enter two points of latitude in degree (comma seperated): "))
x2 , y2 = eval(input("Enter two points of longtitube in degree (comma seperated): "))
radius = 6371


def rad_con(degree):
    return math.radians(degree) # Takes Radian value and Returnes degree value.


x1_deg = rad_con(x1)
x2_deg = rad_con(x2)
y1_deg = rad_con(y1)
y2_deg = rad_con(y2)

d = radius * math.acos(math.sin(x1_deg) * math.sin(x2_deg) + math.cos(x1_deg) * math.cos(x2_deg) * math.cos(y1_deg - y2_deg))
distance = round(d,3)
print(f"Distance between the the points is {distance} Km")