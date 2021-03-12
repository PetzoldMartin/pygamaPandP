import pygame
import sys


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    pygame.init()
    pygame.display.set_caption('\u2764\uFE0F Pinguin and Panda \u2764\uFE0F')
    screen = pygame.display.set_mode([600, 600])
    clock = pygame.time.Clock()

    x = 300
    y = 300
    speed = 3
    width = 40
    height = 80

    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= speed
        if pressed[pygame.K_RIGHT]:
            x += speed
        if pressed[pygame.K_DOWN]:
            y += speed
        if pressed[pygame.K_LEFT]:
            x -= speed

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 0), (x, y, width, height))
        pygame.display.update()
        clock.tick(60)
