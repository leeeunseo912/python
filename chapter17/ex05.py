def makeHello(message):
    def hello(name):
        print(message + "," + name)
    return hello


def main():
    enghello = makeHello("Good Morning")
    kohello = makeHello("안녕하세요")

    enghello = ("Mr Kim")
    kohello = ("홍길동")

main()