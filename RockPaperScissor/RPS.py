# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play="", opponent_history=[], name_history=[], my_history=[], play_order=[{"RR": 0,"RP": 0,"RS": 0,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0,}] ):
    opponent_history.append(prev_play)

    guess = "R"
    iter = len(opponent_history)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    #RESET AFTER 1000
    if iter == 1001:
      opponent_history.clear()
      opponent_history.append(prev_play)
      name_history.clear()
      name_history.append('')
      my_history.clear()

    #FIND BOT IN 3 TURNS USING ITS CODE
    if iter <= 4:

      if iter == 1:
        my_history.append("R")
        return "R"
      elif iter == 2:
        my_history.append("P")
        return "P"
      elif iter == 3:
        my_history.append("S")
        return "S"
      else:              
        opponentcode = "".join(opponent_history[-3:])
        codetobot = {"RPP": "quincy", "PPP": "abbey", "PPS": "kris", "RRR":"mrugesh"}
        opponent = codetobot[opponentcode]
        name_history.append(opponent)

    if name_history[-1] == 'quincy':
      choices = ["R", "R", "P", "P", "S"]
      next_move = choices[iter % len(choices)]
      guess = ideal_response[next_move]

    if name_history[-1] == 'abbey':
      last_two = "".join(my_history[-2:])
      if len(last_two) == 2:
          play_order[0][last_two] += 1

      potential_plays = [
          my_history[-1] + "R",
          my_history[-1] + "P",
          my_history[-1] + "S",
      ]

      sub_order = {
          k: play_order[0][k]
          for k in potential_plays if k in play_order[0]
      }

      prediction = max(sub_order, key=sub_order.get)[-1:]

      next_move = ideal_response[prediction]
      guess = ideal_response[next_move]

    if name_history[-1] == 'kris':
      next_move = ideal_response[my_history[-1]]
      guess = ideal_response[next_move]

    if name_history[-1] == 'mrugesh':
      last_ten = my_history[-10:]
      most_frequent = max(set(last_ten), key=last_ten.count)

      if most_frequent == '':
          most_frequent = "S"

      ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
      next_move = ideal_response[most_frequent]
      guess = ideal_response[next_move]

    my_history.append(guess)
    return guess
