import pygame

class Character(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load(filename)
        self.image = pygame.transform.scale(image, (32, 32))

        self.rect = self.image.get_rect()

        self.rect.left = x
        self.rect.top = y

    def update(self, new_x, new_y, walls):
        old_x = self.rect.left
        old_y = self.rect.top

        self.rect.left += new_x
        self.rect.top += new_y

        collide = pygame.sprite.spritecollide(self, walls, False)
        if collide:
            self.rect.left = old_x
            self.rect.top = old_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
