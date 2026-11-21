# 1. make a list of fruits and print the first and last fruit in the list
fruits = ["apple", "banana", "cherry", "orange", "Banana"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 2. make list of numbers [4, 2, 9, 1, 7] and print the sum and largest number in the list
numbers = [4, 2, 9, 1, 7]
print ("Sum of numbers:", sum(numbers))
print("Largest number", max(numbers))
print("Smallest number", min(numbers))
print("Average of numbers", sum(numbers)/len(numbers))


# 3. make an empty list the add three of your friends name using append(). print the list the remove the last name using pop.
friends = []
friends.append("Daniyal")
friends.append("Hammad")
friends.append("Irtiza")
print("Friends: ", friends)

friends.pop(-1)
print("Friends after removing the last name: ", friends)

# 4. make a tuple of 5 colors. print the first color and count how many time red appears in it
colors = ("green", "red", "blue", "yellow", "red")
print("first color: ", colors[0])
print("red count: ", colors.count("red"))


# 5. try to change one value inside a tuple, and see what happends. write a comment explaint why it gives and error
colors[0] = "black"
# This will give a TypeError because tuples are immutable and their values cannot be changed after creation.