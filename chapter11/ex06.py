lambda x : x + 1

def increase(x):
    return x+1

score = [45,89,72,53,98]
for s in filter(lambda x:x<60, score):
    print(s)

print()

for s in filter(lambda x : x>=95,score):
    print(s)