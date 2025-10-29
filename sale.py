class Customer:
    def __init__(self, name):
        self.name = name
        # Приватный атрибут со значением по умолчанию 10
        self.__discount = 10

    def get_price(self, original_price):
        # Применяем скидку и округляем до двух знаков
        discounted_price = original_price * (1 - self.__discount / 100)
        return round(discounted_price, 2)

    def set_discount(self, new_discount):
        # Ограничиваем скидку максимум 80%
        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


# Пример использования:
customer = Customer("Иван Иванович")
print(customer.get_price(100))  # 90.0
customer.set_discount(20)
print(customer.get_price(100))  # 80.0