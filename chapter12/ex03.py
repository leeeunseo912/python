from time_util import get_time_filename
import time

def capture(seq=1):
    file_name = get_time_filename('jpg',seq)

    return file_name


def main():
   for ix in range(5):
       file_name = capture(ix+1)
       print(file_name)
       time.sleep(0.2)

main()