# basics

# variables

name = 'riyan ahmed'
age = 19

print(name,age)

# combining strings

first_name = 'Riyan'
last_name = 'Ahmed'

complete_name = first_name + ' ' + last_name
print(complete_name)

# flaots bool
marks = 97.4
temperatur = -5

# booleans
budget = 5000
is_feasible = budget < 10000
print(is_feasible)

# None type 
prize = None
print(prize)

# f-string 
print(f'my name is {name} and i am {age} years old')

# operations
# (floor division)
result = 5 ** 3
print(f"result = {result}")

# type conversion
"""  
useful for conversion number in string form to int or other form
"""

budget = "5000"
print(type(budget))
budget = int(budget)
print(type(budget))

# comparison operators
if budget < 1000:
    print(f"Acceptable")
else:
    print(f"expensive")


""" 
Excercise number : 01
"""
name = 'Riyan Ahmed'
age = 19
university = 'GIKI'
height = 61.32
is_student = True

print("===========================")
print("Student Details:")
print("===========================")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"University: {university}")
print(f"Height: {height}")
print(f"Is_student: {is_student}")


""" 
Excercise number : 02

total price then 10 % discount
"""

price = 120
quantity = 5

total_price = price * quantity
discounted_price = total_price - (total_price * 0.1)

print("===========================")
print("Price Calculation:")
print("===========================")
print(f"total price: {total_price}")
print(f"discounted price: {discounted_price}")


""" 
Excercise number : 03

type conversion
"""

age = "20"
price = "1499.99"

# converting to appropriate types
age = int(age)
price = float(price)

age = age + 5
price = price * 2

print("===========================")
print("age Calculation:")
print("===========================")
print(f"age: {age} \nprice: {price}")

""" 
Excercise number : 04

Real lead data
"""
# leads data
lead_name = 'Hamza'
industry = 'SAAS'
company_size = 10
budget = "500"
is_urgent = True

# type conversion to proper type
budget = int(budget)
print("=======================")
print("Lead details:")
print("=======================")
print(f"Name: {lead_name}")
print(f"industry: {industry}")
print(f"company_size: {company_size}")
print(f"budget: {budget}")
print(f"is_urgent: {is_urgent}")


# self learning and testing

# manually reversing the string
def reverse(string):
    temp = ""
    for index in range(len(string)):
        temp = temp + string[(len(string) - index - 1)]
    return temp

add = "hello"
print(f"the length of string is: {len(add)}")
print(add, reverse)

result = reverse(add)
print(f"using self made function: {result}")

# today i revised to basics variables , print , type casting and basic operators ,also string manuplation