#Smart ATM System
correct_pin = 1234
balance = 50000
atm_working = True

user_pin = int(input("Enter your PIN: "))
withdraw_amount = 0
acc_type = int(input("Select you Account type:\n1. Savings\n2. Current"))

if atm_working == False:
    print("ATM is not Functional")
else:
    print("ATM is Working...")
    attempt = 0
    max_attempt = 3
    while attempt <= max_attempt:
        if user_pin != correct_pin:
            print("Incorrect PIN.... try Again")
            user_pin = int(input("Enter your correct PIN: "))
            attempt += 1
        else:
            withdraw_amount = int(input("Enter Amount to withdraw: "))
            if withdraw_amount > balance:
                print("Not Enough Balance")
                #withdraw_amount = int(input("Please your Amount to withdraw again: "))
            elif withdraw_amount < 500:
                print("Minimum 500 can be withdraw")
            
            if withdraw_amount <= 20000 and (acc_type == 1 or acc_type == 2):
                balance = balance - withdraw_amount
                print("Transaction Sucessfull!\nNo Tax.")
                print(f"Current Balance Now: {balance}")
            elif withdraw_amount > 20000:
                print("Transacton Sucessfull. Rs 100 deducted as Tax!")
            else:
                print("Something went Wrong!")
            break;
    else:
        print("You are blocked")
            
