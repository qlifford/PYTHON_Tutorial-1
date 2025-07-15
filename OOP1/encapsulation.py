class BankAccount:
    def __init__(self):
        self._balance = 00.0
        
    @property
    def balance(self):
        return f"Balance: {self._balance}"
        
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
        else:
            print("Deposit amount must be a positive value")

    def withdraw(self, amount):  
        if amount < 0:
            print("Withdraw amount must be a positive value")            
        elif self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError ("Insufficient funds")
        
    def _is_valid_amount(self, amount):
        return amount > 0
        
if __name__ == '__main__':   
    account1 = BankAccount()
    print(account1.balance)
    account1.deposit(200)
    print(account1.balance)
    account1.withdraw(100)
    print(account1.balance)
    account1.withdraw(-10)
    print(account1.balance)