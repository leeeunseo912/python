import time

def inner():
    print("결과를 출력합니다.")

def outer(func):
    print("-"*30)
    func()
    print("-"*30)

def hello():
    print("안녕하세요")

def elapse(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)

def main():
    outer(inner)
    outer(hello)

    elapse(inner)
    elapse(hello)

main()

