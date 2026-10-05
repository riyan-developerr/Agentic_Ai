# dictionary exercise

lead = {
    "name": "Hamza",
    "company": "AI Solutions",
    "industry": "SaaS",
    "employees": 50,
    "budget": 8000,
    "urgent": True
}

print(f"name:{lead.get("name")}")
print(f"company:{lead.get("company")}")
print(f"budget:{lead.get("budget")}")
# changing budget
lead["budget"] = 10000

# adding new key
lead["country"] = "Pakistan"

print("=======================")
print("final details:")
print("=======================")
for key,value in lead.items():
    print(f"{key} : {value}")
    

# exercise number : 02

lead["industry"] = "AI"
lead["email"] = "hamza@example.com"
print("email:",lead.get("email","unknown email"))

if "phone" in lead:
    print("phone exists in the dictionary")
else:
    print("phone does not exist in the dictionary")
    
for key,value in lead.items():
    print(f"{key} : {value}")
    

# exercise number: 03

leads = [
    {"name": "Ali", "budget": 5000},
    {"name": "Hamza", "budget": 8000},
    {"name": "Ahmed", "budget": 12000}
]

# for lead in leads:
#     if lead["name"] == "Ali":
#         print(f"{lead['budget']}")
#     if lead["name"] == "Hamza":
#         print(lead["name"])
#     if lead["name"] == "Ahmed":
#         print(lead["budget"])
print(leads[0]["budget"])
print(leads[1]["name"])
print(leads[2]["budget"])
        

for lead in leads:
    print(f"{lead['name']} - {lead['budget']}")


# mini challenge # 04
leads = [
    {"name": "Ali", "budget": 3000, "urgent": False},
    {"name": "Hamza", "budget": 7500, "urgent": True},
    {"name": "Ahmed", "budget": 12000, "urgent": True},
    {"name": "Bilal", "budget": 4500, "urgent": False}
]

# printing names of all the leads
for lead in leads:
    print(lead["name"])
    
for lead in leads:
    if lead["budget"] > 5000:
        print(f"{lead['name']} - {lead['budget']}")

print(f"total number of leads: {len(leads)}")

# exercise number # 05

for lead in leads:
    # response = ""
    # response += lead["name"]
    # if lead["budget"] > 5000:
    #     response += "- high budget"
    # else:
    #     response += "- low budget"
        
    # if lead["urgent"] == True:
    #     response += "- Urgent"
    # else:
    #     response += "- Normal"
    
    if lead["budget"] > 5000:
        if lead["urgent"] == True:
            print(f"{lead['name']} - high budget - Urgent") 
        else:
            print(f"{lead['name']} - high budget - Normal") 
    else:
        if lead["urgent"] == True:
            print(f"{lead['name']} - low budget - Urgent") 
        else:
            print(f"{lead['name']} - low budget - Normal") 
        
                   
    # print(response)
        