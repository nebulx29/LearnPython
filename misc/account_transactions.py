import time
import datetime_example

class Transaction():
    def __init__(self, text, value, acbalance):
        self.timestamp = time.time()
        self.text = text
        self.value = value
        self.acbalance = acbalance
    def __str__(self):
        return "time=" + self.get_timestamp() + " value=" + str(self.value) + " acbalance=" + str(self.acbalance)
    def get_value(self):
        return self.value
    def get_text(self):
        return self.text
    def get_acbalance(self):
        return self.acbalance
    def get_timestamp(self):
        str_timestamp = datetime_example.datetime_example.fromtimestamp(self.timestamp).strftime('%Y-%m-%d_%H:%M:%S')
        return str_timestamp
        
class Account():
    def __init__(self, owner, name, initial_balance):
        self.owner = owner
        self.name = name
        self.balance = initial_balance
        self.transactions = []
    def __str__(self):
        return "owner=" + self.owner + " name=" + self.name + " balance=" + str(self.balance)
    # withdraw: amount > 0
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(Transaction("DEPOSIT", amount, self.balance))
    # withdraw: amount > 0
    def withdraw(self, amount):  
        self.balance = self.balance - amount
        self.transactions.append(Transaction("WITHDRW", amount, self.balance))
    def list_transactions_as_str_list(self):
        r = []
        for t in self.transactions:
            r.append(str(t))
        return r
    

a = Account("joe", "main", 0)
a.deposit(10)
print(a)
a.deposit(5)
print(a)
a.withdraw(3)
print(a)
a.withdraw(6)
print(a)
print(a.list_transactions_as_str_list())



