# Testing the program to ensure it runs as described

# A program that uses a list (linear data structure) to manage a to-do list

# Step 1: Create a list of tasks
tasks = ["Do homework", "Wash dishes", "Exercise", "Read a book"]

# Step 2: Print all tasks
print("To-Do List:")
for task in tasks:
    print(f"- {task}")

# Step 3: Mark tasks as completed
completed_tasks = []
while tasks:
    task = tasks.pop(0)  # Remove the first task from the list
    print(f"\nCompleting task: {task}")
    completed_tasks.append(task)

# Step 4: Show completed tasks
print("\nAll tasks completed:")
for completed_task in completed_tasks:
    print(f"- {completed_task}")
