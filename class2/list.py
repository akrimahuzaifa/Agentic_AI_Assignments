#fruits = ["apple", "banana", "cherry", "orange", "Banana"]

# print(fruits[-2])  # Output: apple
# print(len(fruits))  # Output: 5

# #CRUD operations
# # create, read, update, delete

# #create
# fruits.append("date") #add in last
# print(fruits)  

# #update
# fruits[0] = "grapes"
# print(fruits)  

#fruits.clear()  # remove all elements
# print("Before: ", fruits)  # Output: []

#print(fruits.count("banana"))  # Output: 1

# fruits.pop(2) # remove element at index 2
# fruits.remove("Banana") # remove element by value
# print("After: ", fruits)

# fruits.insert(2, "grapes")  # insert element at index 2
# print("After: ", fruits)  # Output: ['grapes', 'banana', 'cherry', 'orange', 'Banana']

# fruits.reverse()  # reverse the list
# print("Reversed: ", fruits) 


# List Copy as a reference
# list1 = [1, 2, 3, 4, 5]
# #list2 = [5, 6, 7, 8, 9]
# list2 = list1 
# list2[0] = "usama"
# print("List1: ", list1) 
# print("List2: ", list2)

#shallow copy vs deep copy

#shallow copy
# list1 = [1, 2, 3, 4, 5]
# list2 = list1.copy()  # shallow copy
# list2[0] = "usama"
# print("List1: ", list1)
# print("List2: ", list2)

#deep copy
# import copy
# list1 = [1, 2, 3, 4, 5, [98,99]]
# list2 = list1.copy()  # shallow copy
# list2 = copy.deepcopy(list1)  # deep copy
# print(list2[5])
# print(list2[5][0])

# list2[5][0] = 100
# list2[0] = "usama"
# print("List1: ", list1)
# print("List2: ", list2)



