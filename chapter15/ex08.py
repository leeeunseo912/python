class Date:
    def __init__(self,month):
        self.inner_month = month

    @property
    def month(self):
        return self.inner_month

    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month

def main():
    today = Date(8)

    today.month = 15
    print(today.month)

    today.month = 10
    print(today.month)

main()