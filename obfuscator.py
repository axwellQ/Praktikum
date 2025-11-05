def obfuscator(func):
    def wrapper():
        original_dict = func()
        obfuscated_dict = {}

        # Обработка поля 'name'
        name = original_dict.get('name', '')
        if len(name) <= 2:
            obfuscated_name = name
        else:
            obfuscated_name = name[0] + '*' * (len(name) - 2) + name[-1]
        obfuscated_dict['name'] = obfuscated_name

        # Обработка поля 'password'
        password = original_dict.get('password', '')
        obfuscated_dict['password'] = '*' * len(password)

        return obfuscated_dict

    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
