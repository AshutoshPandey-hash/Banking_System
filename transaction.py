import os

BALANCE_FILE = "bank_balance.txt"

def read_balance():
    if not os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'w') as f:
            f.write("900")
    with open(BALANCE_FILE, 'r') as f:
        return float(f.read().strip())

def write_balance(balance):
    with open(BALANCE_FILE, 'w') as f:
        f.write(str(balance))

bank_balance = read_balance()
transaction_history = []

def show_menu():
    print("\n=== Banking Menu ===")
    print("1. Show Bank Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")
    print("=====================")

def show_bank_balance():
    print(f"Your current bank balance is: ₹{bank_balance:.2f}")

def deposit():
    global bank_balance
    while True:
        try:
            amount = float(input("Enter the amount you want to deposit ₹"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            bank_balance += amount
            write_balance(bank_balance)
            transaction_history.append(f"Deposited: ₹{amount:.2f}. New Balance: ₹{bank_balance:.2f}")
            print(f"Deposited: ₹{amount:.2f}. New Balance: ₹{bank_balance:.2f}")
            break
        except ValueError:
            print("Please enter a valid amount.")

def withdrawal():
    global bank_balance
    while True:
        try:
            amount = float(input("Enter the amount you want to withdraw ₹"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            if amount > bank_balance:
                print("Insufficient Funds!")
                break
            bank_balance -= amount
            write_balance(bank_balance)
            transaction_history.append(f"Withdrew: ₹{amount:.2f}. New Balance: ₹{bank_balance:.2f}")
            print(f"Withdrew: ₹{amount:.2f}. New Balance: ₹{bank_balance:.2f}")
            break
        except ValueError:
            print("Please enter a valid amount.")

def show_transaction_history():
    if not transaction_history:
        print("\nNo Transaction History.")
    else:
        print("\n=== Transaction History ===")
        for i, transaction in enumerate(transaction_history, 1):
            print(f"{i}. {transaction}")
        print("===========================")

while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    if choice == "1":
        show_bank_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdrawal()
    elif choice == "4":
        show_transaction_history()
    elif choice == "5":
        print("HAVE A GREAT DAY!")
        break
    else:
        print("Please choose a valid option.")
