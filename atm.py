""""Build a mini ATM terminal based project
where users can create accounts, check balances, deposit and withdraw using
using object oriented programming
"""

# First step will be to create a user to access the ATM
class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New Balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. New Balance: ${self.balance}"
        elif self.balance < amount:
            return "Insufficient Funds"
        else:
            return "Invalid Withdrawal Amount"

# Second step will be to create an ATM class
class ATM:
    def __init__(self):
        self.accounts = {}

    # Creating an account and linking the user to the account
    def create_account(self, account_number, pin):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, pin)
            return "Account created successfully"
        else:
            return "Account already exists, please choose a different account number"

    # Accessing the created account
    def access_account(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number].pin == pin:
            return self.accounts[account_number]
        else:
            return None

def main():
    atm = ATM()

    while True:
        print("\nATM Menu")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter your Account Number: ")
            pin = input("Enter your PIN: ")
            result = atm.create_account(account_number, pin)
            print(result)
        elif choice == "2":
            account_number = input("Enter your Account Number: ")
            pin = input("Enter your PIN: ")
            account = atm.access_account(account_number, pin)
            if account:
                while True:
                    print("\nAccount Menu")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    account_choice = input("Enter your choice: ")

                    if account_choice == "1":
                        balance = account.check_balance()
                        print(f"Your balance: ${balance}")
                    elif account_choice == "2":
                        amount = float(input("Enter the deposit amount: "))
                        result = account.deposit(amount)
                        print(result)
                    elif account_choice == "3":
                        amount = float(input("Enter the withdrawal amount: "))
                        result = account.withdraw(amount)
                        print(result)
                    elif account_choice == "4":
                        break
                    else:
                        print("Invalid Choice")
            else:
                print("Invalid account number or pin")
        elif choice == "3":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice, Please select a valid option")

if __name__ == "__main__":
    main()

                
                    
                    
                    
                    
                