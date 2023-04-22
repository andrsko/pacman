import pygame
import random
from character import Character
class Ghost(Character):
    def __init__(self, x, y, filename):
        Character.__init__(self, x, y, filename)
        self.previous_positions = [[0, 0], [0, 0], [0,0]]
    def collides_with_walls(self, new_x, new_y,walls):
        old_x = self.rect.left
        old_y = self.rect.top

        self.rect.left = new_x
        self.rect.top = new_y

        collide = pygame.sprite.spritecollide(self, walls, False)
        self.rect.left = old_x
        self.rect.top = old_y
        return collide

    def update_random(self, walls):
        moves = [(30, 0), (-30, 0), (0, -30), (0, 30)]

        random_move = random.choice(moves)
        new_x = self.rect.left + random_move[0]
        new_y = self.rect.top + random_move[1]
        while (new_x == self.previous_positions[0][0] and new_y == self.previous_positions[0][1]
                or new_x == self.previous_positions[1][0] and new_y == self.previous_positions[1][1]
                or new_x == self.previous_positions[2][0] and new_y == self.previous_positions[2][1]
                or self.collides_with_walls(new_x, new_y, walls)):
            random_move = random.choice(moves)
            new_x = self.rect.left + random_move[0]
            new_y = self.rect.top + random_move[1]
        self.update(random_move[0], random_move[1], walls)
        # self.previous_positions[0] = self.previous_positions[1].copy()
        # self.previous_positions[1] = self.previous_positions[2].copy()
        self.previous_positions[0][0] = self.previous_positions[1][0]
        self.previous_positions[0][1] = self.previous_positions[1][1]
        self.previous_positions[1][0] = self.previous_positions[2][0]
        self.previous_positions[1][1] = self.previous_positions[2][1]
        self.previous_positions[2][0] = self.rect.left
        self.previous_positions[2][1] = self.rect.top