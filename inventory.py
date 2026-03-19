import json
import os

DB_FILE = "inventory_data.json"

def load_inv():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    # Default data if file doesn't exist
    return {
        "101": {"name": "Router", "price": 500, "qty": 10},
        "102": {"name": "Switch", "price": 300, "qty": 5}
    }

def save_inv(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def find_item(inv, item_id):
    return inv.get(item_id)

def sell_item(inv, item_id, amount):
    item = find_item(inv, item_id)
    if not item:
        print("Error: Item ID not found.")
        return False
    
    if item['qty'] < amount:
        print(f"Error: Not enough stock. Only {item['qty']} left.")
        return False
    
    item['qty'] -= amount
    print(f"Sold {amount} {item['name']}(s).")
    return True

def main():
    inventory = load_inv()

    while True:
        print("\n--- Inventory Version 1 ---")
        print("1. View All | 2. Search | 3. Sell | 4. Add/Update | 5. Exit")
        cmd = input("> ")

        if cmd == "1":
            for id, info in inventory.items():
                print(f"ID: {id} | Name: {info['name']} | Price: ${info['price']} | Qty: {info['qty']}")
        
        elif cmd == "2":
            search_id = input("Enter ID: ")
            item = find_item(inventory, search_id)
            if item:
                print(f"Found: {item}")
            else:
                print("Not found.")

        elif cmd == "3":
            sell_id = input("Item ID to sell: ")
            qty_to_sell = int(input("Quantity: "))
            if sell_item(inventory, sell_id, qty_to_sell):
                save_inv(inventory)

        elif cmd == "4":
            new_id = input("Item ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            qty = int(input("Initial Qty: "))
            inventory[new_id] = {"name": name, "price": price, "qty": qty}
            save_inv(inventory)
            print("Inventory updated.")

        elif cmd == "5":
            break

if __name__ == "__main__":
    main()
    