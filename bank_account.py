class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = float(account_balance)
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.account_balance


# Create the first account
my_account = Account("1234567890", 50000, "Ayo")

# Perform transactions
my_account.deposit(10000)
my_account.withdraw(20000)

print("Account Holder:", my_account.account_holder)
print("Account Number:", my_account.account_number)
print("Account Balance:", my_account.check_balance())


# Create a second account
account2 = Account("9876543210", 30000, "John")

account2.deposit(5000)
account2.withdraw(10000)

print("\nAccount Holder:", account2.account_holder)
print("Account Number:", account2.account_number)
print("Account Balance:", account2.check_balance())


# Create a third account
account3 = Account("5555555555", 10000, "David")

account3.deposit(2000)
account3.withdraw(15000)  # Insufficient balance

print("\nAccount Holder:", account3.account_holder)
print("Account Number:", account3.account_number)
print("Account Balance:", account3.check_balance())
