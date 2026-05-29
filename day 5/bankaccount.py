
from typing import ClassVar

class BankAccount:
    """
        balance management
        checks if balance >= 0 all the time
    """

    # class variables (similar to static variables in Java etc.
    # Are shared across all instances)
    INTEREST_RATE: ClassVar[float] = 0.035
    _NEXT_ID: ClassVar[int] = 1000

    # python in-built constructor for classes
    def __init__(self, owner: str, initial_bal: float = 0.0):
        if initial_bal < 0:
            print('Balance cannot be negative')
        else:
            # instance variables
            self.owner = owner
            self._balance = float(initial_bal)
            self.__id = BankAccount._NEXT_ID

        BankAccount._NEXT_ID += 1
        self._transactions: list[dict] = []

    @property
    def balance(self) -> float:
        """
            retrieve the balance
        """
        return self._balance

    @property
    def account_id(self) -> int:
        return self.__id
    
    # instance methods
    def deposit(self, amount: float, memo: str ='') -> None:
        if amount <= 0:
            print("Deposit amount must be greater than zero")
        elif BankAccount.validate_amount(amount):
            self._balance += amount
            self._transactions.append({'type': 'deposit', 'amount': amount, 'memo': memo})
        else:
            print("Amount should be a number and greater than zero")

    def withdraw(self, amount: float, memo: str = '') -> None:
        if amount <= 0:
            print("Withdrwal amount must be greater than zero")
        elif amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            self._transactions.append({'type': 'withdrawal', 'amount': amount, 'memo': memo})

    def get_account_statement(self) -> str:
        statement =  [f'Account #{self.__id} - {self.owner}', f'Balance: Rs.{self._balance:,.2f}']
        
        for t in self._transactions:
            sign = '+' if t['type'] == 'deposit' else '-'
            statement.append(f' {sign}Rs.{t['amount']:>10,.2f} {t['memo']}')
        
        return '\n'.join(statement)
    
    @classmethod
    def set_interest_rate(cls, rate:float)-> None:
        if 0 < rate < 1:
            print("Interest rate must be between 0 and 1")
        else:
            cls.INTEREST_RATE = rate

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0




acc1 = BankAccount('Prithvi', 12000)
print('Initial Balance: ', acc1.balance)
acc1.deposit(-1)
print('Current Balance: ', acc1.balance)
# acc1.withdraw(40000)
