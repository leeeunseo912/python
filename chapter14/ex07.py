def main():
    datas = [12,34,56,78,90]

    content = []
    
    for n in datas:
        content.append(str(n))
    print(content)

    content = [str(n) for n in datas]
    print(content)

    content = list(map(str, datas))
    print(content)

    content = ','.join(content)
    print(content)

    try:
        with open("data.txt","wt") as file:
            file.write(content)

    except Exception as e:
        print(e)


main()