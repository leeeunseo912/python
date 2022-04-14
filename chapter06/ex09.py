#유효한 성적의 평균구하기

scores = [92,86,68,-1,56,-30,90,140,90]
total = 0
count = 0

for s in scores:
    if 0 <= s <= 100:
        total += s
        count += 1

avg = total / count

print("평균은 ", round(avg,2), "입니다")
