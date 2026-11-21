# sets - unique collection of elements
colors = {"red", "green", "blue", "yellow", "red"}
print(type(colors))  # Output: <class 'set'>
print(colors)  
#colors.clear()  # remove all elements
print("before: ", colors)  # Output: set()
colors.add("orange")  # add element


#colors = {"red", "green", "blue", "yellow", "red", [99, 100]}
#set only only take mutable data types like int, float, string, tuple. It will not take mutable data types like list, dict, set.
#does noy alow duplicate values. It will only take unique values.
# does not maintain the order of elements. It will not take index values. It will not take slicing. 