#! /usr/local/bin/python3
# coding: utf-8
"""
this module defines the character
"""

import pygame

import constants as const

class Character:
    """
    docstring for Character class.
    """
    def __init__(self, image, lab):
        """
        Initialize the instance of character.
        """
        self.image = pygame.image.load(image).convert()
        self.lab = lab
        self.pos_x = 0
        self.pos_y = 0
        self.pix_x = 0
        self.pix_y = 0
        self.objct = 0

    def moving(self, direction):
        """
        makes the character move up, down, left and right in the labyrinth.
        """
        if direction == 'right':
            if self.pos_x < (const.SPRITE_TOTAL - 1):
                if self.lab.structure[self.pos_y][self.pos_x + 1] != '0'\
                and self.lab.structure[self.pos_y][self.pos_x + 1] != 'g':
                    self.pos_x += 1
                    self.pix_x = self.pos_x * const.SPRITE_SIZE
        if direction == 'left':
            if self.pos_x > 0:
                if self.lab.structure[self.pos_y][self.pos_x - 1] != '0':
                    self.pos_x -= 1
                    self.pix_x = self.pos_x * const.SPRITE_SIZE
        if direction == 'down':
            if self.pos_y < (const.SPRITE_TOTAL - 1):
                if self.lab.structure[self.pos_y + 1][self.pos_x] != '0':
                    self.pos_y += 1
                    self.pix_y = self.pos_y * const.SPRITE_SIZE
        if direction == 'up':
            if self.pos_y > 0:
                if self.lab.structure[self.pos_y - 1][self.pos_x] != '0':
                    self.pos_y -= 1
                    self.pix_y = self.pos_y * const.SPRITE_SIZE

    def pickup_objct(self):
        """
        makes the character pick up the objects he finds on his way.
        """
        if self.lab.structure[self.pos_y][self.pos_x] == 'o':
            self.lab.structure[self.pos_y][self.pos_x] = '_'
            self.objct += 1
