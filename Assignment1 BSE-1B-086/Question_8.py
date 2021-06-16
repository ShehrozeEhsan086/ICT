# Checks if a point with coordinates (x,y) are  inside a circle.

point_x, point_y = eval(input("Enter value for point on x-axis and y-axis(seperate by comma): "))
center_point_x , center_point_y = 0,0 # defining center points(0,0) not necessary; is important if the center points are to be changed in the future.  

distance = ( (point_x - center_point_x)**2 + (point_y - center_point_y)**2 )**0.5 

if distance <= 10 :
    print(f"Point ({point_x},{point_y}) is in the circle.")
else:
    print(f"Point ({point_x},{point_y}) is not in circle.")

# Shehroze Ehsan BSE-1B 086