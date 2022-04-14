import random

def main():
    for i in range(5):
        print(random.random(), end=", ")
    
    print()

    for i in range(5):
        print(random.randint(1,10), end=", ")

    print()

    for i in range(5):
        print(random.randrange(1,10), end=", ")

    print()

    for i in range(5):
        print(random.uniform(1,10), end = ", ")

    print()
    food = ["cheese","apple","banana","watermelon"]
    random.shuffle(food)
    print(food)

    print(random.sample(food,3))
    
    

main()