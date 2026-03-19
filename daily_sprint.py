class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def mark_done(self):
        self.is_completed = True

    def __str__(self):
        # Displays [v] if done, [ ] if not done
        status = "v" if self.is_completed else " "
        return f"[{status}] {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks =[]

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print("Task added.")

    def display_all(self):
        print("\n--- Daily Sprint ---")
        if not self.tasks:
            print("No tasks currently scheduled.")
            return
            
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print("Task marked as complete.")
        else:
            print("Error: Invalid task number.")


def main():
    sprint = TaskManager()

    while True:
        sprint.display_all()
        print("\nOptions: 1. Add Task  2. Complete Task  3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Task description: ")
            sprint.add_task(desc)
        elif choice == "2":
            try:
                task_num = int(input("Enter task number to mark done: "))
                sprint.complete_task(task_num)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "3":
            print("Exiting sprint manager...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()