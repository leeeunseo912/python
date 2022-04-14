def calcSum(n):
    total = 0
    for num in range(n+1):
        total += num
    return total

print("1 ~ 4 = ", calcSum(4))
print("1 ~ 10 = ", calcSum(10))