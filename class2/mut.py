#mutable vs immutable
# mutable = can be changed
# immutable = cannot be changed

# int, float, string, tuple = immutable
# list, dict, set = mutable


f_name = "usama"

print(f_name[0])  

f_name[0] = "O"  # This will raise an error because strings are immutable

print(f_name)  # Output: "usama" (unchanged)