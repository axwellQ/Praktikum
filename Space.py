import pygame
import random
import sys
import os

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космическая битва: Защита от комет")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 255, 100)

SHIP1_IMAGE_PATH = r"  "  # ← ЗАМЕНИ НА СВОЙ ПУТЬ
SHIP2_IMAGE_PATH = r"  "   # ← ЗАМЕНИ НА СВОЙ ПУТЬ

# Функция загрузки изображения с резервным вариантом
def load_ship_image(path, default_color):
    if os.path.exists(path):
        try:
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (50, 40))
        except Exception as e:
            print(f"Ошибка загрузки изображения {path}: {e}")
    # Резерв: рисуем простой корабль
    surf = pygame.Surface((50, 40), pygame.SRCALPHA)
    pygame.draw.polygon(surf, default_color, [(25, 0), (0, 40), (50, 40)])
    pygame.draw.rect(surf, (255, 255, 0), (15, -10, 6, 10))   # пушка слева
    pygame.draw.rect(surf, (255, 255, 0), (29, -10, 6, 10))   # пушка справа
    return surf

# Загружаем изображения
ship1_image = load_ship_image(SHIP1_IMAGE_PATH, (50, 100, 255))  # синий по умолчанию
ship2_image = load_ship_image(SHIP2_IMAGE_PATH, (255, 50, 50))   # красный по умолчанию

# Создание звёздного фона
def create_stars(num_stars=100):
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.uniform(0.5, 2)
        speed = random.uniform(0.2, 0.8)
        stars.append([x, y, size, speed])
    return stars

stars = create_stars()

# Класс корабля
class Ship:
    def __init__(self, x, image, left_key, right_key, shoot_key1, shoot_key2):
        self.x = x
        self.y = HEIGHT - 60
        self.image = image
        self.width, self.height = image.get_size()
        self.speed = 5
        self.alive = True
        self.left_key = left_key
        self.right_key = right_key
        self.shoot_key1 = shoot_key1
        self.shoot_key2 = shoot_key2
        self.next_gun = 0  # для чередования пушек

    def draw(self, surface):
        if self.alive:
            surface.blit(self.image, (self.x - self.width // 2, self.y))

    def move(self, keys):
        if not self.alive:
            return
        if keys[self.left_key]:
            self.x = max(self.x - self.speed, self.width // 2)
        if keys[self.right_key]:
            self.x = min(self.x + self.speed, WIDTH - self.width // 2)

    def shoot(self, keys, bullets):
        if not self.alive:
            return
        if keys[self.shoot_key1] or keys[self.shoot_key2]:
            offset = 12 if self.next_gun == 1 else -12
            bullets.append([self.x + offset, self.y])
            self.next_gun = 1 - self.next_gun

# Класс кометы
class Comet:
    def __init__(self, speed):
        self.x = random.randint(20, WIDTH - 20)
        self.y = -20
        self.radius = random.randint(10, 20)
        self.speed = speed
        self.color = (random.randint(150, 255), random.randint(100, 200), random.randint(100, 200))

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.polygon(surface, (100, 100, 200), [
            (self.x - 5, self.y + self.radius),
            (self.x, self.y + self.radius + 20),
            (self.x + 5, self.y + self.radius)
        ])

