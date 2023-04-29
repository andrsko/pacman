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
        self.game_over = False

    def set_walls(self, walls):
        self.walls = walls

    def add(self, x, y, filename, remove_background=False, background_color=(255, 255, 255)):
        sprite = Mob(x, y, filename, remove_background, background_color)
        sprite.set_walls(self.walls)
        self.sprite_list.append(sprite)
        self.sprite_group.add(sprite)

    def move(self):
        for sprite in self.sprite_list:
            sprite.move()

    def draw(self, screen):
        for sprite in self.sprite_list:
            sprite.draw(screen)

    def collide(self, player):
        return pygame.sprite.spritecollide(player, self.sprite_group, False)

    def check_game_over(self, player, screen):
        ghost_collision = self.collide(player)

        if ghost_collision:
            self.game_over = True

        if self.game_over:
            font_color = (255, 255, 255)  # Білий
            pygame.font.init()
            font = pygame.font.Font("freesansbold.ttf", 32)
            text2 = font.render("Game Over", True, font_color)
            screen.blit(text2, [210, 250])


class Mob(Character):
    def __init__(self, x, y, filename, remove_background, background_color):
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, (32, 32))
        if remove_background:
            image.set_colorkey(background_color)
            image = image.convert_alpha()
        Character.__init__(self, x, y, image)
        self.previous_position = [0, 0]

    def update(self, new_x, new_y):
        self.rect.left += new_x
        self.rect.top += new_y

    def collides_with_walls(self, new_x, new_y):
        """
        Тільки перевірити - не переміщаючи в результаті.
        Для цього потрібно: запам'ятати поточні координати, далі
        перемістити тимчасово щоб використати вбудовану функцію
        перевірки зіткнення і далі повернути початкові координати.
        """
        old_x = self.rect.left
        old_y = self.rect.top

        self.rect.left = new_x
        self.rect.top = new_y

        collide = pygame.sprite.spritecollide(self, self.walls, False)

        self.rect.left = old_x
        self.rect.top = old_y

        return collide

    def move(self):
        """
        Здійснити рух персонажа у випадковому напрямку.
        Щоб рух був плавний і направлений - перевіряти
        на зіткнення зі стінами і направленість в одну сторону
        за допомогою порівняння з попередніми координатами.
        """
        moves = [(30, 0), (-30, 0), (0, -30), (0, 30)]

        random_move = random.choice(moves)
        new_x = self.rect.left + random_move[0]
        new_y = self.rect.top + random_move[1]

        # Вибирати нову позицію поки вона не буде співпадати з
        # попередніми координатами і не впиратися в стіну,
        # що змусило б персонажа лишатися на місці протягом
        # поточного кадру
        while ([new_x, new_y] == self.previous_position
                or self.collides_with_walls(new_x, new_y)):
            random_move = random.choice(moves)
            new_x = self.rect.left + random_move[0]
            new_y = self.rect.top + random_move[1]

        self.previous_position = [self.rect.left, self.rect.top]

        self.update(random_move[0], random_move[1])
