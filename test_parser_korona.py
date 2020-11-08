from bs4 import BeautifulSoup
import requests


site_link = "https://index.minfin.com.ua/ua/reference/coronavirus/ukraine/"
request_link = requests.get(site_link)
soup = BeautifulSoup(request_link.text, 'html.parser')


def number_of_city(test):
    city_name = test.lower()
    if city_name == "вінниця" or city_name == "вінницька" or city_name == "винница" or city_name == "винницкая":
        return 0
    elif city_name == "луцьк" or city_name == "луцька" or city_name == "луцк" or city_name == "луцкая":
        return 1
    elif city_name == "дніпро" or city_name == "дніпропетровська" or city_name == "днипропетровская" or city_name == "днипро":
        return 2
    elif city_name == "донецьк" or city_name == "донецька" or city_name == "донецк" or city_name == "донецкая":
        return 3
    elif city_name == "житомир" or city_name == "житомирська" or city_name == "житомир" or city_name == "житомерская":
        return 4
    elif city_name == "закарпаття" or city_name == "закарпатська":
        return 5
    elif city_name == "запоріжжя" or city_name == "запоріжська":
        return 6
    elif city_name == "івано-франківськ" or city_name == "івано-франківська" or city_name == "івано франківськ" or city_name == "івано франківська":
        return 7
    elif city_name == "київ" or city_name == "київська" or city_name == "киев" or city_name == "киевская":
        return 8
    elif city_name == "кіровоград" or city_name == "кіровоградська" or city_name == "кировоград" or city_name == "кировоградская":
        return 9
    elif city_name == "луганськ" or city_name == "луганська" or city_name == "луганск" or city_name == "луганская":
        return 10
    elif city_name == "львів" or city_name == "львівська":
        return 11
    elif city_name == "миколаїв" or city_name == "миколаївська" or city_name == "николаев" or city_name == "николаевская": 
        return 12
    elif city_name == "одеса" or city_name == "одеська" or city_name == "одесса" or city_name == "одесская":
        return 13
    elif city_name == "полтава" or city_name == "полтавська":
        return 14
    elif city_name == "рівне" or city_name == "рівненська":
        return 15
    elif city_name == "суми" or city_name == "сумська":
        return 16
    elif city_name == "тернопіль" or city_name == "тернопільська":
        return 17
    elif city_name == "харків" or city_name == "харківська":
        return 18
    elif city_name == "херсон" or city_name == "херсонська" or city_name == "херсонская":
        return 19
    elif city_name == "хмельницьк" or city_name == "хмельницька":
        return 20
    elif city_name == "черкаси" or city_name == "черкаська":
        return 21
    elif city_name == "чернівецька":
        return 22
    elif city_name == "чернігівська" or city_name == "чернігів":
        return 23
    else:
        return "good"


def starter(number):
    n_city = number
    if type(n_city) is int:
        doba = soup.find_all('small', class_='gold')[int(n_city)].text
        korona = soup.find_all('td', class_='blank larger')[int(n_city)].text
        return "Всього хворих: " + str(korona) + ", за добу " + str(doba)
    else:
        return ""
