import pygame
import walls
from character import Character
from mobs import Mobs
walls.color = (0, 0, 0)
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


game_over = False
clock = pygame.time.Clock()
wall_sprites = walls.get()

ghosts = Mobs()
ghosts.set_walls(wall_sprites)
ghosts.add(55, 200, "Blinky.png")
ghosts.add(475, 200, "Clyde.png")
ghosts.add(295, 200, "Inky.png")
ghosts.add(415, 200, "Pinky.png")

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

    ghosts.move()

    screen.fill(violet)

    wall_sprites.draw(screen)
    player.draw(screen)
    ghosts.draw(screen)

    ghost_collision = ghosts.collide(player)

    if ghost_collision:
        game_over = True

    if game_over:
        white = (255, 255, 255)
        pygame.font.init()
        font = pygame.font.Font("freesansbold.ttf", 32)
        text2 = font.render("Game Over", True, white)
        screen.blit(text2, [210, 250])

    pygame.display.update()

    clock.tick(10)
