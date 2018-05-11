#! /usr/local/bin/python3
# coding utf-8
"""
Help MC Gyver to escape from the maze. for this he has to find all the
objects to neutralize the guard or else he will die!
"""

import pygame
import pygame.locals as pyl

import constants as const
import level
import character


pygame.init()
WINDOW = pygame.display.set_mode((const.WIN_SIZE, const.WIN_SIZE))
BACKGROUND = pygame.image.load(const.BACKGROUND).convert()
pygame.display.set_caption('MC Gyver Escape')
LAB = level.Labyrinth("data/level1.txt")
MCGYVER = character.Character(const.CHARACTER, LAB)
MCGYVER.image = pygame.transform.scale(MCGYVER.image, (const.SPRITE_SIZE,\
const.SPRITE_SIZE))
WINDOW.blit(BACKGROUND, (0, 0))
LAB.create_lab()
LAB.lab_object()
LAB.display_lab(WINDOW)


MAINTAIN = 1
while MAINTAIN:
    #WINDOW.blit(BACKGROUND, (0, 0))
    OBJCT_FOUND = MCGYVER.objct
    WIN = 'You Win!!'
    LOSE = 'You Lose!! MCGyver is dead man!!'
    FONT = pygame.font.SysFont("broadway", 30, bold=True, italic=False)
    LOSE_TEXT = FONT.render(LOSE, 1, (0, 0, 0))
    WIN_TEXT = FONT.render(WIN, 1, (255, 255, 255))
    GAME = 1
    while GAME:
        for event in pygame.event.get():
            if event.type == pyl.QUIT:
                GAME = 0
                MAINTAIN = 0
            if event.type == pyl.KEYDOWN:
                if event.key == pyl.K_RIGHT:
                    MCGYVER.moving('right')
                if event.key == pyl.K_LEFT:
                    MCGYVER.moving('left')
                if event.key == pyl.K_DOWN:
                    MCGYVER.moving('down')
                if event.key == pyl.K_UP:
                    MCGYVER.moving('up')
            MCGYVER.pickup_objct()
        if LAB.structure[MCGYVER.pos_y][MCGYVER.pos_x] != 'a':
            WINDOW.blit(BACKGROUND, (0, 0))
            LAB.display_lab(WINDOW)
            WINDOW.blit(MCGYVER.image, (MCGYVER.pix_x, MCGYVER.pix_y))
            pygame.display.flip()
        else:
            GAME = 0
            WINDOW.blit(BACKGROUND, (0, 0))
    if OBJCT_FOUND < 3:
        WINDOW.blit(LOSE_TEXT, (30, 210))
    else:
        WINDOW.blit(WIN_TEXT, (30, 210))
    pygame.display.flip()
