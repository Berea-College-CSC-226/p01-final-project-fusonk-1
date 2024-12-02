######################################################################
# Author: Kirsten Fuson
# Username: fusonk
#
# Assignment: Final Project
#
# Purpose:
#
#
######################################################################
# Acknowledgements:
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import pygame
# from dungeon import *
# from item import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size, width=50, height=50):
        """
        Represents the player in the game.

        :param screen_size: Screen size, for keeping character on the screen
        """
        super().__init__()
        self.screen_size = screen_size
        print("Spawning player")
        self.surf = pygame.image.load('image/player.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)
        self.size = 5
        self.surf = pygame.transform.scale(self.surf, (width, height)) #changes height and width of monster


    def movement(self, keys):
        """
        Handles movement events from the player

        :param keys: key presses from pygame event listener

        :return: None
        """
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -3)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 3)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(3, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-3, 0)

        self.rect.x = max(0, min(self.rect.x, self.screen_size[0] - self.rect.width))  #keeps player in boundary
        self.rect.y = max(0, min(self.rect.y, self.screen_size[1] - self.rect.height))

    def take_damage(self):
        """
        calculates the damage the player takes after its been hit, and reduces health
        :param:
        :return:
        """
        pass

    def attack_monster(self, monster):
        """
        calculates damage done to monster, and if it can be hit
        :param monster:
        :return:
        """
        pass

    def add_item(self):
        """
        Adds items to the player main screen (gold), or other
        :return:
        """
        pass

    def use_item(self):
        """
        allows player to use item in inventory, removes item if needed
        :return:
        """
