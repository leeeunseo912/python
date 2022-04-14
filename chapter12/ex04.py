from time_util import get_elapse_time

def work1():
    for i in range(1000):
        print(i)

def work2():
    total = 0
    for i in range(1000):
        total += i
  

def main():
    time = get_elapse_time(work1)
    print(time)

    time = get_elapse_time(work2)
    print(time)


main()
