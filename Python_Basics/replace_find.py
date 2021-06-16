# replace() method
string = "she is beautiful and she is a good dancer"
print(string.replace(" ","_")) # replaces space with underscore 
print(string.replace("is","was")) # replaces is with was
print(string.replace("is","was",1)) #replaces the first is with was
print(string.replace("is","was",2)) #replaces both is in the sentence to was
# find() method
# find the location for a value
print(string.find("is"))
print(string.find("is", 5)) # will look for "is" after position 4
# if the location of the first "is" is unknown we can do;.
is_pos1 = string.find("is")
print(is_pos1)
is_pos2 = string.find("is",is_pos1 +1) # +1 so that it wont count the first "is"
print(is_pos2)