# 📝 Python To-Do List / Task Manager

tasks = []


def show_tasks():
    if not tasks:
        print("\n📭 No tasks yet.")
        return

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a new task: ").strip()

    if task:
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"🗑️ Deleted: {removed}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    while True:
        print("\n" + "=" * 35)
        print("📝 PYTHON TO-DO LIST")
        print("=" * 35)

        print("1. ➕ Add Task")
        print("2. 📋 View Tasks")
        print("3. 🗑️ Delete Task")
        print("4. 🚪 Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("\n👋 Goodbye! Keep coding!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()