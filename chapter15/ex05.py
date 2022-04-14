#Queue ==> FIFO
#   클래스 설계
#       클래스명 : Queue
#           데어터 : 리스트
#           기능 : 추가, 꺼내기, 꺼내지 않고 읽기, 비었는지 검사


class Queue:
    
    def __init__(self):
        self.data = []

    def put(self,value):
        self.data.append(value)

    def get(self):
        assert not self.is_empty() , '큐가 비었습니다.'
        return self.data.pop(0)

    def read_front(self):
        assert not self.is_empty()  , '큐가 비었습니다.'
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

def main():
    q = Queue()

    q.put(1)
    q.put(10)
    q.put(100)

    print(q.get())
    print(q.get())
    print(q.get())

    if(not q.is_empty()):
        print(q.get())
main()
