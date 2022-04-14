#명함 관리 프로그램
#관리할 명함 정보 : 이름, 전화번호, email, 주소
import sys
import random
from file_util import load, load_json, save_json

books = [ ]
FILE_NAME = 'book.json'

def create_card(name, phone, email, address):
    return {
        "name" : name,
        "phone" : phone,
        "email":  email,
        "address" : address
    }

def init(): #초기화 함수(예제데이터 생성하기)
    # for i in range(1,101):
    #     card = create_card(f'홍길동{i:03}',f'010-1111-{i:04}',f'hong{i:03}@google.com','서울시')
    #     books.append(card)
    
    # random.shuffle(books)
    # books.sort(key = lambda card: card["name"])

    #json파일에 있는거 복원하기
    global books
    books = load_json(FILE_NAME)

def print_menu():
    print()
    print("="*75)
    print("1.목록보기\t2.목록검색\t3.추가하기\t4.수정하기\t5.삭제하기\t6.종료하기")
    print("="*75)

def print_card_list(card_list):
    print('-'*75)
    for ix, card in enumerate(card_list):
        print(f'{ix:3} {card["name"]} {card["phone"]}')

    print('-'*75)
    print(f'총 : {len(card_list)}명')
    print()


def print_list():
    print("리스트보기")
    print_card_list(books)


def search():
    print("리스트 검색")
    keyword = input("검색 이름: ")
    # result = []
    # for card in books:
    #     if keyword in card['name']:
    #         result.append(card)

    #람다함수를 이요한 filter
    result = list(filter(lambda card: keyword in card['name'],books))
    print_card_list(result)
    

def exit():
    answer = input("종료할까요? (y/n) or (Y/N) ")
    if answer == 'Y' or answer == 'y':
        save_json(FILE_NAME,books)
        sys.exit(0)

def add_card():
    name = input("이름: ")
    phone = input("전화번호: ")
    email = input("email: ")
    address = input("주소: ")

    card = create_card(name, phone, email, address)
    books.append(card)
    books.sort(key = lambda card: card["name"])

def find_by_name(name):
    for ix, card in enumerate(books):
        if card['name'] == name:
            return ix

    return -1


def delete_card():
    name = input("삭제할 이름: ")
    ix = find_by_name(name)
    if ix != -1:
        books.pop(ix)
        print(f'{name} 삭제 성공!')
    else:
        print(f'{name} 항목이 없습니다.')
        
def update_card():
    name = input("수정할 이름: ")
    ix = find_by_name(name)
    if ix != -1:
        card = books[ix] #card가 원본에 대한 참조변수라서 업데이트가 되는 것
        name = input(f'이름({card["name"]}) : ')
        if name != '':
            card['name'] = name
        
        phone = input(f'전화번호({card["name"]}) : ')
        if phone != '':
            card['phone'] = phone

        email = input(f'email({card["email"]}) : ')
        if email != '':
            card['email'] = email

        address = input(f'주소({card["address"]}) : ')
        if address != '':
            card['address'] = address
            
        print(f'{name} 항목을 수정했습니다.')
        
    else:
        print(f'{name} 항목이 없습니다.')
    

def main():
    init()
    while True:
        print_menu()
        menu_item = int(input('선택> '))

        if menu_item == 1:
            print_list()
        elif menu_item == 2:
            search()
        elif menu_item == 3:
            add_card()
        elif menu_item == 4:
            update_card()
        elif menu_item ==5:
            delete_card()
        elif menu_item == 6:
            exit()
        else:
            print("잘못 입력한 메뉴입니다. 다시 입력해 주세요.")

main()
