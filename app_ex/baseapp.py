#애플리케이션 : Application
#   데이터 : 앱 이름, 메뉴
#   기능 : 초기화, 메뉴 구성, 종료, 운영
import sys
from menu import Menu

class Application:
    def __init__(self, title):
        self.title = title
        self.menu = Menu()

    def create_menu(self):
        pass

    def init(self):
        self.create_menu()

    def exit(self, func =None):
        answer = input('종료할까요? (y/n) ').lower()
        if answer == 'y':
            #종료전 함수 호출 필요
            if func: # func가 전달 됐으면 실행
                func()
            sys.exit()

    def run(self):
        self.init()
        while True:
            print(f'[{self.title}]')
            self.menu.print()
            item = self.menu.select()

            if item:
                item.run()
            else:
                print("잘못된 메뉴입니다.")
            
            print()
