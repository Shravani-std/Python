# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"]) 
print(person["age"])  


# Creating a dictionary with mixed value types
data = {
    "integer": 42,
    "float": 3.14,
    "string": "Hello, World!",
    "boolean": True,
    "list": [1, 2, 3],
    "dictionary": {"key": "value"}
}

# Accessing values
print(data["integer"])     
print(data["float"])       
print(data["string"])     
print(data["boolean"])      
print(data["list"])        
print(data["dictionary"])   


# Creating a nested dictionary
employee = {
    "name": "Bob",
    "position": "Engineer",
    "contact": {
        "email": "bob@example.com",
        "phone": "123-456-7890"
    },
    "skills": ["Python", "Java", "C++"]
}

print(employee["contact"]["email"]) 
print(employee["skills"][0])         
