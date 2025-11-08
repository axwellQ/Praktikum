user_query = 'как стать бэкенд-разработчиком'

# Разбиваем строку по пробелам и затем объединяем с '%20'
url = 'https://yandex.ru/search/?text=' + '%20'.join(user_query.split(' '))

print(url)