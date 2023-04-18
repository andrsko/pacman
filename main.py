import pygame
import walls

width = 606
height = 606

screen = pygame.display.set_mode((width, height))
violet = (50, 20, 64)
screen.fill(violet)
pygame.display.set_caption('Pacman')

# початкові координати
x = 300
y = 400
pacman = pygame.image.load("Pacman.png")
pacman = pygame.transform.scale(pacman, (50, 50))
screen.blit(pacman, (x, y))


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
    walls.get().draw(screen)
    screen.blit(pacman, (x, y))
    pygame.display.update()