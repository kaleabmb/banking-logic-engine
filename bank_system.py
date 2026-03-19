account = {"balance": 0, "history": []}

def deposit(amount):
    if amount > 0:
        account["balance"] += amount
        account["history"].append(f"Deposited {amount}")
        print("Success.")
    else:
        print("Invalid amount.")

def withdraw(amount):
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        account["history"].append(f"Withdrew {amount}")
        print("Success.")
    else:
        print("Insufficient funds or invalid amount.")

while True:
    print(f"\nBalance: {account['balance']}")
    action = input("1. Deposit, 2. Withdraw, 3. History, 4. Exit: ")
    if action == "1":
        try:
            val = float(input("Amount: "))
            deposit(val)
        except ValueError:
            print("Please enter a valid number.")
    elif action == "2":
        try:
            val = float(input("Amount: "))
            withdraw(val)
        except ValueError:
            print("Please enter a valid number.")
    elif action == "3":
        print("\n--- Transaction History ---")
        for item in account["history"]:
            print(item)
    elif action == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")