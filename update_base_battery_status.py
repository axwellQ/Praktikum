class Robot:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_base_battery_status(cls, new_status):
        cls.base_battery_status = new_status

    def report(self):
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)

    @property
    def identifier(self):
        """Вычисляет уникальный идентификатор робота на основе его имени."""
        # Преобразование имени в числовое представление:
        return sum(ord(char) for char in self.name)


# Создаём робота:
robot = Robot('R2-D2')
print(robot.identifier)
