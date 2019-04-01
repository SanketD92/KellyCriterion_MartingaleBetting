
def KellyMartingale(game):
  bankroll = game.initialBankroll
  Bet=bankroll/10
  
  for i in range(0,len(game.result)):
          
    if bankroll < game.stopLoss:          # Stop loss triggered
      return bankroll
    
    if Bet > bankroll:
        return bankroll

    if game.result[i] == "H":
      bankroll += Bet
      Bet=bankroll/10
      
    else:
      bankroll -= Bet
      Bet *= 2      

  return bankroll