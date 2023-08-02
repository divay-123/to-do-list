class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False
class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, 1):
                status = "✓" if task.is_completed else " "
                print(f"{index}. [{status}] {task.description}")

    def mark_completed(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task.is_completed = True
            print(f"Task '{task.description}' marked as completed.")
        except IndexError:
            print("Invalid task index!")

    def run(self):
        print("Welcome to the To-Do List App!")
        while True:
            print("\nOptions:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as completed")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_index = int(input("Enter the task index to mark as completed: "))
                self.mark_completed(task_index)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
