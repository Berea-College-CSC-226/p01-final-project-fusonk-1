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
from player import *
from dungeon import *
from item import *


class player:
    def __init__(self):
        """
        Handles the basic logic needed to use the character
        """
        pass

    def move_direction(self):
        """
        uses keys to determine how to move character
        :param:
        :return:
        """
        pass

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
