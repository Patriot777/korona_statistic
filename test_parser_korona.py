from bs4 import BeautifulSoup
import requests


site_link = "https://index.minfin.com.ua/ua/reference/coronavirus/ukraine/"
request_link = requests.get(site_link)
soup = BeautifulSoup(request_link.text, 'html.parser')


def number_of_city(test):
    city_name = test
    if city_name == "Вінниця" or city_name == "Вінницька":
        return 0
    elif city_name == "Луцьк":
        return 1
    elif city_name == "Дніпро":
        return 2
    elif city_name == "Донецьк":
        return 3
    elif city_name == "Житомир":
        return 4
    elif city_name == "Закарпаття":
        return 5
    elif city_name == "Запоріжжя":
        return 6
    elif city_name == "Івано-Франківськ":
        return 7
    elif city_name == "Київ":
        return 8
    elif city_name == "Кіровоград":
        return 9
    elif city_name == "Луганськ":
        return 10
    elif city_name == "Львів":
        return 11
    elif city_name == "Миколаїв":
        return 12
    elif city_name == "Одеса":
        return 13
    elif city_name == "Полтава":
        return 14
    elif city_name == "Рівне":
        return 15
    elif city_name == "Суми":
        return 16
    elif city_name == "Тернопіль":
        return 17
    elif city_name == "Харків":
        return 18
    elif city_name == "Херсон":
        return 19
    elif city_name == "Хмельницьк":
        return 20
    elif city_name == "Черкаси":
        return 21
    elif city_name == "Чернівецька":
        return 22
    elif city_name == "Чернігівська":
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
        return "Я тебе зрозумів...."
