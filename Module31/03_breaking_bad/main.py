import requests
import json


def create_json_file(name: str) -> None:
    """Создает файлы json из ключей словаря по полученному реквесту с сайта:
    - https://www.breakingbadapi.com/api/"""
    with open(f'{name}.json', 'w') as file:
        req = requests.get(data[f'{name}'])
        date = json.loads(req.text)
        json.dump(date, file, indent=4)


my_req = requests.get('https://www.breakingbadapi.com/api/')
data = json.loads(my_req.text)
data_dict = dict()

with open('j_son.json', 'w') as j_son:
    json.dump(data, j_son, indent=4)
    for key in data.keys():
        create_json_file(key)


with open('deaths.json', 'r') as deaths:
    data_deaths = json.load(deaths)
    total_death = 0
    
    for i in data_deaths:
        if i['number_of_deaths'] > total_death:
            season = i['season']
            episode = i['episode']
            total_death = i['number_of_deaths']
            death_list = i['death']
    
    with open('episodes.json', 'r') as episodes:
        data_episodes = json.load(episodes)
        for i in data_episodes:
            if season == int(i['season']) and episode == int(i['episode']):
                episode_id = i['episode_id']

    data_dict = {'Id эпизода': episode_id, 'Номер сезона': season, 'Номер эпизода': episode,
                 'Общее количество смертей': total_death, 'Список погибших': death_list}
    

for i, key in enumerate(data_dict.keys()):
    print(f'{i + 1}. {key}: {data_dict[key]}')
    