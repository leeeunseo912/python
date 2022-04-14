#온도계 센서
#클래스명 : Temperature
#데이터 : 온도, 기록(온도, 측정시간), 위치, 측정가능 범위
#기능 : 측정하기, 범위 초과시,,,기록 보여주기()
import random
from datetime import datetime
import time

class Temperature():
    
    def __init__(self, location, min_value, max_value):
        self.value = None
        self.records = []
        self.location = location
        self.min_value = min_value
        self.max_value = max_value

    def measure(self):
        self.value = round(random.uniform(self.min_value,self.max_value),2)
        now = datetime.now()

        self.records.append((now, self.value))
        return now, self.value

#히터(보일러)
#클래스 : Hitter
#데이터 : 온도계, 장소, 운영 기준 온도
#동작/기능 : 켜기, 끄기, 운영, 온도 설정

class Hitter:
    def __init__(self, location):
        self.temp = Temperature(location,-5,35)
        self.location = location
        self.criteria = 19
        self.status - False
    
    def turn_on(self):
        self.status = True
        print(f"보일러 켜짐 {self.temp.value}도")

    def turn_off(self):
        self.status = False
        print("보일러 꺼짐 {self.temp.value}도")

    def run(self):
        now, temp = self.temp.measure()
        if temp < self.criteria:
            self.turn_on()
        else:
            self.turn_off()


def main():

    temp = Temperature("안방", -5, 35)
    while True:
        time.sleep(1)
        now, value = temp.measure()
        print(f'온도 : {value} 측정시간 : {now} 측정위치 : {temp.location}')
main()    


