def main():
    scores = [
            ("홍길동", 90),
            ("고길동",80),
            ("둘리",50),
            ("또치",30)
    ]

    for i in scores:
        print(f"이름: {i[0]}, 점수 : {i[1]}")

    print()
    
    for name, score in scores:
        print(f"이름: {name}, 점수 : {score}")

main()