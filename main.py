import pygame
import sys

W = 800
H = 600
collide = False

# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# цвета
a = (0, 255, 236)
b = (180, 255, 94)
c = (0, 93, 46)
BG = (156, 218, 255)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            circle_pos = e.pos

    screen.fill(BG)

    rect1 = pygame.draw.circle(screen, a, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, c if collide else b,
                             (rect_pos, rect_size))

# столкновение
    if rect1.colliderect(rect2):
        collide = True
    else:
        collide = False

    pygame.display.update()
