def calcsum(n):
    def add(a,b):
        return a + b

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total

print("~ 10 = ", calcsum(10))

# def calc(op, a, b):
#     op(a,b)

# def add(a,b):
#     print(a+b)

# def multi(a,b):
#     print(a*b)

# calc(add, 1,2)
# calc(multi, 3, 4)