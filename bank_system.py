import json
import os

# The file where we will store our data
DATA_FILE = "bank_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"balance": 0, "history": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

account = load_data()

def deposit(amount):
    if amount > 0:
        account["balance"] += amount
        account["history"].append(f"Deposited {amount}")
        save_data(account)
        print("Success.")
    else:
        print("Invalid amount.")

def withdraw(amount):
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        account["history"].append(f"Withdrew {amount}")
        save_data(account)
        print("Success.")
    else:
        print("Insufficient funds.")

while True:
    print(f"\nSaved Balance: {account['balance']}")
    action = input("1. Deposit, 2. Withdraw, 3. History, 4. Exit: ")
    
    if action == "1":
        try:
            val = float(input("Amount: "))
            deposit(val)
        except ValueError:
            print("Enter a number.")
    elif action == "2":
        try:
            val = float(input("Amount: "))
            withdraw(val)
        except ValueError:
            print("Enter a number.")
    elif action == "3":
        for entry in account["history"]:
            print(entry)
    elif action == "4":
        break