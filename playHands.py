import random

def playHands(game):
  result = []
  for i in range(game.N):
    coin = random.randint(0,100)
    if coin<50:       # 49-51 probability distribution
      result.append('H')  # Heads is a player's winning round (or hand)
    else:
      result.append('T')  # Tails is a player's losing round (or hand)
  return result
