salerate = 0.9

def kim():
    print("오늘의 할인율: ", salerate)
    salerate = 2.0
    print("오늘의 할인율: ", salerate)


def lee():
    price = 1000
    print("가격: ", price * salerate)

kim()
salerate = 1.1
lee()