import pygame
import sys

# Сначала делаем инициализацию Pygame
pygame.init()

# Установливаем размер экрана (ширина, высота)
size = (700, 500)
screen = pygame.display.set_mode(size)

# Установливаем заголовок окна
pygame.display.set_caption("Перемещение фона и переднего фона")

# Создаем переменную для завершения программы
done = False

# Управляем FPS
clock = pygame.time.Clock()

# Загружаем изображения для заднего фона
back = pygame.image.load("1.png").convert()

# Загружаем изображения для переднего фона
front = pygame.image.load("33.png").convert_alpha()

# Начальное положение фона
back_position = 0

# Скорость и направление фона
back_speed = 2  # Движение вправо

# Основной цикл программы
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Обновление позиции фона
    back_position -= back_speed

    # Данный кусочек кода нужен для того, чтобы задний фон после перемещения влево сразу возвращался справа
    if back_position <= -back.get_width():
        back_position = 0

    # Отрисовка фона
    screen.blit(back, (back_position, 0))
    screen.blit(back, (back_position + back.get_width(), 0))

    # Отрисовка переднего плана
    screen.blit(front, (0, 0))  # Положение переднего плана

    # Обновление экрана
    pygame.display.flip()

    # Устанавливаем FPS
    clock.tick(60)

# Закрываем окно и завершаем программу.
pygame.quit()
sys.exit()

# В целом на этом все, как то так:)