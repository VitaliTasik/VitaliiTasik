import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Створення вікна гри
window = pygame.display.set_mode((800, 600))

# Створення змії
snake = [[200, 200], [220, 200], [240, 200]]
direction = 'right'

# Створення крапки
food = [random.randint(0, 39) * 20, random.randint(0, 29) * 20]

# Основний цикл гри
running = True
while running:
    # Отримання подій від користувача
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = 'up'
            elif event.key == pygame.K_s:
                direction = 'down'
            elif event.key == pygame.K_a:
                direction = 'left'
            elif event.key == pygame.K_d:
                direction = 'right'

    # Рух змії
    head = snake[-1]
    if direction == 'up':
        new_head = [head[0], head[1] - 20]
    elif direction == 'down':
        new_head = [head[0], head[1] + 20]
    elif direction == 'left':
        new_head = [head[0] - 20, head[1]]
    elif direction == 'right':
        new_head = [head[0] + 20, head[1]]
    snake.append(new_head)

    # Перевірка, чи змія потрапила на крапку
    if snake[-1] == food:
        # Згенерувати нову випадкову координату для крапки
        food = [random.randint(0, 39) * 20, random.randint(0, 29) * 20]
    else:
        # Видалити останню частину змії
        snake.pop(0)

    # Оновлення вікна
    window.fill((0, 0, 0))
    for pos in snake:
        pygame.draw.rect(window, (255, 255, 255), (pos[0], pos[1], 20, 20))
    pygame.draw.rect(window, (255, 0, 0), (food[0], food[1], 20, 20))
    pygame.display.update()

    # Затримка для регулювання швидкості гри
    pygame.time.delay(100)

# Закриття вікна гри
pygame.quit()