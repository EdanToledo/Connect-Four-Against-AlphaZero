from flask import Flask, jsonify, request
import torch
from agent import AlphaZero
from Connect4 import Connect4Game
from flask_cors import CORS, cross_origin
import numpy as np

HIDDEN_SIZE=512
NUM_SIMULATIONS=1500
LEARNING_RATE=5e-4
SAVE_PATH="./AlphaZero.pt"


game = Connect4Game()

agent = AlphaZero(game,(game.rows,game.columns),HIDDEN_SIZE,game.columns,NUM_SIMULATIONS,LEARNING_RATE)

agent.load_weights(SAVE_PATH)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/act")
@cross_origin()
def act():
    
    board = eval(request.args.get('board'))
    board = np.flip(np.flip(np.array(board,dtype=np.float32)),1)
    player = eval(request.args.get('player'))
    action = agent.act(board,player)
    
    return str(action)

    
    