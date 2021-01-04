import random

size = width, height = 448, 448

MAX_V = 5

DOWN, RIGHT, UP, LEFT = 0, 1, 2, 3
DOWNRIGHT, UPRIGHT, UPLEFT, DOWNLEFT = 4, 5, 6, 7

SQRT2 = 1.41

_velocity = {DOWN: [0, MAX_V],
             RIGHT: [MAX_V, 0],
             UP: [0, -MAX_V],
             LEFT: [-MAX_V, 0],
             DOWNRIGHT: [MAX_V*SQRT2/2, MAX_V*SQRT2/2],
             UPRIGHT: [MAX_V*SQRT2/2, -MAX_V*SQRT2/2],
             UPLEFT: [-MAX_V*SQRT2/2, -MAX_V*SQRT2/2],
             DOWNLEFT: [-MAX_V*SQRT2/2, MAX_V*SQRT2/2]}

class Logicstate:
    def __init__(self):
        self.players = {}

    def update_a_user(self, user, W, A, S, D):
        player = self.players[user]
        player.direction_listen(W, A, S, D)
        player.update_movement()
        
    

class Player:
    def __init__(self, world_coord = [width // 2, height//2]):
        self.x, self.y = world_coord
        self.velocity = [0,0]
        self.moving = None
        self.user = None
        self.username = None

    def update_movement(self):
        self.accelerate()
        self.update_position()

    def accelerate(self):
        if self.moving != None:
            self.velocity = _velocity[self.moving]
        else:
            self.velocity = [0,0]

    def update_position(self):
       #TODO: add boundaries so dude doesn't go off the map
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def direction_listen(self, W, A, S, D):
        if S == "1":
            if A == "1":
                self.moving = DOWNLEFT
            elif D == "1":
                self.moving = DOWNRIGHT
            else:
                self.moving = DOWN
        elif D == "1":
            if W == "1":
                self.moving = UPRIGHT
            else:
                self.moving = RIGHT

        elif W == "1":
            if A == "1":
                self.moving = UPLEFT
            else:
                self.moving = UP
            
        elif A == "1":
            self.moving = LEFT
        else:
            self.moving = None
