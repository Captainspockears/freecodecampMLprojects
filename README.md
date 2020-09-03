# freecodecamp Machine Learning with Python Projects

## 1. Rock Paper Scissors

For this challenge, you will create a program to play Rock, Paper, Scissors. A program that picks at random will usually win 50% of the time. To pass this challenge your program must play matches against four different bots, winning at least 60% of the games in each match.

In the file `RPS.py` you are provided with a function called `player`. The function takes an argument that is a string describing the last move of the opponent ("R", "P", or "S"). The function should return a string representing the next move for it to play ("R", "P", or "S").

A player function will receive an empty string as an argument for the first game in a match since there is no previous play.

The file `RPS.py` shows an example function that you will need to update. The example function is defined with two arguments (`player(prev_play, opponent_history = [])`). The function is never called with a second argument so that one is completely optional. The reason why the example function contains a second argument (`opponent_history = []`) is because that is the only way to save state between consecutive calls of the `player` function. You only need the `opponent_history` argument if you want to keep track of the opponent_history.

*Hint: To defeat all four opponents, your program may need to have multiple strategies that change depending on the plays of the opponent.*

### Development

Do not modify `RPS_game.py`. Write all your code in `RPS.py`. For development, you can use `main.py` to test your code. 

`main.py` imports the game function and bots from `RPS_game.py`.

To test your code, play a game with the `play` function. The `play` function takes four arguments:
- two players to play against each other (the players are actually functions)
- the number of games to play in the match
- an optional argument to see a log of each game. Set it to `True` to see these messages.

```py
play(player1, player2, num_games[, verbose])
```
For example, here is how you would call the function if you want `player` and `quincy` to play 1000 games against each other and you want to see the results of each game:
```py
play(player, quincy, 1000, verbose=True)
```

Click the "run" button and `main.py` will run.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. If you uncomment the last line in `main.py`, the tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.

## 2. Cat and Dog Image Classifier

For this challenge, you will complete the code below to classify images of dogs and cats. You will use Tensorflow 2.0 and Keras to create a convolutional neural network that correctly classifies images of cats and dogs at least 63% of the time. (Extra credit if you get it to 70% accuracy!)

Some of the code is given to you but some code you must fill in to complete this challenge. Read the instruction in each text cell so you will know what you have to do in each code cell.

The first code cell imports the required libraries. The second code cell downloads the data and sets key variables. The third cell is the first place you will write your own code.

The structure of the dataset files that are downloaded looks like this (You will notice that the test directory has no subdirectories and the images are not labeled):
```
cats_and_dogs
|__ train:
    |______ cats: [cat.0.jpg, cat.1.jpg ...]
    |______ dogs: [dog.0.jpg, dog.1.jpg ...]
|__ validation:
    |______ cats: [cat.2000.jpg, cat.2001.jpg ...]
    |______ dogs: [dog.2000.jpg, dog.2001.jpg ...]
|__ test: [1.jpg, 2.jpg ...]
```

You can tweak epochs and batch size if you like, but it is not required.
