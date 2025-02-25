class BankAccount:
    def __init__(self, account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        if amount < 0:
            self.balance += amount
            print(f"{amount} deposited successfully.New balance: {self.balance}")
    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

#subclass-savingAccount
class SavingsAccount(BankAccount):
    def add_intrest(self, rate):
        if rate < 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Intrest of{interest} added to {rate}%.New balance: {self.balance}")

#creating a savingsaccount object
student_savings = SavingsAccount("<Justin>",20000)

print("intial balance:",)
student_savings.display_balance()

print("Deposit Money:",)
student_savings.deposit(100)

print("Adding intrest:",)
student_savings.add_intrest(5)

print("Final Balance:",)
student_savings.display_balance()





























