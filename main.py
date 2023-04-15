import pygame
import walls

width = 606
height = 606

screen = pygame.display.set_mode((width, height))
violet = (50, 20, 64)
screen.fill(violet)
pygame.display.set_caption('Pacman')
pacman = pygame.image.load("Pacman.png")
pacman = pygame.transform.scale(pacman, (50, 50))

# початкові координати
x = 100
y = 100

screen.blit(pacman, (x, y))
pygame.display.update()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x = x + 0.1
    if keys[pygame.K_LEFT]:
        x = x - 0.1
    if keys[pygame.K_UP]:
        y = y - 0.1
    if keys[pygame.K_DOWN]:
        y = y + 0.1

    screen.fill(violet)
    screen.blit(pacman, (x, y))
    walls.get().draw(screen)
    pygame.display.update()