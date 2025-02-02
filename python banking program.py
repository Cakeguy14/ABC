#todo python banking program


# todo 1.def func
# todo 2.give rules
# todo 3.def main func
# todo 4.print testing

def show_balance(balance):
    print(f"Your balance is: ${balance}")

def deposit(balance):
    amount = float(input("Deposit amount: "))
    if amount < 0:
        print("Invalid deposit amount. Please enter a positive amount.")
        return deposit()
    else:
        return amount

def withdraw(balance):
    amount = float(input("Withdraw amount: "))
    if amount < 0:
        print("Invalid withdraw amount. Please enter a positive amount.")
        return withdraw(balance)
    elif amount > balance:
        print("Insufficient funds. Please enter a valid amount.")
        return withdraw(balance)
    else:
        return amount


def main():
    balance = 0
    is_running = True
    while is_running:
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice. Please try again.")
    print("Thank you for using the banking app!")
if __name__ == "__main__":
    main()


