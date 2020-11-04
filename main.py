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
a = (0, 255, 236)
b = (180, 255, 94)
c = (0, 93, 46)
BG = (156, 218, 255)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 20, True, False)

icon = pygame.image.load('ikon.png')
pygame.display.set_icon(icon)


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
    text = font.render('scorse: ' + str(scorse), True, c)
    screen.blit(text, (60, 20))
# столкновение
    if rect1.colliderect(rect2):
        collide = True
    else:
        collide = False

    if rect1.colliderect(rect2):
        scorse += 1

    pygame.display.update()


