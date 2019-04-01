from playHands import playHands
from PrintEngine import PrintEngine
from KellyMartingale import KellyMartingale

class Game:
  result = []
  Min = 15
  Max = 200
  stopLoss = 50
  target = 5*Max
  BRs = []
  N = 5        # Rounds (or hands) played
  iterations = 1000  # Number of simulations to average out probabilities
  initialBankroll = 200

if __name__=='__main__':
  game = Game()
  
  for i in range (0,game.iterations):
    game.result=[]
    game.result=playHands(game)  # Giving the player a 49% chance to win  
    bankroll = round(KellyMartingale(game))
    game.BRs.append(bankroll)

  PrintEngine(game)