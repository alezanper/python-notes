#Inheritance order
class Animal:
    average_age_1 = 100
    def __init__(self):
        self.average_height_1 = 120
    def average_weight_1(self):
        return 15

class Mammal(Animal):
    average_age_2 = 40
    def __init__(self):
        super().__init__()
        self.average_height_2 = 90
    def average_weight_2(self):
        return 10

class Cat(Mammal):
    average_age_3 = 15
    def __init__(self):
        super().__init__()
        self.average_height_3 = 40
    def average_weight_3(self):
        return 5

itachi = Cat()

print("Object's heritance")
print(itachi.average_age_1, itachi.average_height_1, itachi.average_weight_1())   # 100 120 15
print(itachi.average_age_2, itachi.average_height_2, itachi.average_weight_2())   # 40 90 10
print(itachi.average_age_3, itachi.average_height_3, itachi.average_weight_3())   # 15 40 5