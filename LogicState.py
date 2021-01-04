#### LOGICSTATE FOR WEBPARTY CLIENT ####

import sys, os
import pygame
from pygame.locals import *
import numpy as np
import math
from PIL import Image
import time
import requests

size = width, height = 448, 448
black = 0, 0, 0
white = 255, 255, 255

background = 0, 140, 178

DOWN, RIGHT, UP, LEFT = 0, 1, 2, 3
DOWNRIGHT, UPRIGHT, UPLEFT, DOWNLEFT = 4, 5, 6, 7

SQRT2 = 1.41

MAX_V = 5

_velocity = {DOWN: [0, MAX_V],
             RIGHT: [MAX_V, 0],
             UP: [0, -MAX_V],
             LEFT: [-MAX_V, 0],
             DOWNRIGHT: [MAX_V*SQRT2/2, MAX_V*SQRT2/2],
             UPRIGHT: [MAX_V*SQRT2/2, -MAX_V*SQRT2/2],
             UPLEFT: [-MAX_V*SQRT2/2, -MAX_V*SQRT2/2],
             DOWNLEFT: [-MAX_V*SQRT2/2, MAX_V*SQRT2/2]}

class Player():
    def __init__(self, world_coordinate = [width // 2, height // 2]):
        self.X, self.Y = world_coordinate
        self.velocity = [0,0]
        self.moving = None

        self.user = None
        self.username = None
        
class LogicState():
    #A state should have at least three methods: handle its own events, update the game world, and draw something different on the screen
    def __init__(self, Player, screen):
        
        self.Player = Player
        self.screen = screen

        self.gameState = 'login'
        self.loginText = "Name"

    def CreateLoginText(self):
        text = self.loginText
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if self.gameState == 'login':
                    if event.key == K_BACKSPACE:
                        if len(text)>0:
                            text = text[:-1]
                    elif event.key == K_RETURN:
                        self.gameState = 'confirm'
                    elif len(text) < 15:
                        text += event.unicode

                    

                elif event.key == K_RETURN:
                    if self.gameState == 'confirm':
                        self.gameState = 'lobby'
                    elif self.gameState == 'lobby':
                        self.gameState = 'play'

                elif event.key == K_ESCAPE:
                    if self.gameState == 'confirm':
                        self.gameState = 'login'
                    
        self.loginText = text

    """
    Main Loop
    """
    def event_listen(self):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                quit()
                pygame.quit()
        
                
    def update_logic_state(self):
        keys = pygame.key.get_pressed()

        key_params = {'user' : self.Player.user,
                       'W':keys[ord('w')],
                       'S':keys[ord('s')],
                       'A':keys[ord('a')],
                       'D':keys[ord('d')]
                       }

        

        r = requests.get('http://127.0.0.1:5000/update', key_params)

        self.Player.X = r.json()['player_x']
        self.Player.Y = r.json()['player_y']

        

    def Draw(self):        
        self.Draw_Player()
                
    def Draw_Player(self):
        new_rect = pygame.Rect(self.Player.X, self.Player.Y, 5, 5)
        pygame.draw.rect(self.screen, white, new_rect)


def main():
    pass
if __name__ == "__main__":
    main()
