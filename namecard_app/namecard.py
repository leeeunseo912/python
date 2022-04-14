
# class NameCard:
#     def __init__(self, name, phone, email, address):
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.address = address

#     def __repr__(self):
#         return f'NameCard(name = {self.name})'

#     def __str__(self):
#         return f'NameCard(name = {self.name}, phone = {self.phone}, email = {self.email}, address = {self.address}'

from dataclasses import dataclass
from distutils import file_util
from itertools import count
from pydoc import pager
#from file_util import load, save #pickle로 로드/저장
import file_util
import os
import math
from paging import Paginator


@dataclass
class NameCard:
    name : str
    phone : str = ''
    email : str = ''
    address : str = ''

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)


#NameCardBook 클래스 : SRP
#   NameCard 모델 클래스의 콜렉션 역할
#   데이터 : NameCard 목록(리스트)
#   기능 : 추가, 수정, 삭제, 검색, 로딩, 저장

class NameCardBook:
    def __init__(self):
        self.book = []
    
    def get_page(self, page_num, count_per_page = 10):
        #리턴값 : 해당 페이지의 데이터 목록, 전체 페이지 수를 리턴
        page_obj = Paginator(self.book, page_num, count_per_page)
        return page_obj

        # total_count = len(self.book)
        # total_page = math.ceil(len(total_count)/count_per_page)
        # start = (page_num-1) * count_per_page
        # end = start + count_per_page

        # page = self.book[start:end]
        # return page, total_page, total_count,start



    def add(self, name, phone, email, address):
        card = NameCard(name, phone, email, address)
        self.book.append(card)
        self.book.sort(key=lambda card : card.name)
    
    def update(self):
        pass

    def remove(self, name):
        #ix = self.find(name)
        if ix != -1:
            self.pop(ix)

    def search(self, name): #포함으로 검색, 리스트 리턴
        result = list(filter(lambda card : name in card.name, self.book))
        return result
    
    def find(self,name): #완전 일치 검색, 인덱스 리턴
        for ix, card in enumerate(self.book):
            if card.name == name:
                return ix
        return -1
    
    def load(self, file_path):
        if os.path.exists(file_path):
            self.book = file_util.load(file_path)
        else:
            self.book = []

    
    def save(self, file_path):
        file_util.save(file_path, self.book)
        


if __name__ == '__main__':
    import random

    card = NameCard('홍길동', '010-7766-1247','hong@naver.com','서울시')
    print(card)
    print([card])

    book = NameCardBook()

    print('추가 테스트')
    book.add('홍길동2','010-7766-1247','hong2@naver.com','서울시')
    book.add('홍길동1','010-7766-1247','hong1@naver.com','서울시')
    print(book.book)

    print('검색 테스트')
    result = book.search('길동')
    print(result)
    result = book.search('동1')
    print(result)

    print('find 검색 테스트')
    ix = book.find('홍길동2')
    print(ix)
    ix = book.find('홍길동3')
    print(ix)

    print('삭제 테스트')
    book.remove(0)
    print(book.book)

    print('저장 테스트')
    book.save('book.dat')

    print('로딩 테스트')
    book.load('test.dat')
    print(book.book)
    book.load('book.dat')
    print(book.book)

    # book.book = []
    # addresses = ['서울','부산','대구','광주','인천','성남']

    # for i in range(1, 101):
    #     address = random.choice(addresses)
    #     book.add(f'홍길동{i:03}', f'010-1111-{i:04}', f'hong{i:03}@gmail.com', address)

    # print(book.book)
    # book.save('book.dat')