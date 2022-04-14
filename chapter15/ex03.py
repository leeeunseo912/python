class NameCard:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return f'<NameCard : name = {self.name}, phone = {self.phone} >'

    def __repr__(self):
        return f'NameCard : name : {self.name}'

def main():

    # people1 = NameCard("이은서","010-7766-1247","evestar98@naver.com","성남시")
    # people2 = NameCard("이효령","010-7766-1630","hyo@naver.com","서울시")
    # print(people1.name,people1.phone,people1.email,people1.address)
    # print(people1)
    
    # print(people2.name,people2.phone,people2.email,people2.address)
    # print(people2)

    book = []
    for i in range(100):
        card = NameCard(f'홍길동{i:03}', f'010-1111-{i:04}',f'hong{i:03}@google.com','서울시')
        book.append(card)
    print(book)
    

main()