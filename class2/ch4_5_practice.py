# # Q1. Make a list of 6 numbers. Print the total number of elements, the sum, the largest, and the smallest number.
# myList = [1, 2, 3, 4, 5, 6]

# elements_count = len(myList)
# print(f"Total number of elements: {elements_count}")

# sum_of_elements = sum(myList)
# print(f"Sum of all elements: {sum_of_elements}")

# largest_element = max(myList)
# print(f"Largest element: {largest_element}")

# smallest_num = min(myList)
# print(f"Smallest element: {smallest_num}")


# # Q2. Take the list [10, 20, 30, 40, 50]. Print the elements from index 1 to 3 using slicing.
# index_list = [10, 20, 30, 40, 50]
# print(f"Element at index 1 to 3: {index_list[1:4]}")


# # Q3. Make a list of 5 names. Add 2 more names using append(), sort the list alphabetically, then remove the last name using pop() and print the list at each step.
# names = ["Eve", "Charlie", "Alice", "David", "Bob"]
# #names.reverse()
# print(f"Names Before Append: {names}")
# names.append("Grace")  # Add a new name to the list
# names.append("Frank")  # Add another new name to the list
# print(f"Names After Append: {names}")

# names.sort()
# print(f"Sorted Names: {names}")

# names.pop(len(names)-1)
# print(f"last index poped: {names}")


# # Q4. Make a tuple of 4 subjects. Print its length, then try to change one item. In a comment, explain why the program gives an error.
# subjects = ("Maths", "Urdu", "Chemistry", "Physics")
# print(f"Total Subjects: {len(subjects)}")

# subjects[0] = "English"
# #TypeError: 'tuple' object does not support item assignment
# # because tuples are immutable, values cannot changed at run time/after initialization.
# # test_int = 45
# # test_float = 34.22
# # print(f"Before int: {test_int} float: {test_float}")
# # test_int.real = 65
# # test_float.real = 87.99
# # print(f"After int: {test_int} float: {test_float}")


# # Q5. Make a tuple of 5 numbers. Print the first and last number, and count how many times 10 appears in it.
# numbers_tup = (2, 10, 6, 8, 10)
# print(f"first Num: {numbers_tup[0]}")
# print(f"Last Num: {numbers_tup[len(numbers_tup)-1]}")
# print(f"10 appears: {numbers_tup.count(10)} time(s)")


# Q6. Make a dictionary of 3 students and their marks. Print all keys, all values, and one student's marks. Then update one student's marks and add a new student. Print the final dictionary.
students = {
    "std1": {
        "Name" : "Akrima",
        "Marks": 80
    },
    "std2": {
        "Name" : "Hammad",
        "Marks": 90
    },
    "std3": {
        "Name" : "Daniyal",
        "Marks": 75
    }
}

# print all keys
#print(f"Top Keys: {students.keys()}\n")
#print(f"Inside Keys: {dict(students.values())}\n")
all_keys = list(students.keys()) + list(dict(students.values())) + list(dict(students.values()).values())
print(f"All Keys: {all_keys}")

# print all values
#print(f"Inside Values as Dict: {dict(students.values())}\n")
#print(f"Inside Values as List to dict: {list(students.values())}\n")
all_values = list(students.values()) + list(students["std1"].values()) + list(students["std2"].values()) + list(students["std3"].values())
print(f"All Values: {all_values}")

# print one student marks
print(f"{students["std1"]["Name"]}'s Marks: {students["std1"]["Marks"]}")

# update one student's marks 
print(f"Std2 Marks before: {students["std2"]["Marks"]}")
students["std2"]["Marks"] = 79
print(f"Std2 Marks before: {students["std2"]["Marks"]}")

# add a new student
students["std4"] = {
    "Name": "Khurram",
    "Marks": 55
}

# print final dictionary
print(f"Final Dictionary:\n{students}")




