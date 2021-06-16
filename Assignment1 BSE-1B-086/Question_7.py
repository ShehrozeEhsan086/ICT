# Reads three edges of a triangle and calculates parameter if input in valid.

edge1, edge2, edge3 = eval(input("Enter three edges (seperate by comma): "))

if (edge1 + edge2 > edge3) and (edge1 + edge3 > edge2) and (edge2 + edge3 > edge1):
    parameter = edge1 + edge2 + edge3
    print(f"The parameter is {parameter}")
else:
    print("The input is invalid")
    
 # Shehroze Ehsan BSE-1B 086