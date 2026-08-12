print("=" * 50)
print("          PERSONAL EXPENSE TRACKER")
print("=" * 50)

expenses = []

def add_expense():
    category = input("\nEnter expense category: ")
    
    while True:
        try:
            amount = float(input("Enter amount (₹): "))

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("✅ Expense added successfully!")


def show_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "=" * 50)
    print("              EXPENSE HISTORY")
    print("=" * 50)

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['category']:<20} "
            f"₹{expense['amount']:.2f}"
        )


def show_summary():
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]

    highest_expense = max(expenses, key=lambda x: x["amount"])

    print("\n" + "=" * 50)
    print("              EXPENSE SUMMARY")
    print("=" * 50)

    print(f"Total Expenses : ₹{total:.2f}")
    print(
        f"Highest Expense: ₹{highest_expense['amount']:.2f} "
        f"({highest_expense['category']})"
    )

    print("\nCategory-wise Spending:")

    for category, amount in categories.items():
        print(f"- {category}: ₹{amount:.2f}")


while True:

    print("\n" + "=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")
    print("=" * 50)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        print("\nThank you for using Expense Tracker! 👋")
        break

    else:
        print("\n❌ Invalid choice. Please select 1-4.")