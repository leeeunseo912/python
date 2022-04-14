def flunk(s):
    return s < 60

def high_score(s):
    return s >= 90

def main():
    scores = [45,89,78,55,60,90,94]
    for s in filter(flunk, scores):
        print(s)

    for s in filter(high_score,scores):
        print(s)

    print()
    result = []
    for s in scores:
        if s <= 60:
            result.append(s)
            
    print(result)

main()