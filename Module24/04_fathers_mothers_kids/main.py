import parent
import child

parent_1 = parent.Parent('Анна', 27, [])
child_1 = child.Child('Ева', 3, relax=True, hunger=False)
child_2 = child.Child('Есения', 12, relax=False, hunger=True)

if parent_1.age - child_1.age >= 16:
    parent_1.children.append([child_1.name, child_1.age, child_1.relax,
                              child_1.hunger])
else:
    print(f'Возраст ребенка {child_1.name} должен быть меньше возраста родителя'
          f' хотя бы на 16 лет')
if parent_1.age - child_2.age >= 16:
    parent_1.children.append([child_2.name, child_2.age, child_2.relax,
                              child_2.hunger])
else:
    print(f'Возраст ребенка {child_2.name} должен быть меньше возраста '
          'родителя хотя бы на 16 лет')
    

parent_1.info()
print('\nГолодны ли дети?')
parent_1.check_hunger()
print('\nДети волнуются?')
parent_1.check_relax()
