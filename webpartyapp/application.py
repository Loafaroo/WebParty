from flask import Flask, request
import random

from logicstate import Logicstate, Player, width, height, MAX_V, DOWN, RIGHT, UP, LEFT, DOWNRIGHT, UPRIGHT, UPLEFT, DOWNLEFT, SQRT2, _velocity 

app = Flask(__name__)

ls = Logicstate()

@app.route("/")
def NewPlayer():
    new_player = Player()

    user_assigned = False
    while not user_assigned:
        new_user = str(random.randint(1,999))
        user_assigned = True
        for user in ls.players:
            if new_user == user:
                user_assigned = False

    new_player.user = new_user

    ls.players[new_user] = new_player

    ls.players[new_user].username = request.args.get("name")

    return new_user
    

@app.route("/update")
def update():
    user = request.args.get("user")
    W = request.args.get("W")
    A = request.args.get("A")
    S = request.args.get("S")
    D = request.args.get("D")

    ls.update_a_user(user, W, A, S, D)

    key_params = {"player_x" : ls.players[user].x,
                  "player_y" : ls.players[user].y,
                 }

    return key_params
    
    

app.run()
