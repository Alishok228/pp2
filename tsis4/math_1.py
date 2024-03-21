import math

# Преобразование градусов в радианы
degree = float(input("Введите значение в градусах: "))
radian = degree * math.pi / 180
print("Значение в радианах:", radian)

# Расчет площади трапеции
height = float(input("Высота: "))
base1 = float(input("Основание, первое значение: "))
base2 = float(input("Основание, второе значение: "))
area_trapezoid = 0.5 * (base1 + base2) * height
print("Площадь трапеции:", area_trapezoid)

# Расчет площади правильного многоугольника
num_sides = int(input("Количество сторон: "))
side_length = float(input("Длина стороны: "))
area_polygon = num_sides * side_length ** 2 / (4 * math.tan(math.pi / num_sides))
print("Площадь многоугольника:", area_polygon)

# Расчет площади параллелограмма
base_length = float(input("Длина основания: "))
height_parallelogram = float(input("Высота параллелограмма: "))
area_parallelogram = base_length * height_parallelogram
print("Площадь параллелограмма:", area_parallelogram)
