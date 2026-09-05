class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.__account_number = account_number   
        self.__balance = balance                 

   
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
            print("Balance updated successfully")
        else:
            print("Invalid balance amount")

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")



account = BankAccount("Nikitha", 123456789, 10000)

print("Account Holder:", account.account_holder)
print("Account Number:", account.get_account_number())
print("Current Balance:", account.get_balance())


account.set_balance(15000)

print("Updated Balance:", account.get_balance())


account.deposit(5000)
print("Balance after deposit:", account.get_balance())

account.withdraw(3000)
print("Balance after withdrawal:", account.get_balance())