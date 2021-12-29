def move_disk(disk, start=1, stop=3):
    if disk == 1:
        print(f'Переложить диск {disk} со стержня номер {start} '
              f'на стержень номер {stop}')
    else:
        move_disk(disk - 1, start, 6 - start - stop)
        print(f'Переложить диск {disk} со стержня номер {start} '
              f'на стержень номер {stop}')
        move_disk(disk - 1, 6 - start - stop, stop)


total_disks = int(input('Введите количество дисков:'))
move_disk(total_disks)
