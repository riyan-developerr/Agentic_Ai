""" 
Understanding lists and dictionaries

Lists: are used to store multiple values in one name(at one place)
e.g: names = ['riyan', 'zain' etc]
"""

# creating a list
names = ["riyan","hamza"]

# accessing a llist using indexing also negative indexong
print(f"member of list: {names[0]}")
print(f"member of list: {names[-1]}")

# Muteable
names[0] = "Ahmed"
print(f"member of list: {names}")

# adding a value to the list
# we can also add using insert key word
names.append("Riyan")
names.insert(0, "Qasim")
print(f"member of list: {names}")


# now removing elements
# remove: can remove with name 
# pop : removes item with index ( by default last element)

names.remove("Riyan")
names.pop(0)
print(f"member of list: {names}")

# loop through the list
if "Ali" in names:
    print("ali si present")
else:
    print("ali is not present")
  
    
""" 
looping thorugh the list 
"""
for name in names:
    print(f"name: {name}")
    
companies = ["microsoft", "Amazon", "Azure","Google"]
for company in companies:
    print(f"name: {company}")