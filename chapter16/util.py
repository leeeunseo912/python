INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

print('util.py', __name__)

if __name__ == '__main__':
    print(INCH)
    print(calcsum(100))