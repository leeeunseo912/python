score = [50,34,78,90,35,100]
total = 0
max_score = -1

for s in score:
    if s > max_score:
        max_score = s


print("최대 성적은 ", max_score, "입니다")