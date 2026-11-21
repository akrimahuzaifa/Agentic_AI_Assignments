
tup = ("red", "green", "blue", 1, 2, 3, 4, 5)
newTup = ("orange") #string
newTup = ("orange",) #tuple
print(type(tup))
print(type(newTup))

print(tup[0])  # Output: "red"
tup[0] = "yellow"  # This will raise an error because tuples are immutable

