import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        return [eval(line.strip()) for line in lines]  # Each line is a dictionary

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(str(task) + "\n")

tasks = load_tasks()

def add_task():
    name = input("📝 Enter task description: ").strip()
    if not name:
        print("⚠️ Task description cannot be empty!")
        return
    priority = input("📌 Set priority (Low / Medium / High): ").strip().capitalize()
    if priority not in ["Low", "Medium", "High"]:
        priority = "Low"  # Default priority
    task = {"name": name, "priority": priority, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{name}' added with priority '{priority}'.")

def remove_task():
    show_tasks()
    if not tasks:
        return
    try:
        idx = int(input("🗑️ Enter task number to remove: "))
        removed = tasks.pop(idx - 1)
        save_tasks(tasks)
        print(f"🗑️ Removed task '{removed['name']}'.")
    except (IndexError, ValueError):
        print("❌ Invalid task number.")

def mark_done():
    show_tasks()
    if not tasks:
        return
    try:
        idx = int(input("✔️ Enter task number to mark as done: "))
        tasks[idx - 1]["done"] = True
        save_tasks(tasks)
        print(f"✅ Task '{tasks[idx - 1]['name']}' marked as done!")
    except (IndexError, ValueError):
        print("❌ Invalid task number.")

def search_tasks():
    keyword = input("🔍 Enter keyword to search: ").strip().lower()
    matches = [task for task in tasks if keyword in task['name'].lower()]
    if matches:
        print("\n🔍 Matching Tasks:")
        for i, task in enumerate(matches, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['name']} [{task['priority']}] - {status}")
    else:
        print("❌ No matching tasks found.")

def show_tasks():
    if not tasks:
        print("\n📭 No tasks available.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['name']} [{task['priority']}] - {status}")

def main():
    print("📌 Welcome to the Smart CLI To-Do App with Persistence\n")
    while True:
        print("\nOptions:")
        print("1. ➕ Add Task")
        print("2. 🗑️ Remove Task")
        print("3. 📋 Show Tasks")
        print("4. ✔️ Mark Task as Done")
        print("5. 🔍 Search Task")
        print("6. ❌ Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            search_tasks()
        elif choice == '6':
            print("👋 Exiting To-Do App. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
