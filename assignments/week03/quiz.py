# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if choice == "1":
            print(f"balance is:{balance}")
        elif choice == "2":
            balance_out = float(input("Enter balance:"))
            if balance_out > balance:
                print("nah i won't")
            else:
                balance = balance - balance_out
                print(f"balance is:{balance}")
        if choice =="3":
            balance_in = float(input("Enter balance:"))
            if balance = balance + balance_in :
                print(f"balance is:{balance}")
        if choice == "4":
            break
        else:
            print("อะไรทำใหม่นะน้อง")
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
