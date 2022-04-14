class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        assert len(self.data) > 0,"스택이 비었습니다" #참이면 통과 거짓이면 프린트문
        return self.data.pop()

    def read_top(self):
        assert len(self.data) > 0,"스택이 비었습니다"
        top = self.data[-1]
        return 
    
    def is_empty(self):
        return len(self.data) == 0 #리턴타입이

    

    def main():
        stack = Stack()



        stack.push(10)
        stack.push("홍길동")
        stack.push(100)

