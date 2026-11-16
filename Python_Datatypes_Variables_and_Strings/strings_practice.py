# Q1. Import the math module and print the square root of 256 and the value of pi (π) using the module.
import math
sqrt_value = math.sqrt(256)
pi_value = math.pi
print("Square root of 256:", sqrt_value)
print("Value of Pi (π):", pi_value)
print("="*50 + "\n")

# Q2. Import the random module and write a program that prints a random number between 1 and 100 (both included).
import random
random_num = random.randint(1, 100)
print(f"Random number between 1 & 100: {random_num}")
print("="*50 + "\n")

# Q3. Write a program that prints "Hello" to the screen, and add a single-line comment and a multi-line comment explaining what your program does.
print("Hello")  # This line prints "Hello" to the screen
"""
This program prints "Hello" to the screen.
It also demonstrates the use of single-line and multi-line comments.
"""
print("="*50 + "\n")

# Q4. Use pip to install the pyjokes module, then write a program that imports it and prints one joke.
import pyjokes
joke = pyjokes.get_joke()
print(f"Here's a joke for you: \"{joke}\"")
print("="*50 + "\n")
