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

