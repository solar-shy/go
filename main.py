import pygame
import sys

W = 800
H = 600
collide = False
collide2 = False
scorse_k = 0
scorse_s = 0
block = False
block2 = False


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

speed = [5, 5]

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 20, True, False)

icon = pygame.image.load('ikon.png')
pygame.display.set_icon(icon)

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


def pp(x, y):
    if ball_rect.left < 0 or ball_rect.right > W:
        speed[0] = -x
    elif ball_rect.top < 0 or ball_rect.bottom > H:
        speed[1] = -y
    return ball_rect.move(speed)


while True:
    Clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            rect1.center = e.pos
    screen.fill(BG)

    COLOR = c if block or block2 else b
    # rect1 = pygame.draw.circle(screen, a, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, COLOR,
                             (rect_pos, rect_size))
    text = font.render('scorse_k: ' + str(scorse_k), True, c)
    screen.blit(text, (60, 20))
    text1 = font.render('scorse_s: ' + str(scorse_s), True, c)
    screen.blit(text1, (650, 20))
    screen.blit(surface, rect1)
    screen.blit(ball, ball_rect)

# столкновение
    if ball_rect.colliderect(rect2):
        block = True
        if COLOR == b:
            scorse_k += 1
    else:
        block = False
    if rect1.colliderect(rect2):
        block2 = True
        if COLOR == b:
            scorse_s += 1
    else:
        block2 = False
    ball_rect = pp(speed[0], speed[1])
    pygame.display.update()
