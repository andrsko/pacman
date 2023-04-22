import pygame

class Character(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.walls = []


    def set_walls(self, walls):
        self.walls = walls
    def update(self, new_x, new_y):
        old_x = self.rect.left
        old_y = self.rect.top

        self.rect.left += (new_x - old_x)*300
        self.rect.top += (new_y - old_y)*300

        collide = pygame.sprite.spritecollide(self, self.walls, False)
        if collide:
            self.rect.left = old_x
            self.rect.top = old_y

    def get_x(self):
        return self.rect.left

    def get_y(self):
        return self.rect.top
    def draw(self, screen):
        screen.blit(self.image, self.rect)
