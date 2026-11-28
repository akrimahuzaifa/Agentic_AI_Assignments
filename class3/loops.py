#print 1 to 100
# for loop, while loop

# for item in range(1, 100):
#     print(item)

# days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# inp = input("Enter a day to find: ")
# #isDayFound = False

# for item in days:
#     if item == inp:
#         print("Day found")
#         #isDayFound = True
#         break;
# else: #for else
#     print("day not found")

# # if isDayFound == False:
# #     print("Day not Found")



#
# mangoes = ["Chausa", "Sindhri", "Kharab", "Langra", "Anwar Ratol"]

# for item in mangoes:
#     if item == "Kharab":
#         print("Kharab Aam")
#         continue

#     print(item, "Amm mil gya h")



# while loop
# count = 1

# while count < 10:
#     print(count)
#     count = count + 1


correct_pin = "1234"
max_attempts = 3
attempt = 0

while attempt < max_attempts:
    pin = input("Enter you pin: ")
    # attempt = attempt + 1
    attempt += 1

    if pin == correct_pin:
        print("Welcome to the ATM")
        break;

    if pin == "":
        print("PIN could not empty")
    
    if pin != correct_pin:
        print("Sorry Incorrect PIN")
else:
    print("You are blocked")

