"""
A simple class to handle DB Characters

@Author: Vittorione
@Date: January 2025
"""


class Character:
    def __init__(self, name, attack, defence, hp, ep):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.ep = ep

