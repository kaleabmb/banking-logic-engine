import json
import os

class Task:
    def __init__(self, description, is_completed=False):
        self.description = description
        self.is_completed = is_completed

    def mark_done(self):
        self.is_completed = True

    def to_dict(self):
        # Convert object to a dictionary for JSON saving
        return {
            "description": self.description,
            "is_completed": self.is_completed
        }

    def __str__(self):
        status = "X" if self.is_completed else " "
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self, filename="sprint_data.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as f:
                data_list = json.load(f)
                # Rehydrate: Turn dictionaries back into Task objects
                return [Task(d["description"], d["is_completed"]) for d in data_list]
        except (json.JSONDecodeError, KeyError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            # Serialize: Turn Task objects into dictionaries
            json.dump([t.to_dict() for t in self.tasks], f)

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save_tasks()
            return True
        return False

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            return True
        return False

    def display(self):
        print("\n--- Final Version: Sprint Manager ---")
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")


def main():
    manager = TaskManager()

    while True:
        manager.display()
        print("\n1. Add Task | 2. Done | 3. Delete | 4. Exit")
        cmd = input("> ")

        if cmd == "1":
            desc = input("Describe task: ")
            manager.add_task(desc)
        elif cmd == "2":
            try:
                idx = int(input("Task index: "))
                if not manager.complete_task(idx):
                    print("Invalid index.")
            except ValueError:
                print("Enter a number.")
        elif cmd == "3":
            try:
                idx = int(input("Task index: "))
                if not manager.delete_task(idx):
                    print("Invalid index.")
            except ValueError:
                print("Enter a number.")
        elif cmd == "4":
            break

if __name__ == "__main__":
    main()