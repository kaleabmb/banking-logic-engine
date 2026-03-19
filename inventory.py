import json
import os

class Item:
    def __init__(self, item_id, name, price, qty):
        self.item_id = str(item_id)
        self.name = name
        self.price = float(price)
        self.qty = int(qty)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "qty": self.qty
        }

class InventoryManager:
    def __init__(self, file_path="inventory.json"):
        self.file_path = file_path
        self.inventory = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                raw_data = json.load(f)
                # Convert dictionary back into Item objects
                return {sid: Item(sid, **info) for sid, info in raw_data.items()}
        return {}

    def save_data(self):
        # Convert objects back into dictionaries for JSON
        serializable_data = {sid: item.to_dict() for sid, item in self.inventory.items()}
        with open(self.file_path, "w") as f:
            json.dump(serializable_data, f, indent=4)

    def add_item(self, item_id, name, price, qty):
        self.inventory[str(item_id)] = Item(item_id, name, price, qty)
        self.save_data()

    def update_stock(self, item_id, change):
        item = self.inventory.get(str(item_id))
        if item:
            if item.qty + change >= 0:
                item.qty += change
                self.save_data()
                return True
        return False

    def get_total_value(self):
        return sum(item.price * item.qty for item in self.inventory.values())

    def low_stock_report(self, threshold=5):
        return [item.name for item in self.inventory.values() if item.qty <= threshold]

def main():
    manager = InventoryManager()

    while True:
        print(f"\n--- Final Inventory System (Total Value: ${manager.get_total_value()}) ---")
        print("1. List All | 2. Update Stock | 3. New Item | 4. Alerts | 5. Exit")
        choice = input("Select: ")

        if choice == "1":
            for sid, item in manager.inventory.items():
                print(f"[{sid}] {item.name} - ${item.price} (Qty: {item.qty})")
        
        elif choice == "2":
            sid = input("Item ID: ")
            try:
                amt = int(input("Change (e.g., -5 for sale, 10 for restock): "))
                if manager.update_stock(sid, amt):
                    print("Updated successfully.")
                else:
                    print("Error: Invalid ID or insufficient stock.")
            except ValueError:
                print("Enter a valid number.")

        elif choice == "3":
            sid = input("ID: ")
            name = input("Name: ")
            price = input("Price: ")
            qty = input("Qty: ")
            manager.add_item(sid, name, price, qty)
            print("Item added.")

        elif choice == "4":
            low_items = manager.low_stock_report()
            if low_items:
                print("LOW STOCK ALERT:", ", ".join(low_items))
            else:
                print("All stock levels healthy.")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
    