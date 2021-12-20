violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs = int(input('Сколько песен выбрать: '))
all_time = 0

for i in range(songs):
    song = input(f'Название {i + 1} песни: ')

    while song not in violator_songs.keys():
        print('Нет такой песни в списке, попробуйте еще раз.')
        song = input(f'Название {i + 1} песни: ')

    all_time += violator_songs[song]

print(f'\nОбщее время звучания: {round(all_time, 2)} минут.')
