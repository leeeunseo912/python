import time

def gettime():
    now = time.localtime()
    print(now)
    return now.tm_hour, now.tm_min

def main():
        
    result = gettime()
    print(result)
    print(f"지금은 {result[0]}시 {result[1]}분 입니다.")

    hour, minute = gettime()

    print(f"지금은 {hour}시 {minute}분 입니다.")

main()