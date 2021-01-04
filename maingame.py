
import sys, os
import pygame
from pygame.locals import *
import numpy as np
import math
from PIL import Image
from LogicState import size, black, white, background, width, height, Player, LogicState
import time
import requests

screen = pygame.display.set_mode(size)
"""
set display mode (with openGL rendering, if desired)
"""
clock = pygame.time.Clock()
framerate = 60
"""
set framerate below with clock.tick
"""
        
def DrawTitleText(textTitle = 'Enter Your Username'):
    fontSize = 24
    font = pygame.font.SysFont(None, fontSize)
    
    img = font.render(textTitle, True, white)

    img_width = img.get_rect().width
    
    screen.blit(img, (int(width/2 - img_width/2), height // 2 - 80))

def DrawWaitingText(textTitle = "Waiting for others to join", ellipsis = ""):
    fontSize = 24
    font = pygame.font.SysFont(None, fontSize)
    
    img = font.render(textTitle, True, white)

    img_width = img.get_rect().width

    img = img = font.render(textTitle + ellipsis, True, white)  
    
    screen.blit(img, (int(width/2 - img_width/2), height // 2))

def DrawNameText(text, gameState):
    fontSize = 36
    font = pygame.font.SysFont(None, fontSize)
    img = font.render(text, True, white)

    rect = img.get_rect()
    rect.topleft = (int(width/2 - rect.width/2), height // 2)
    cursor = Rect(rect.topright, (3, rect.height))
    
    screen.blit(img, rect)
    if time.time() % 1 < 0.5 and gameState == 'login':
        pygame.draw.rect(screen, white, cursor)    


def main():
    pygame.init()

    ORB = Player()    
        
    State = LogicState(ORB, screen) # the darkness on the face of the deep

    while True:
        while State.gameState == 'login':
            screen.fill(background)

            DrawTitleText()
            
            State.CreateLoginText()

            DrawNameText(State.loginText, State.gameState)
            
            pygame.display.flip()
            
            clock.tick(framerate)

        while State.gameState == 'confirm':
            screen.fill(background)

            DrawTitleText("Is this your username?")

            DrawNameText(State.loginText, State.gameState)

            State.CreateLoginText()
            
            pygame.display.flip()
            
            clock.tick(framerate)
            

        while State.gameState is 'lobby':
            if not State.Player.user:
                State.Player.username = State.loginText
                r = requests.get("http://127.0.0.1:5000/", {"name" : State.Player.username})

                State.Player.user = r.text
            
            
            screen.fill(background)

            mod = time.time() % 2

            mod = int(mod*2)

            ellipsis = "".join(["." for _ in range(mod)])

            DrawWaitingText("Waiting for other players to join", ellipsis)

            State.CreateLoginText()
            
            pygame.display.flip()
            
            clock.tick(framerate)
            pass
            
        while State.gameState is 'play':

            screen.fill(background)
            
            State.event_listen()

            State.update_logic_state()
            
            State.Draw()
                    
            pygame.display.flip()
            
            clock.tick(framerate)
        
if __name__ == "__main__":
    main()
