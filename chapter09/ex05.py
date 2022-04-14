def main():
    lol = [
        [1,2,3],[4,5],[6,7,8,9]
    ]

    print(lol)
    print(lol[0])
    print(lol[2][1])
    print()

    for sub in lol:
        print(sub)
        for item in sub:
            print(item, end = " ")
        print()

main()