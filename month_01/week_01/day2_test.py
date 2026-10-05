"""  
Exercises : 01
"""

industries = ["SaaS",
"Real Estate",
"E-commerce",
"Healthcare",
"Finance"]

print(industries[0])
print(industries[-1])
print(f"Number of industries: {len(industries)}")

for x in range(len(industries)):
    if industries[x] == "Healthcare":
        industries[x] = "AI"
        break
    
# for indx, industry in enumerate(industries):
#     if industries[indx] == "Healthcare":
#         industries[indx] = "AI"
#         break
    
# print(industries)

""" excercise number: 02
"""

budgets = [3000, 7500, 12000, 4500, 9000]
total = 0

for budget in budgets:
    total += budget
    print(budget,end=" ")
   
 
print(f"\ntotal amount: {total}")


# next exercise
leads = ["Ali", "Hamza", "Ahmed"]
leads.append("Usman")
leads.remove('Hamza')
leads.insert(1,"Bilal")

print(f"leads: {leads} \ncount of leads: {len(leads)}")


# printing budgets greater than 5000
budgets = [3000, 7500, 12000, 4500, 9000]
for budget in budgets:
    if budget > 5000:
        print(budget)