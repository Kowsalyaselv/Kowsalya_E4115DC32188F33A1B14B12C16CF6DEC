class player:
  def play(self):
    print('The player is playing circket')
class Batsman(player):
  def play(self):
    print('The batsman is batting')
class Bowler(player):
  def play(self):
    print('The bowler is bowling')
p=player()
p.play()
B=Batsman()
B.play()
b=Bowler()
b.play()