def calc_sum(scores):
    total = 0
    for s in scores:
        total += s

    return total

def print_score(subject, scores):
    total = calc_sum(scores)
    print(f"{subject} 총점 : {total}")
    print(f"{subject} 평균 : {total/len(scores):.2f}")


def main():
    eng_scores = [88, 95, 70, 100, 99]
    kor_scores = [98, 56, 30, 63, 77]

    print_score("영어", eng_scores)
    print_score("국어", kor_scores)
    
   

main()