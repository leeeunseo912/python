def calcscore(name, *score, **option):
    print(name)
    print(score)
    print(option)

    total = 0
    for s in score:
        total += s

    print("총점 :", total)

    if option.get('avg'):
        print("평균 :", total/len(score))
    
def main():
    hong_score = [88,99,77]
    go_score = [99,88,95,90]

    calcscore("홍길동", 88, 99, 77, avg=True)
    calcscore("고길동", 99, 88, 95, 85, avg=False)

main()