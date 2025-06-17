print("=== Personal Finance Tracker ===")
print("1. Add Transaction")
print("2. View Transactions")
print("3. Summary")
print("4. Exit")

transactions_expenses = []
transaction_category = []
transaction_description = []
income = []
expenses = []

def add_transaction():
    print("\n*** Add Transaction ***")
    input_transaction = input("Income or Expense? (i/e): ").lower()
    
    category = input("Enter Category: ")
    desc = input("Enter Description: ")

    if input_transaction.startswith('i'):
        try:
            amount = float(input("Enter Total Income: "))
            income.append(amount)
            print("Income added successfully!")
        except ValueError:
            print("Invalid amount for income.")
            return

    elif input_transaction.startswith('e'):
        try:
            amount = float(input("Enter Expense Amount: "))
            expenses.append(amount)
            transactions_expenses.append(amount)
            transaction_category.append(category)
            transaction_description.append(desc)
            print("Expense Transaction Added Successfully!!")
        except ValueError:
            print("Invalid amount for expense.")
            return
    else:
        print("Please enter 'i' or 'e'.")
        return

def view_transaction():
    print("\n*** View Transactions ***")
    if not transactions_expenses:
        print("No expense transactions recorded yet.")
        return
    for i in range(len(transactions_expenses)):
        print(f"\nTransaction {i + 1}")
        print(f"Amount: {transactions_expenses[i]}")
        print(f"Category: {transaction_category[i]}")
        print(f"Description: {transaction_description[i]}")

def summary_transaction():
    print("\n*** Summary ***")
    total_income = sum(income)
    total_expenses = sum(expenses)
    balance = total_income - total_expenses

    print(f"Total Income: ₹{total_income}")
    print(f"Total Expenses: ₹{total_expenses}")
    print(f"Balance: ₹{balance}")

while True:
    try:
        num = int(input("\nChoice (1-4): "))
    except ValueError:
        print("Please enter a valid number (1-4).")
        continue

    if num == 1:
        add_transaction()
    elif num == 2:
        view_transaction()
    elif num == 3:
        summary_transaction()
    elif num == 4:
        print("GoodBye!!")
        break
    else:
        print("Invalid choice. Please select 1 to 4.")

    again = input("\nDo you want to perform another action? (y/n): ").lower()
    if not again.startswith('y'):
        print("Thanks for using the Personal Finance Tracker!")
        break
