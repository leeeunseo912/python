#필요한 클래스
#   NameCard : 데이터 클래서(모델 클래스)
#       name, phone, email, address
#       __repr__(), __str__() 정의
#   NameCardBook : NameCard 모델의 컬렉션 클래서
#   Application 운영 클래스
#       데이터 : 앱타이틀, NameCardBook, 파일명
#       기능 : 초기화, 목록, 추가, 수정, 삭제, 검색, 종료

from baseapp import Application
from namecard import NameCardBook

class NameCardBookApp(Application):
    def __init__(self) -> None:
        super().__init__("명함관리앱")
        self.book = NameCardBook()
        self.FILE_PATH = "book.dat"

    def init(self):
        super().init()
        #book.dat를 로딩
        self.book.load(self.FILE_PATH)
        #print(self.book.book)

    def print_card_list(self, card_list, start=0):
        print("-"*40)
        for ix, card in enumerate(card_list, start=0):
            print(f'{ix:3}  {card["name"]}  {card["phone"]}')
        print("-"*40)
    
    def print(self):
        #페이지 단위로 출력
        while True:
            page_num = int(input('페이지번호: '))
            if page_num == -1:
                break # or return

            page_obj = self.book.get_page(page_num)

            self.print_card_list(page_obj.page, page_obj.start)
            print(f'[{page_obj.page_num}/{page_obj.total_page}] 총{page_obj.total_count}건')
        


    def add(self):
        name = input('이름 : ')
        phone = input('전화번호 : ')
        email = input('email : ')
        address = input('주소 : ')
        self.book.add(name, phone, email, address)
    
    def get_field(self, card, key, title):
        value = input(f'{title} ({card[key]}): ')a
        if value =='':
            value = card[key]
        return value

    def update(self):
        name = input("수정할 이름: ")
        ix = self.book.find(name)
        if ix != -1:
            card = self.book.get(ix)
            name = self.get_field(card,'name','이름')
            phone = self.get_field(card, 'phone', '전화번호')
            email = self.get_field(card,'email','email')
            address = self.get_field(card, 'address', '주소')
            self.book.update(ix,name, phone, email, address)
        else:
            print(f'{name}은/는 없는 이름입니다.')

    def search(self):
        name = input('검색 이름: ')
        result = self.book.search(name)
        self.print_card_list(result)
        print(f'총 {len(result)}건')
    
    def remove(self):
        pass

    def exit(self):
        super().exit(lambda: self.book.save(self.FILE_PATH))

    def create_menu(self):
        self.menu.add_menu("목록", self.print)
        self.menu.add_menu("추가", self.add)
        self.menu.add_menu("수정", self.update)
        self.menu.add_menu("검색", self.search)
        self.menu.add_menu("삭제", self.remove)
        self.menu.add_menu("종료", self.exit)

def main():
    app = NameCardBookApp()
    app.run()

main()