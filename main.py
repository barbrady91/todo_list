class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.completed = False
    
    def __str__(self):
        return f"ID: {self.task_id}, Description: {self.description}, Completed: {self.completed}"

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
    
    def view_tasks(self):
        for task in self.tasks:
            print(task)
    
    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                break
    
    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                break

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
            print("Task added successfully.")
        
        elif choice == '2':
            pass
        
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo_list.mark_task_completed(task_id)
                print("Task marked as completed.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to remove: "))
                todo_list.remove_task(task_id)
                print("Task removed successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
