import circle


circle_1 = circle.Circle(0, 0, 1)
circle_2 = circle.Circle(1, 2, 1)
print(f'Площадь первой окружности: {circle_1.find_s()}')
print(f'Периметр первой окружности: {circle_1.find_p()}')
circle_1.find_intersection(circle_2)
print('Увеличение радиуса второй окружности в 2 раза.')
circle_2.rise(2)
circle_1.find_intersection(circle_2)