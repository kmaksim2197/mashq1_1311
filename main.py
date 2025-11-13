class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_customer_name(self):
        return self.__customer_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False


class PremiumAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, discount_rate=0.1):
        super().__init__(account_number, customer_name, balance)
        self.__discount_rate = discount_rate

    def get_discount_rate(self):
        return self.__discount_rate

    def withdraw(self, amount):
        if amount <= 0:
            return False
        discounted_amount = amount * (1 - self.__discount_rate)
        if super().get_balance() >= discounted_amount:
            super()._BankAccount__balance -= discounted_amount
            return True
        return False
