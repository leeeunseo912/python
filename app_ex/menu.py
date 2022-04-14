#메뉴 개념  --> 클래스로 표현

#메뉴 하나
#   MenuItem
#       데이터 : 타이틀, 메뉴 함수에 대한 참조
#       기능 : 메뉴 함수 실행

class MenuItem:
    def __init__(self, title, func):
        self.title = title
        self.func = func

    def run(self):
        self.func()


# def print_list():
#     print('print_list 실행')

# def main():
#     item = MenuItem("목록", print_list)
#     item.run()
# main()

#메뉴 만들기
#   데이터 : MenuItem의 콜렉션 --> 사전
#   기능 : 선택, 메뉴 보여주기, 메뉴 추가

class Menu:
    def __init__(self):
        self.menus = {}

    def add_menu(self, title, func):
        item = MenuItem(title, func)
        self.menus[title] = item

    def print(self):
        titles = self.menus.keys()
        print("="*50)
        print(' '.join(titles))
        print("="*50)
    
    def select(self):
        choice = input('선택> ')
        item = self.menus.get(choice)
        return item

if __name__== '__main__':
    #Menulist 실행
    def print_list():
        print('print_list 실행')

# def play():
#     print('play 실행')

# def exit():
#     print('종료')

# menu = Menu()
# menu.add_menu('목록',print_list)
# menu.add_menu('재생', play)
# menu.add_menu('종료',exit)

# menu.print()
# item = menu.select()
# item.run()