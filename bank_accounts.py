class BalanceException(Exception):
    ...
    
class BankAccount:
    def __init__(self, initialAmount, accountName):
        self._balance = initialAmount
        self.title = accountName
        print(f"\nInitial Balance: ${self._balance:.2f}")
        
    @property
    def balance(self):
        return f"\nCurrent Balance: ${self._balance:.2f}"
    
    # def __str__(self):
    #     return f"!\nAccount:{self.title}\nBalance: ${self._balance:.2f}"
    
    def deposit(self, amount):
        try:
            self._is_valid_deposit_amount(amount)
            self._balance += amount
            print(f"\nDeposit ${amount}...")
            return self.balance
        except BalanceException as error:
            print (f"\nTransaction interrupted: {error}")
                        
    def _is_valid_withdraw_amount(self, amount):
        if self._balance >= amount:
            return 
        else:
            raise BalanceException(f"\nCannot withdraw '${amount}'!${self._balance} available..")
        
    def _is_valid_deposit_amount(self, amount):
        if amount > 0:
            return 
        else:
            raise BalanceException(f"\nInvalid deposit amount!..")

        
    def withdraw(self, amount):
        try:
            self._is_valid_withdraw_amount(amount)
            self._balance -= amount
            print(f"\nWithdraw ${amount}...\n{self.balance}")
        except BalanceException as error:
            print (f"\nWithdraw interrupted: {error}")
