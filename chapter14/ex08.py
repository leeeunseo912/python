def main():
    try:
        with open('data.txt','rt') as file:
            content = file.read()
            print(content)

            datas = content.split(',')
            datas = list(map(int,datas))
            print(datas)

    except Exception as e:
            print(e)
main()