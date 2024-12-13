######################################################################
# Author: Kirsten Fuson
# Username: fusonk
#
# Assignment: Final Project
#
# Purpose: This program is designed to test my final project
#
#
######################################################################
# Acknowledgements:
#   Original test code: Scott Hegan
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from inspect import getframeinfo, stack
from game_run import Game
from player import *
from monster import *

class Damage:

    def __init__(self):
        self.game = Game()  # Initialize the game for every test

    def unittest(self, did_pass):
        """
        Prints the result of a test
        :param did_pass: a boolean representing the test
        :return: None
        """

        caller = getframeinfo(stack()[1][0])
        linenum = caller.lineno
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)


    def total_health(self,monster,start_health):
        """
        Checks if monster health is right
        :param attack:
        :param monster:
        :param start_health:
        :return:
        """
        if monster.health == start_health:   #checks if health is equal to start health
            self.unittest(True)
        else:
            self.unittest(False)

    def attack_health(self,attack,start_health):
        """
        Checks if monster health is right
        :param attack:
        :param start_health:
        :return:
        """

        if attack.health ==start_health:
            self.unittest(True)
        else:
            self.unittest(False)

    def test_monster_damage(self):
        """
        Test if monster takes damage correctly
        :return: None
        """
        #monster has two health
        monster = self.game.monster
        start_health = monster.health

        # Take 1 damage and check if health decreases
        self.game.take_hit(1)          #forces take_hit to run
        self.total_health(monster,start_health - 1) #passing monster into parameter

        if monster.health <= 1:
            self.unittest(True)
        else:
            self.unittest(False)

    def test_attack_damage(self):
        """
        Test if damage takes damage correctly
        :return:
        """
        # monster has one health
        attack = self.game.attack
        start_health = attack.health

        # Take 1 damage and check if health decreases
        self.game.take_damageA(1)
        self.total_health(attack, start_health - 1) #passing attack into parameter

        if attack.health <= 1:
            self.unittest(True)
        else:
            self.unittest(False)

    def player_health(self,player,start_health):
        """
        Checks if monster health is right
        :param player:
        :param start_health:
        :return:
        """

        if player.hp == start_health:
            self.unittest(True)
        else:
            self.unittest(False)

    def test_player_damage(self):
        """
        Test if player takes damage correctly
        :return:
        """
        #player has 5 health
        player = self.game.player
        start_health = player.hp

        #take 1 damage
        player.take_damage(1)
        self.player_health(player, start_health - 1) #passing player into parameter

        if player.hp <= 4:
            self.unittest(True)
        else:
            self.unittest(False)


    def run_test(self):
        self.test_monster_damage()
        self.test_attack_damage()
        self.test_player_damage()

if __name__ == "__main__":
    test_game = Damage()

    test_game.run_test()


