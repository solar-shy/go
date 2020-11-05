import pygame
import sys

W = 800
H = 600
collide = False
scorse = 0


# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# цвета
a = (0, 255, 236, 180)
b = (180, 255, 94, 180)
c = (0, 93, 46, 180)
BG = (156, 218, 255)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 20, True, False)
# Создаем поверхность размером в 2 раза больше радиуса круга и вкл. альфа-канал
surface = pygame.Surface((circle_radius * 2, circle_radius * 2),
                         pygame.SRCALPHA)
# на созданной поверхности рисуем круг а цвета
pygame.draw.circle(surface, a, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

Clock = pygame.time.Clock()
FPS = 666
speed_x, speed_y = 1, 1

ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect()


while True:
    Clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos
    
    screen.fill(BG)

    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > W:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > H:
        speed_y = -speed_y

    COLOR = c if collide else b
    # rect1 = pygame.draw.circle(screen, a, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, COLOR, (rect_pos, rect_size))
    text = font.render('scorse: ' + str(scorse), True, c)
    screen.blit(text, (60, 20))
    screen.blit(surface, rect1)
    screen.blit(ball, ball_rect)

# столкновение
    if rect1.colliderect(rect2):
        collide = True
        if COLOR == b:
            scorse += 1
    else:
        collide = False

    pygame.display.update()

