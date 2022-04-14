#페이지네이션 정보를 가지는 클래서 : Paginator
#   데이터 : 페이지에 담길 데이터, 페이지번호, 전체 데이터건수
import math

class Paginator:
    def __init__(self, data, page_num, counter_per_page):
        self.total_count = len(data)
        self.page_num = page_num
        self.total_page = math.ceil(self.total_count/counter_per_page)
        self.start = (page_num-1)*counter_per_page
        self.end = self.start + counter_per_page
        self.page = data[self.start:self.end]