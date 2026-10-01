# variables
Name = "Ali"
Company = "TechNova"
Industry = "SaaS"
Employees = 35
Budget = "7500"
Urgent = True

# correct type conversion
Budget = int(Budget)

# calculating annual budget
annual_budget = Budget * 12

# printing details
print(f"Lead: {Name}")
print(f"Company: {Company}")
print(f"Industry: {Industry}")
print(f"Employees: {Employees}")
print(f"Budget: {Budget}")
print(f"Urgent: {Urgent}")
print(f"type of budget: {type(Budget)}")
print(f"Annual budget : {annual_budget}")

if Budget > 5000:
    print(f"high budget lead")
else:
    print(f"low budget lead")
    
