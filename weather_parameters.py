import requests

url = 'https://wttr.in'  # убраны лишние пробелы в конце

weather_parameters = {
    '0': '',
    'T': ''  # чёрно-белый текст
}

response = requests.get(url, params=weather_parameters)

print(response.text)