import math

import pygame
from player import *
from dungeon import *
from game_run import *
from monster import *

class Attack(pygame.sprite.Sprite):
    def __init__(self,screen_size, width=20, height=20):
        #Monster attack image
        super().__init__()
        pygame.sprite.Sprite.__init__(self)  # Calls the sprite methods from pygame sprite
        self.screen_size = screen_size
        print("Spawning monster")
        self.image = pygame.image.load('image/attack.png').convert_alpha()

        # self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.surf = pygame.transform.scale(self.image, (width, height))  # changes height and width of monster

        self.rect.x = 60  # Right of screen, changes spawn point
        self.health = 2
        self.alive = True

        self.move_distance = 1
        self.directions = ["north", "south", "east", "west"]
        self.path = random.choice(self.directions)
        self.position = [0, 0]

    def movement(self):
        """
        Moves the characters in a pattern
        :return:
        """
        #Eventual movement of attack
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "north"
        if self.rect.top <= 0:
            self.path = "south"
        if self.rect.left <= 0:
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            self.path = "west"
        elif random.random() > .95:
            self.path = random.choice(self.directions)

        if self.path == "north":
            self.rect.move_ip(0, -self.move_distance)
            self.position[1] -= self.move_distance
        elif self.path == "south":
            self.rect.move_ip(0, self.move_distance)
            self.position[1] += self.move_distance
        if self.path == "east":
            self.rect.move_ip(self.move_distance, 0)
            self.position[0] -= self.move_distance
        if self.path == "west":
            self.rect.move_ip(-self.move_distance, 0)
            self.position[0] += self.move_distance





    def take_damage(self, damage):
        """
        calculates the damage the monster takes after its been hit
        :param:
        :return:
        """
        #Trying to make monster take damage
        self.health -= damage
        if self.health <= 0:
            self.kill()
