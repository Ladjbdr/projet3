#! /usr/local/bin/python3
# coding: utf-8
"""
this module defines and creates the levels' labyrinth structure.
"""

import random

import pygame

import constants as const

class Labyrinth:
    """initialize the level and its labyrinth's structure. it takes a .txt file
    as argument.
    """
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def create_lab(self):
        """
        create the structure of the labyrinth by inserting the items in the
        file in a list of lists. the structure being the list and the lines the
        lists.
        """
        with open(self.file, 'r') as lab:
            lab_str = []
            for line in lab:
                lab_line = []
                for item in line:
                    if line != '\n':
                        lab_line.append(item)
                lab_str.append(lab_line)
        self.structure = lab_str

    def lab_object(self):
        """
        randomly places the objects in the labyrinth .
        """
        counter = 3
        while counter > 0:
            rand_line = random.choice(self.structure)
            item_index = list()
            for item in rand_line:
                if item == '_':
                    item_index.append(rand_line.index(item))
            counter -= 1
            rand_line[random.choice(item_index)] = 'o'

    def display_lab(self, window):
        """
        display the labyrinth and all its objects.
        """
        wall = pygame.image.load(const.WALL).convert()
        path = pygame.image.load(const.PATH).convert()
        objct = pygame.image.load(const.OBJCT).convert()
        guard = pygame.image.load(const.GUARD).convert()
        guard = pygame.transform.scale(guard, (const.SPRITE_SIZE,\
        const.SPRITE_SIZE)).convert()

        line_index = 0
        for line in self.structure:
            item_index = 0
            for item in line:
                item_pix_x = item_index * const.SPRITE_SIZE
                item_pix_y = line_index * const.SPRITE_SIZE
                if item == '0':
                    window.blit(wall, (item_pix_x, item_pix_y))
                if item == '_' or item == 'a' or item == 'd':
                    window.blit(path, (item_pix_x, item_pix_y))
                if item == 'o':
                    window.blit(objct, (item_pix_x, item_pix_y))
                if item == 'g':
                    window.blit(guard, (item_pix_x, item_pix_y))
                item_index += 1
            line_index += 1
