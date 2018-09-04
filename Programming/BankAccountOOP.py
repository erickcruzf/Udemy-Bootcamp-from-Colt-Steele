#First exercise on OOP
class BankAccount:
    
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, number):
        self.balance += number
        return self.balance
        
    def withdraw(self, number):
        self.balance -= number
        return self.balance
    
    def getbalance(self):
        return self.balance
