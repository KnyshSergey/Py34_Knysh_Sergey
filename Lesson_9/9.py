class Trianle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        sides = sorted((self.a, self.b, self.c))

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "Отрицательные числа или ноль"
        elif sides[0] + sides[1] > sides[2]:
            return "Треугольник существует"
        else:
            return "Треугольник не существует"


tr1 = Trianle(-1, 2, 3)
tr2 = Trianle(1, 2, 3)
tr3 = Trianle(3, 4, 5)
print(tr1.is_triangle())
print(tr2.is_triangle())
print(tr3.is_triangle())


class KgToPounds:
    pounds = property()
    kg = property()

    def __init__(self, kg):
        self.__kg = kg

    @pounds.getter
    def pounds(self):
        return self.__kg * 2.205

    @pounds.setter
    def pounds(self, value):
        self.__kg = value / 2.205

    @kg.getter
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, value):
        self.__kg = value


weightCalc = KgToPounds(10)
print(weightCalc.pounds)
print(weightCalc.kg)
weightCalc.pounds = 100
print(weightCalc.kg)


#
# 1️⃣ . Написать программу, которая будет создавать класс данных из JSON объекта.
# (Дополнительно): Добавить метод для данного класса, который будет выводить все поля класса.
#
# 2️⃣. Создать класс Прямоугольник, который имеет свойства Ширина и Высота. Также добавить свойство для нахождения площади. Свойства реализовать через property.


