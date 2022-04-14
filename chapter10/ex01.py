def main():
    dic = {
        'boy':'소년',
        'school':'학교',
        'book':'책'
    }

    print(dic['boy'])
    print(dic['school'])

    print(dic.keys())
    print(dic.values())
    print(dic.items())

    keylist = dic.keys()
    for key in keylist:
        print(key, dic[key])

main()