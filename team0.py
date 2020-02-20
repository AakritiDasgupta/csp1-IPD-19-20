####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
team_name = 'E0'
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always colludes.
    return 'c'
    
team_name = 'Team 0'
strategy_name = 'Betray but retaliate'
strategy_description = 'Always betray but collude if last round player colludes.'
    
def move(my_history, their_history, my_score, their_score):
  if my_history == 0:
    return 'b'
  elif my_history[-1]== 'b' and their_history[-1]== 'c':
    return 'c'
  else:
    return 'b'
team_name = 'E0'
strategy_name = 'Random Betray '
strategy_description = 'use the random function to randomly choose c or b'

import random   
def move(my_history, their_history, my_score, their_score):
  roll = random.randint(1,50)
  if roll % 2 == 0:
    return 'c'
  else:
    return 'b'


team_name = 'E0'
strategy_name = 'collude but retaliate in odd way'
strategy_description = 'collude but if betrayed wait 1 turn then betray'

def move(my_history, their_history, my_score, their_score): 
  if my_history == 0:
    return 'c'
  elif my_history[-1]=='c' and their_history[-1]=='b':
    return 'c' 
  elif my_history[-1]== 'c'and their_history[-1]== 'c':
    return 'c'
  else:
    return 'b'
    '''
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.'''