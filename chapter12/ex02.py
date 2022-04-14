import time
import datetime

t = time.time()
now  = time.localtime()

print("%d년 %d월 %d일" %(now.tm_year, now.tm_mon, now.tm_mday ))
print("%d:%d:%d" %(now.tm_hour,now.tm_min, now.tm_sec))

print()
now2 = datetime.datetime.now()
print(now2)
print("%d년 %d월 %d일" %(now2.year, now2.month, now2.day))
print("%d:%d:%d" %(now2.hour, now2.minute, now2.second))