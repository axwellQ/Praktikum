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

    def is_off_screen(self):
        return self.y - self.radius > HEIGHT

    def collides_with_ship(self, ship):
        if not ship.alive:
            return False
        ship_rect = pygame.Rect(ship.x - ship.width//2, ship.y, ship.width, ship.height)
        comet_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        return ship_rect.colliderect(comet_rect)

    def collides_with_bullet(self, bullet):
        bx, by = bullet
        distance = ((self.x - bx) ** 2 + (self.y - by) ** 2) ** 0.5
        return distance < self.radius + 5

# Создание кораблей
ship1 = Ship(WIDTH // 3, ship1_image, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
ship2 = Ship(2 * WIDTH // 3, ship2_image, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)

bullets = []
comets = []

# Игровые параметры
comet_spawn_timer = 0
comet_base_speed = 2
comet_speed = comet_base_speed
game_over = False
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if game_over and event.key == pygame.K_r:
                # Перезапуск
                ship1 = Ship(WIDTH // 3, ship1_image, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
                ship2 = Ship(2 * WIDTH // 3, ship2_image, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
                bullets = []
                comets = []
                comet_speed = comet_base_speed
                game_over = False
                score = 0

    if game_over:
        screen.fill(BLACK)
        text = font.render("Игра окончена! Нажмите R для перезапуска", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        continue

    # Обновление звёзд
    for star in stars:
        star[1] += star[3]
        if star[1] > HEIGHT:
            star[1] = 0
            star[0] = random.randint(0, WIDTH)

    keys = pygame.key.get_pressed()
    ship1.move(keys)
    ship2.move(keys)
    ship1.shoot(keys, bullets)
    ship2.shoot(keys, bullets)

    bullets = [[x, y - 7] for x, y in bullets if y > 0]

    # Генерация комет
    comet_spawn_timer += dt
    if comet_spawn_timer > max(0.3, 2.0 - score * 0.01):
        comets.append(Comet(comet_speed))
        comet_spawn_timer = 0

    # Обновление комет
    for comet in comets[:]:
        comet.move()
        if comet.is_off_screen():
            comets.remove(comet)
            continue

        if comet.collides_with_ship(ship1):
            ship1.alive = False
        if comet.collides_with_ship(ship2):
            ship2.alive = False

        if not (ship1.alive or ship2.alive):
            game_over = True

    # Проверка попаданий
    for bullet in bullets[:]:
        for comet in comets[:]:
            if comet.collides_with_bullet(bullet):
                if bullet in bullets:
                    bullets.remove(bullet)
                comets.remove(comet)
                score += 1
                if score % 10 == 0:
                    comet_speed = comet_base_speed + score // 10 * 0.5
                break

    # Отрисовка
    screen.fill(BLACK)

    for x, y, size, _ in stars:
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), size)

    ship1.draw(screen)
    ship2.draw(screen)

    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, (bullet[0] - 2, bullet[1] - 2, 4, 8))

    for comet in comets:
        comet.draw(screen)

    score_text = font.render(f"Счёт: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()