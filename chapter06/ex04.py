start = int(input("시작값을 입력해주세요: "))
end = int(input("종료값을 입력해주세요: "))
total = 0

num =start

while num <= end:
    total += num
    num += 1

print(start," ~ ", end, "까지의 합: ", total)