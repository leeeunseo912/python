from namecard import NameCardBook
import random



def main():
    book = NameCardBook()

    #200개의 데이터를 구성해서 book.dat로 저장
    book.book = []
    addresses = ['서울','부산','대구','광주','인천','성남']

    for i in range(1, 101):
        address = random.choice(addresses)
        book.add(f'홍길동{i:03}', f'010-1111-{i:04}', f'hong{i:03}@gmail.com', address)

    print(book.book)
    book.save('book.dat')

    #book.book을 orderby 변수의 값을 기준으로 정렬하세요
    orderby = 'address'
    book.book.sort(key = lambda card : card[orderby])
    print(book.book)

    orderby = 'name'
    book.book.sort(key = lambda card : card[orderby])
    print(book.book)

main()