## Задача 2. Математический модуль
Ирина использует в своей программы очень много различных математических вычислений, связанные с фигурами. 
Например, нахождение их площадей или периметров. Поэтому чтобы не “захламлять” код огромным количеством функций, 
она решила выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем math

Реализуйте класс MyMath, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):
- Нахождение длины окружности
- Площадь окружности
- Объём куба
- Площадь поверхности сферы

#### Пример основного кода:
````
res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
````
#### Результат:
````
31.41592653589793
113.09733552923255
````




