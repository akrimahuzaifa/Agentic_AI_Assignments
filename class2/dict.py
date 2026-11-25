dictonary = {
    "std_name": "Akrima",
    "std_age": 20,
    "isPaid": False
    }

# curd operations
#print(dictonary["std_org"]) #error because key does not exist
print(dictonary.get("std_org"))  # Output: None

print("before:", dictonary) 
dictonary["std_name"] = "Hammad"
dictonary["std_inst"] = "Jawan Pakistan"
#dictonary.clear()  # remove all elements
#del dictonary["isPaid"] 

print("after: ", dictonary)  # Output: {}

print(dictonary.keys())  # Output: dict_keys(['std_name', 'std_age', 'isPaid'])
print(dictonary.values())  # Output: dict_values(['Akrima', 20

newList = list(dictonary.keys())  # convert dict to list of tuples
print("Keys as a list:", newList)