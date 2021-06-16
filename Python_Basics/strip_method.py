# Strip Method 
name = "    Shehroze    "
dots = "................"
print(name+dots)
# 1. lstrip() method : left strip
print(name.lstrip() +dots)
# 2. rstrip() method : right strip 
print(name.rstrip() +dots)
# 3. strip() method : all strip 
print(name.strip() +dots)
# ex of space between a variable 
name1 = "  She hroz e "
# strip() will not be able to remove spaces between letters.
# replace() method.
print(name.replace(" ","")+dots) # replce space with no space 