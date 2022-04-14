class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다.")

    def eat(self):
        print("식사를 합시다")

    def __str__(self):
        return f'Human(name = {self.name}, age = {self.age})'

class Student(Human):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        self.stunum = stunum

    def intro(self):
        super().intro() #부모에서 정의한 intro()를 재정의 (overriding)
        print("학번 : " + str(self.stunum))

    def study(self):
        print("하늘 천 따지 검을 현 누를 황")

class Teacher(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def teach(self):
        print("수업을 합니다.")

def main():

    kim = Human("김상형", 24)
    kim.intro()
    kim.eat()

    lee = Student("이은서", 25, 2017)
    lee.intro()
    lee.eat()
    lee.study()

    park = Teacher("홍길동", 45)
    park.intro()
    park.eat()
    park.teach()

    print(kim)
    print(lee)

main()
