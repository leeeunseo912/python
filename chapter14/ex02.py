def main():

    try:
        f = open("live.txt","rt", encoding="utf-8")
        text = f.read()
        lines = text.split("\n")
        print(lines)

        # num = 1
        # for i in lines:
        #     print(num, i)
        #     num+=1

        for ix, line in enumerate(lines, 1):
            print(f"{ix}: {line}")

    except FileNotFoundError:
        print("파일이 없습니다")
    finally:
        f.close()

main()