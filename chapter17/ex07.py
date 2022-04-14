from dataclasses import dataclass
import time

def outer(func):
    def wrapper():
        print("-"*30)
        func()
        print("-"*30)
    return wrapper

def elapse(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__} 함수 실행 시간 : {end - start}')
    return wrapper

@elapse
@outer
# inner = elapse(outer(inner))
def inner():
    print("결과를 출력합니다.")

@dataclass
class NameCard:
    name : str
    phone : str = ' '

def main():
    inner()

main()