score = [88,95,70,100,99]

no = 1
for s in score:
    print(str(no) + "번 학생의 성적 : ", s)
    no += 1
    
for no, s in enumerate(score,1):
    print(str(no)+ "번 학생의 성적 : ", s)