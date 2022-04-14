import time
from datetime import datetime


def get_time_filename(ext,seq=1):
    now = datetime.now()
    file_name = f'{now.year}{now.month}{now.day}-{now.hour:02}{now.minute:02}{now.second:02}{seq:03}.{ext}'
    return file_name

def get_elapse_time(func):
    start = time.time()
    #work1()
    func() #매개변수로 전달된 함수를 호출
    end = time.time()
    return end-start 