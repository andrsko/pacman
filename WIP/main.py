import pygame
import walls
from character import Character
from ghost import Ghost
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
# pacman = pygame.image.load("Pacman.png")
# pacman = pygame.transform.scale(pacman, (50, 50))
# screen.blit(pacman, (x, y))

pacman = Character(x, y, "../Pacman.png")
ghost1 = Ghost(55, 200, "Blinky.png")
ghost2 = Ghost(475, 200, "Clyde.png")
ghost3 = Ghost(295, 200, "Inky.png")
ghost4 = Ghost(415, 200, "Pinky.png")
ghosts = pygame.sprite.Group()
ghosts.add(ghost1, ghost2, ghost3, ghost4)
game_over = False
clock = pygame.time.Clock()
wall_sprites = walls.get()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        pacman.update(30, 0, wall_sprites)
    if keys[pygame.K_LEFT]:
        pacman.update(-30, 0, wall_sprites)
    if keys[pygame.K_UP]:
        pacman.update(0, -30, wall_sprites)
    if keys[pygame.K_DOWN]:
        pacman.update(0, 30, wall_sprites)

    screen.fill(violet)
    ghost1.update_random(wall_sprites)
    ghost2.update_random(wall_sprites)
    ghost3.update_random(wall_sprites)
    ghost4.update_random(wall_sprites)
    wall_sprites.draw(screen)
    pacman.draw(screen)
    ghost1.draw(screen)
    ghost2.draw(screen)
    ghost3.draw(screen)
    ghost4.draw(screen)
    ghost_collision = pygame.sprite.spritecollide(pacman, ghosts, False)
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
