dates = ["월","화","수","목","금","토","일"]
food = ["갈비탕","순대국","칼국수","삼겹살"]

menu = zip(dates,food)

for d, f in menu:
    print("%s요일 메뉴: %s" %(d,f))