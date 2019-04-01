import random

def RandomBetting(game):
  bankroll = game.initialBankroll
  for i in range(0,len(game.result)):
    RandomBet = random.randint(game.Min,game.Max)
    if game.result[i] == "H":
      bankroll += RandomBet
    else:
      bankroll -= RandomBet
  return bankroll