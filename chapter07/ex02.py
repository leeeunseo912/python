def calcchange(begin,end):
    total = 0
    for num in range(begin, end+1):
        total += num
    return total

print("3 ~ 7ė íŠė ", calcchange(3,7))
