names = ['홍길동', '고길동', '둘리', '또치']

search_name = input("이름을 입력하시오: ")
search_result = False
count = 0

for name in names:
    if search_name == name:
        search_result = True
        break
    count += 1

if search_result:
    print(search_name, "은 리스트", count+1, "번째에 있습니다.")
else:
    print(search_name,"은 리스트 안에 없습니다.")
