import re


auto_num = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
auto = re.findall(r'\b\w\d{3}\w{2}\d{2,3}', auto_num)
print(f'Список номеров частных автомобилей: {auto}')
taxi = re.findall(r'\b\w{2}\d{5,6}', auto_num)
print(f'Список номеров такси: {taxi}')
