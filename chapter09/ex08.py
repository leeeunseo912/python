def main():
    scores = [70,30,-10,100,160,90]
    
    scores = [n for n in scores if 0<= n <= 100]
    print(scores)
    print(sum(scores))

main()