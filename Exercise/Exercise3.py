name, char = input("Enter your name and a random letter ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"char count in your name {name.count(char)}") #case sensitive 

# to remove case sensitivity convert both input to lower case
# print(name.lower().count(char.lower())) solves case sensitivity

# if user has spaces then following will fix it
print("corrected :")
print(name.strip().lower().count(char.strip().lower()))