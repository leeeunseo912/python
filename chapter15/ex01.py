class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def inquire(self):
        print(f"잔액은 {self.balance}원 입니다.")

def main():
        
    account = Account(8000)
    account.deposit(1000)
    account.inquire()

    shihan = Account(8000)
    shihan.deposit(1000)
    shihan.inquire()

    nonghyup = Account(1200000)
    nonghyup.inquire()

main()

