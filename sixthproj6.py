# Define the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        # Initialize the account with an account number and a starting balance
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Add the deposit amount to the balance
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtract the withdrawal amount from the balance if funds are sufficient
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Return the current balance
        print(f"Your current balance is: ${self.balance:.2f}")

# Create an instance of BankAccount
user_account = BankAccount(account_number="123456")

# Start an indefinite loop for user interactions
while True:
    print("\nWelcome to the Bank Account Management System!")
    account_input = input("Please enter your account number (or type 'exit' to quit): ").strip()

    # Exit condition for the loop
    if account_input.lower() == 'exit':
        print("Thank you for using the Bank Account Management System. Goodbye!")
        break

    # Check if the account number matches the user's account
    if account_input == user_account.account_number:
        print("\nChoose an option:")
        print("a) Deposit money")
        print("b) Withdraw money")
        print("c) Check balance")
        print("d) Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "a":
            # Prompt for deposit amount and call the deposit method
            amount = float(input("Enter the amount to deposit: "))
            user_account.deposit(amount)
        elif choice == "b":
            # Prompt for withdrawal amount and call the withdraw method
            amount = float(input("Enter the amount to withdraw: "))
            user_account.withdraw(amount)
        elif choice == "c":
            # Call the check_balance method to display the current balance
            user_account.check_balance()
        elif choice == "d":
            print("Logging out of your account.")
            continue
        else:
            print("Invalid option. Please try again.")
    else:
        print("Incorrect account number. Please try again.")