class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")

    def __str__(self):
        return f'<Human name = {self.name}, age = {self.name}>'


def main():

    kim = Human("김상형",29)
    kim.intro()

    lee = Human("이승우",45)
    lee.intro()

    print(kim.name, kim.age)
    print(lee.name, lee.age)
    print(kim)
    print(lee)
main()