import pygame
import walls
from player import Player

width = 606
height = 606

screen = pygame.display.set_mode((width, height))
violet = (50, 20, 64)
screen.fill(violet)
pygame.display.set_caption('Pacman')

# початкові координати
x = 303 - 16
y = (7 * 60) + 19
# pacman = pygame.image.load("Pacman.png")
# pacman = pygame.transform.scale(pacman, (50, 50))
# screen.blit(pacman, (x, y))

pacman = Player(x, y, 32, 32, "Pacman.png")

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    wall_list = walls.get()
    if keys[pygame.K_RIGHT]:
        pacman.update(30, 0, wall_list)
    if keys[pygame.K_LEFT]:
        pacman.update(-30, 0, wall_list)
    if keys[pygame.K_UP]:
        pacman.update(0, -30, wall_list)
    if keys[pygame.K_DOWN]:
        pacman.update(0, 30, wall_list)

    screen.fill(violet)

    wall_list.draw(screen)
    pacman.draw(screen)
    pygame.display.update()
    clock.tick(10)
