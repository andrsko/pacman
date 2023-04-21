import pygame
# TODO make configurable
color = (0, 0, 255)


class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, width, height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make top-left corner as the passed-in location
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x


def get():
    # Make the walls with parameters like (x, y, width, height)
    sprites = pygame.sprite.Group()
    coordinates_list = [
        [0, 0, 6, 600],
        [0, 0, 600, 6],
        [0, 600, 606, 6],
        [600, 0, 6, 606],
        [300, 0, 6, 66],
        [60, 60, 186, 6],
        [360, 60, 186, 6],
        [60, 120, 66, 6],
        [60, 120, 6, 126],
        [180, 120, 246, 6],
        [300, 120, 6, 66],
        [480, 120, 66, 6],
        [540, 120, 6, 126],
        [120, 180, 126, 6],
        [120, 180, 6, 126],
        [360, 180, 126, 6],
        [480, 180, 6, 126],
        [180, 240, 6, 126],
        [180, 360, 246, 6],
        [420, 240, 6, 126],
        [240, 240, 42, 6],
        [324, 240, 42, 6],
        [240, 240, 6, 66],
        [240, 300, 126, 6],
        [360, 240, 6, 66],
        [0, 300, 66, 6],
        [540, 300, 66, 6],
        [60, 360, 66, 6],
        [60, 360, 6, 186],
        [480, 360, 66, 6],
        [540, 360, 6, 186],
        [120, 420, 366, 6],
        [120, 420, 6, 66],
        [480, 420, 6, 66],
        [180, 480, 246, 6],
        [300, 480, 6, 66],
        [120, 540, 126, 6],
        [360, 540, 126, 6],
    ]

    # Loop through the list. Create the wall, add it to the list
    for coordinates in coordinates_list:
        wall = Wall(coordinates[0], coordinates[1], coordinates[2], coordinates[3], color)
        sprites.add(wall)

    # return our new list
    return sprites
