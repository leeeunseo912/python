class Human:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

kim = Human("김상형", 29, "성남")
sang = Human("김상형", 29, "서울")
moon = Human("문종민", 44, "일본")

print(kim == sang)
print(kim == moon)