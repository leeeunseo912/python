def total(a,b):
    return a + b

def main():
    scores = [45,89,78,55,60]
    bonus = [2,3,0,0,5]
    for s in map(total, scores, bonus):
        print(s, end = ", ")

main()