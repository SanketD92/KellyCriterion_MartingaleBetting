import statistics
import collections

def PrintEngine(game):
  print()
  bankrollFinalCounts = collections.OrderedDict(sorted(collections.Counter(game.BRs).items()))
  print ("BR : Count")
  for key in bankrollFinalCounts.keys():
    print (str(key) + " : " + str(bankrollFinalCounts.get(key)))
  print()
  print("Median bankroll " + str(statistics.median(game.BRs)))
  print("Mode bankroll " + str(statistics.mode(game.BRs)))
  print()
  print("Bankroll above initial " + 
  str(round(sum(1 for i in game.BRs if i > game.initialBankroll)*100/game.iterations)) + "%")
  print("Bankroll risk of ruin " + 
  str(round(sum(1 for i in game.BRs if i < game.Min)*100/game.iterations)) + "%")
  print()
  print("Minimum " + str(min(game.BRs)) + "   Maximum " + str(max(game.BRs)))
  print()