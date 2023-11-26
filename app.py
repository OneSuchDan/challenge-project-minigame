#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
import time

from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
print("hello world")

# add logic to play the game

# define a function to play the game
# add to function play API flask to add multiplayer game paper rock scissors with logic to play the game
@app.route('/play/<user_choice>')
def play(user_choice):
    # define a list of choices
    choices = ['rock', 'paper', 'scissors']
    # randomly select the computer's choice
    computer_choice = random.choice(choices)
    # determine the winner
    if user_choice == computer_choice:
        winner = 'tie'
    elif user_choice == 'rock' and computer_choice == 'paper':
        winner = 'computer'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        winner = 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        winner = 'user'
    elif user_choice == 'paper' and computer_choice == 'scissors':
        winner = 'computer'
    elif user_choice == 'scissors' and computer_choice == 'rock':
        winner = 'computer'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        winner = 'user'
    # return the results
    return """
        <html>
            <body>
                <h1>You chose {user_choice}.</h1>
                <h1>The computer chose {computer_choice}.</h1>
                <h1>The winner is {winner}.</h1>
            </body>
        </html>
    """.format(
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner
    )

# add to function play API flask to add multiplayer game paper rock scissors with logic to play the game
@app.route('/play2/<user_choice>')
def play2(user_choice):
    # define a list of choices
    choices = ['rock', 'paper', 'scissors']
    # randomly select the computer's choice
    computer_choice = random.choice(choices)
    # determine the winner
    if user_choice == computer_choice:
        winner = 'tie'
    elif user_choice == 'rock' and computer_choice == 'paper':
        winner = 'computer'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        winner = 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        winner = 'user'
    elif user_choice == 'paper' and computer_choice == 'scissors':
        winner = 'computer'
    elif user_choice == 'scissors' and computer_choice == 'rock':
        winner = 'computer'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        winner = 'user'
    # return the results
    return """
        <html>
            <body>
                <h1>You chose {user_choice}.</h1>
                <h1>The computer chose {computer_choice}.</h1>
                <h1>The winner is {winner}.</h1>
            </body>
        </html>
    """.format(
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner
    )