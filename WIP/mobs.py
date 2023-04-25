from inspect import getmembers

import pygame
import random
from character import Character


class Mobs:
    def __init__(self):
        # Вбудований базовий тип у Пітоні
        # Щоб викликати методи руху і відмальовки для кожного спрайту
        self.sprite_list = []

        # Об'єкт бібліотеки pygame
        # Щоб перевіряти зіткнення з гравцем
        self.sprite_group = pygame.sprite.Group()

        self.walls = []

    def set_walls(self, walls):
        self.walls = walls

    def add(self, x, y, filename):
        sprite = Mob(x, y, filename)
        from pprint import pprint
        pprint(getmembers(sprite))
        sprite.set_walls(self.walls)
        self.sprite_list.append(sprite)
        self.sprite_group.add(sprite)

    def move(self):
        for sprite in self.sprite_list:
            sprite.move()

    def draw(self, screen):
        for sprite in self.sprite_list:
            sprite.draw(screen)

    def check_collision(self, player):
        return pygame.sprite.spritecollide(player, self.sprite_group, False)


class Mob(Character):
    def __init__(self, x, y, filename):
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, (32, 32))
        Character.__init__(self, x, y, image)
        self.previous_positions = [[0, 0], [0, 0], [0, 0]]

    def update(self, new_x, new_y):
        self.rect.left += new_x
        self.rect.top += new_y

    def collides_with_walls(self, new_x, new_y):
        old_x = self.rect.left
        old_y = self.rect.top

        self.rect.left = new_x
        self.rect.top = new_y

        collide = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.left = old_x
        self.rect.top = old_y
        return collide

    def move(self):
        moves = [(30, 0), (-30, 0), (0, -30), (0, 30)]

        random_move = random.choice(moves)
        new_x = self.rect.left + random_move[0]
        new_y = self.rect.top + random_move[1]
        while (new_x == self.previous_positions[0][0] and new_y == self.previous_positions[0][1]
                or new_x == self.previous_positions[1][0] and new_y == self.previous_positions[1][1]
                or new_x == self.previous_positions[2][0] and new_y == self.previous_positions[2][1]
                or self.collides_with_walls(new_x, new_y)):
            random_move = random.choice(moves)
            new_x = self.rect.left + random_move[0]
            new_y = self.rect.top + random_move[1]
        self.update(random_move[0], random_move[1])
        # self.previous_positions[0] = self.previous_positions[1].copy()
        # self.previous_positions[1] = self.previous_positions[2].copy()
        self.previous_positions[0][0] = self.previous_positions[1][0]
        self.previous_positions[0][1] = self.previous_positions[1][1]
        self.previous_positions[1][0] = self.previous_positions[2][0]
        self.previous_positions[1][1] = self.previous_positions[2][1]
        self.previous_positions[2][0] = self.rect.left
        self.previous_positions[2][1] = self.rect.top
