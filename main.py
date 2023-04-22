import pygame
import walls
from character import Character

width = 606
height = 606

screen = pygame.display.set_mode((width, height))
violet = (50, 20, 64)
screen.fill(violet)
pygame.display.set_caption('Pacman')

# початкові координати
x = 287
y = 439
pacman = pygame.image.load("Pacman.png")
pacman = pygame.transform.scale(pacman, (32, 32))

player = Character(x, y, pacman)
player.set_walls(walls.get())

clock = pygame.time.Clock()

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

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > 603 - 32:
        x = 603 - 32
    if y > 603 - 32:
        y = 603 - 32

    player.update(x, y)
    x = player.get_x()
    y = player.get_y()

    screen.fill(violet)
    walls.get().draw(screen)
    player.draw(screen)
    pygame.display.update()

    clock.tick(20)