import requests

url = 'https://wttr.in'  # убраны лишние пробелы в конце

weather_parameters = {
    '0': '',
    'T': '',  # чёрно-белый текст
    'M': '',  # скорость ветра в метрах в секунду
    'lang': 'ru'  # прогноз на русском языке
}

response = requests.get(url, params=weather_parameters)

print(response.text)