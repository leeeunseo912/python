class TestApp(Application):
    def create_menu(self):
        self.menu.add_menu('테스트', self.text)
        self.menu.add_menu('종료', self.ext)

    def test():
        print('테스트')