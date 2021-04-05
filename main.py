import pygame
import sys


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    hintergrund = pygame.image.load("graphics/backround/backround2.jpg")
    pygame.init()
    pygame.display.set_caption('\u2764\uFE0F Pinguin and Panda \u2764\uFE0F')
    screen = pygame.display.set_mode([1300, 693])
    clock = pygame.time.Clock()


    def zeichnen():
        screen.blit(hintergrund, (0, 0))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
        pygame.display.update()


    x = 300
    y = 477
    speed = 5
    width = 32
    height = 32

    linkeWand = pygame.draw.rect(screen, (0, 0, 255), (0, 0, 2, 693), 0)
    rechteWand = pygame.draw.rect(screen, (0, 0, 255), (1301, 0, 0, 693), 10)

    go = True
    sprungvar = -16
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        spielerRechteck = pygame.Rect(x,y,width,height)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and sprungvar == -16:
            sprungvar = 15
        if pressed[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):
            x += speed
        #if pressed[pygame.K_DOWN]:
        #    y += speed
        if pressed[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):
            x -= speed

        if sprungvar >= -15:
            n = 1
            if sprungvar < 0:
                n = -1
            y -= (sprungvar**2)*0.17*n
            sprungvar -= 1
        zeichnen()
        clock.tick(60)
