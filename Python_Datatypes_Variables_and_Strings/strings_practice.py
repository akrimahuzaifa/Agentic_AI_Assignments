# Problem 1. Import the math module and print the square root of 256 and the value of pi (π) using the module.
import math
sqrt_value = math.sqrt(256)
pi_value = math.pi
print("Square root of 256:", sqrt_value)
print("Value of Pi (π):", pi_value)
print("="*50 + "\n")


# Problem 2. Import the random module and write a program that prints a random number between 1 and 100 (both included).
import random
random_num = random.randint(1, 100)
print(f"Random number between 1 & 100: {random_num}")
print("="*50 + "\n")


# Problem 3. Write a program that prints "Hello" to the screen, and add a single-line comment and a multi-line comment explaining what your program does.
print("Hello")  # This line prints "Hello" to the screen
"""
This program prints "Hello" to the screen.
It also demonstrates the use of single-line and multi-line comments.
"""
print("="*50 + "\n")


# Problem 4. Use pip to install the pyjokes module, then write a program that imports it and prints one joke.
# run pip install pyjokes in terminal first then run this below code
import pyjokes
joke = pyjokes.get_joke()
print(f"Here's a joke for you: \"{joke}\"")
print("="*50 + "\n")


 # Problem 5. Import the os module and write a program that lists all the files and folders present in the current directory.
import os
files_and_folders = os.listdir("./")
print("Files and folders in the current directory: \n", files_and_folders)
print("="*50 + "\n")


# Problem 6. Create one variable of each of these data types — integer, float, string, boolean, and None — and print each value along with its type using type().
int_var = 89
float_var = 5.67
str_var = "My Name is Akrima"
bool_var = True
none_var = None

print(f"Integer value: {int_var}, Type: {type(int_var)}")
print(f"Float value: {float_var}, Type: {type(float_var)}")
print(f"String value: {str_var}, Type: {type(str_var)}")
print(f"Boolean value: {bool_var}, Type: {type(bool_var)}")
print(f"None value: {none_var}, Type: {type(none_var)}")
print("="*50 + "\n")


# Problem 7. Write a program that asks the user for two numbers, adds them, and prints the sum.
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

sum_of_numbers = num_1 + num_2
print(f"The sum of {num_1} and {num_2} is: \"{sum_of_numbers:.2f}\"")
print("="*50 + "\n")


# Problem 8. Ask the user to enter a number. Print its type before and after converting it to an integer (hint: int()).
user_input = input("Enter a number: ")
print(f"Type before conversion: {type(user_input)}")
user_input = int(user_input)
print(f"Type after conversion: {type(user_input)}")


# Problem 9. Store your name, your age, and whether you are a student (True/False) in three variables, then print them together in a single sentence.
name = "Akrima"
age = 30
student_status = False
print(f"My name is {name}, I am {age} years old, and current student status is \"{student_status}\".")
print("="*50 + "\n")


# Problem 10. Write a program that takes the length and breadth of a rectangle from the user and prints its area (length × breadth).
length = float(input("Enter Length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print(f"Area of rectangle is \"{area:.2f}\"")
print("="*50 + "\n")


# Problem 11. Ask the user to enter a word or sentence and print its length using len().
user_input = input("Enter a word or sentence: ")
print("Length of user input is: ", len(user_input))
print("="*50 + "\n")


# Problem 12. Ask the user for a string and print it in all UPPERCASE and then in all lowercase.
user_input = input("Enter anything: ")
print(f"Text in UPPERCASE: {user_input.upper()}")
print(f"Text in lowercase: {user_input.lower()}")
print("="*50 + "\n")


# Problem 13. Ask the user for a sentence and print it with every space replaced by an underscore (_).
user_input = input("Enter a sentence: ")
replaced_spaces_input = user_input.replace(" ", "_")
print(f"Sentence with spaces replaced: {replaced_spaces_input}")
print("="*50 + "\n")

# Problem 14. Ask the user for a sentence and check whether it contains the word "python" (it should work whether the user types "Python", "PYTHON", or "python"). Print "Found" or "Not found".
user_input = input("Enter a sentence: ")
if "python" in user_input.lower():
    print("Found")
else:
    print("Not found")
print("="*50 + "\n")


# Problem 15. Ask the user for a string and print: (a) the first character, (b) the last character, and (c) the whole string reversed using slicing.
user_input = input("Enter a string: ")
print(f"(a) First Character: {user_input[0]}")
print(f"(b) Last Character: {user_input[-1]}")
print(f"(c) Reversed sentence: {user_input[::-1]}")
print("="*50 + "\n")

