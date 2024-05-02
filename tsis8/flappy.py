import pygame
import sys
import random

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Перемещение фона и переднего фона")

done = False
clock = pygame.time.Clock()

back = pygame.image.load("out.png").convert()
back = pygame.transform.scale(back, (700, 500))

front = pygame.image.load("bluebird.png").convert_alpha()
front = pygame.transform.scale(front, (50, 45))

# Инициализация и настройка препятствий
obstacle_image = pygame.image.load("pipe.png").convert_alpha()
obstacle_image = pygame.transform.scale(obstacle_image, (50, 300))  # Размер столба

obstacle_gap = 150  # Расстояние между верхним и нижним препятствиями
obstacle_x = 700  # Начальная позиция X препятствий (с правой стороны экрана)
obstacle_top_y = random.randint(-250, -100)  # Случайная начальная позиция Y верхнего препятствия
obstacle_bottom_y = obstacle_top_y + obstacle_image.get_height() + obstacle_gap  # Позиция Y нижнего препятствия

back_position = 0
back_speed = -2  # Скорость движения фона влево

front_x = 350
front_y = 250
front_speed = 5

# Границы для переднего изображения (птицы)
min_x = 0
max_x = size[0] - front.get_width()
min_y = 0
max_y = size[1] - front.get_height()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        front_x -= front_speed
        if front_x < min_x:
            front_x = min_x
    if keys[pygame.K_d]:
        front_x += front_speed
        if front_x > max_x:
            front_x = max_x
    if keys[pygame.K_w]:
        front_y -= front_speed
        if front_y < min_y:
            front_y = min_y
    if keys[pygame.K_s]:
        front_y += front_speed
        if front_y > max_y:
            front_y = max_y

    back_position += back_speed
    if back_position <= -700:
        back_position = 0

    obstacle_x -= 2  # Скорость движения препятствий влево
    if obstacle_x < -50:  # Проверка, вышло ли препятствие за пределы экрана
        obstacle_x = 700
        obstacle_top_y = random.randint(-250, -100)
        obstacle_bottom_y = obstacle_top_y + obstacle_image.get_height() + obstacle_gap

    # Отрисовка
    screen.blit(back, (back_position, 0))
    screen.blit(back, (back_position + 700, 0))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(obstacle_x, obstacle_top_y, obstacle_image.get_width(), obstacle_image.get_height()))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(obstacle_x, obstacle_bottom_y, obstacle_image.get_width(), obstacle_image.get_height()))

    screen.blit(front, (front_x, front_y))
    
    # Проверка столкновений
    bird_rect = pygame.Rect(front_x, front_y, front.get_width(), front.get_height())
    top_obstacle_rect = pygame.Rect(obstacle_x, obstacle_top_y, obstacle_image.get_width(), obstacle_image.get_height())
    bottom_obstacle_rect = pygame.Rect(obstacle_x, obstacle_bottom_y, obstacle_image.get_width(), obstacle_image.get_height())
    if bird_rect.colliderect(top_obstacle_rect) or bird_rect.colliderect(bottom_obstacle_rect):
        done = True  # Завершение игры при столкновении

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
