# intro to dictionaries and their functionalities

# dictionary is a collection of the form key: value pairs

lead = {
    "name": "Ahmed",
    "company": "abc limited",
    "budget": 10000
}

# print(lead)
# print(lead["budget"])

# for value in lead:
#     print(value)
#     print(type(lead[value]))
lead["country"] = "Pakistan"
print(lead.get("continent", "not present"))