#다른 디렉토리에 접근하는 방법

f = open("live.txt","rt",encoding="utf-8")

rows = f.readlines()

print(rows)

for r in rows:
    print(r,end="")

f.close()