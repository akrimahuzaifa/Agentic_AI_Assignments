# Q1. Make a list of 6 numbers. Print the total number of elements, the sum, the largest, and the smallest number.
myList = [1, 2, 3, 4, 5, 6]

elements_count = len(myList)
print(f"Total number of elements: {elements_count}")

sum_of_elements = sum(myList)
print(f"Sum of all elements: {sum_of_elements}")

largest_element = max(myList)
print(f"Largest element: {largest_element}")

smallest_num = min(myList)
print(f"Smallest element: {smallest_num}")


# Q2. Take the list [10, 20, 30, 40, 50]. Print the elements from index 1 to 3 using slicing.
index_list = [10, 20, 30, 40, 50]
print(f"Element at index 1 to 3: {index_list[1:4]}")


# Q3. Make a list of 5 names. Add 2 more names using append(), sort the list alphabetically, then remove the last name using pop() and print the list at each step.
names = ["Eve", "Charlie", "Alice", "David", "Bob"]
#names.reverse()
print(f"Names Before Append: {names}")
names.append("Grace")  # Add a new name to the list
print(f"Names After Append: {names}")
names.append("Frank")  # Add another new name to the list
print(f"Names After Append: {names}")

names.sort()
print(f"Sorted Names: {names}")

names.pop(len(names)-1)
print(f"last index poped: {names}")


# Q4. Make a tuple of 4 subjects. Print its length, then try to change one item. In a comment, explain why the program gives an error.
subjects = ("Maths", "Urdu", "Chemistry", "Physics")
print(f"Total Subjects: {len(subjects)}")

#subjects[0] = "English" #committed because it will stop the entire file
#TypeError: 'tuple' object does not support item assignment
# because tuples are immutable, values cannot changed at run time/after initialization.
# test_int = 45
# test_float = 34.22
# print(f"Before int: {test_int} float: {test_float}")
# test_int.real = 65
# test_float.real = 87.99
# print(f"After int: {test_int} float: {test_float}")


# Q5. Make a tuple of 5 numbers. Print the first and last number, and count how many times 10 appears in it.
numbers_tup = (2, 10, 6, 8, 10)
print(f"first Num: {numbers_tup[0]}")
print(f"Last Num: {numbers_tup[len(numbers_tup)-1]}")
print(f"10 appears: {numbers_tup.count(10)} time(s)")


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
print(f"Std2 Marks After: {students["std2"]["Marks"]}")

# add a new student
students["std4"] = {
    "Name": "Khurram",
    "Marks": 55
}

# print final dictionary
print(f"Final Dictionary:\n{students}")


# Q7. Make a dictionary of 3 fruits and their prices. Ask the user for a fruit name and print its price using .get(). If the fruit is not present, print "Not available"
fruits = {
    "banana": 80,
    "apple": 200,
    "grapes": 400,
}
user_input = input(f"Enter fruit name for price: ").lower()
print(f"Fruit Price: {fruits.get(user_input, "Not available")}")



# Q8. Make a set of 5 numbers. Print its length, add one new number using add(), and remove one number using remove(). Print the set after each step.
num_set = {5, 6, 7, 8, 9}
print(f"Length of set: {len(num_set)}")
num_set.add(1)
print(f"set after add: {num_set}")
num_set.remove(9)
print(f"set after remove: {num_set}")

# Q9. Make a list [1, 2, 2, 3, 3, 3, 4]. Convert it into a set, print the unique values, and print the count of unique values.
num_list = [1, 2, 2, 3, 3, 3, 4]
print(f"Num List: {num_list}")
conv_set = set(num_list)
print(f"Set: {conv_set}")
print(f"Count Set: {len(conv_set)}")


# Q10. Ask the user for 5 numbers one by one, store them in a list, then print the list in sorted order and also print the list reversed.
user_num_list = []
user_num_list.append(int(input("Enter 1st number: ")))
#print(f"List now: {user_num_list}")

user_num_list.append(int(input("Enter 2nd number: ")))
#print(f"List now: {user_num_list}")

user_num_list.append(int(input("Enter 3rd number: ")))
#print(f"List now: {user_num_list}")

user_num_list.append(int(input("Enter 4th number: ")))
#print(f"List now: {user_num_list}")

user_num_list.append(int(input("Enter 5th number: ")))
print(f"List now: {user_num_list}")

list_copy_sort = user_num_list.copy()
list_copy_sort.sort()
print(f"Sorted List:\n{list_copy_sort}")

list_copy_reverse = user_num_list.copy()
list_copy_reverse.reverse()
#list_copy_reverse.sort(reverse=True)
print(f"Reverse List:\n{list_copy_reverse}")


