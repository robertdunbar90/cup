class team:
  def __init__(self, team):
    self.team = team
    self.rank = ranks[team] 
    self.points = 0

  def won(self, points):
    self.points += points 

class group:
  def __init__(self, name, a, b, c, d):
    self.name = name
    self.teams = [a, b, c, d]

  def __eq__(self, other):
    return self.name == other.name

  def __hash__(self):
    return hash(self.name)

  def play_game(self, a, b):
    winner, loser = play(self.teams[a], self.teams[b])
    winner.won(winner.rank - loser.rank)
  
  def play_group(self, games):
    for game in games:
      self.play_game(game[0], game[1])
    self.teams = sorted(self.teams, key=lambda team: -team.points) 

  def print_group(self):
    for team in self.teams:
      print team.team, team.rank, team.points
    
def play(a, b):
  print a.team, a.rank, " vs. ", b.team, b.rank
  if (a.rank > b.rank):
    print a.team, "wins"
    return a, b
  print b.team, "wins"
  return b, a

f = open('ranks', 'r')

ranks = {}

for line in f:
  split = line.split(",")
  rank = 0
  for i in split[1:]:
    rank += float(i)
  ranks[split[0]] = 24 - rank/len(split[1:])

for a, b in ranks.iteritems():
  print a, b


hungary = team("hungary")
albania = team("albania")
slovakia = team("slovakia")
romania = team("romania")
ukraine = team("ukraine")
ni = team("ni")
switzerland = team("switzerland")
turkey = team("turkey")
cr = team("cr")
roi = team("roi")
iceland = team("iceland")
sweden = team("sweden")
russia = team("russia")
wales = team("wales")
poland = team("poland")
croatia = team("croatia")
austria = team("austria")
england = team("england")
portugal = team("portugal")
italy = team("italy")
belgium = team("belgium")
spain = team("spain")
france = team("france")
germany = team("germany")

seed1 = [spain, germany, england, portugal, belgium]
seed2 = [italy, russia, switzerland, austria, croatia, ukraine]
seed3 = [cr, sweden, poland, romania, slovakia, hungary]
seed4 = [turkey, roi, iceland, wales, albania, ni]

A = group("A", albania, france, romania, switzerland)
A.play_group([[1,2],[0,3],[2,3],[0,1],[0,2],[1,3]])

B = group("B", england, russia, slovakia, wales)
B.play_group([[2,3],[0,1],[1,2],[0,3],[1,3],[0,2]])

C = group("C", germany, ni, poland, ukraine)
C.play_group([[1,2],[0,3],[1,3],[0,2],[0,1],[2,3]])

D = group("D", croatia, cr, spain, turkey)
D.play_group([[0,3],[1,2],[0,1],[2,3],[0,2],[1,3]])

E = group("E", belgium, italy, roi, sweden)
E.play_group([[2,3],[0,1],[1,3],[0,2],[1,2],[0,3]])

F = group("F", austria, hungary, iceland, portugal)
F.play_group([[0,1],[2,3],[1,2],[0,3],[1,3],[0,2]])

groups = [A,B,C,D,E,F]
teams = []

for group in groups:
  group.print_group()
  print
  for team in group.teams:
    teams.append(team)

third_place = []

for group in groups:
  third_place.append(group.teams[2])

third_place = sorted(groups, key=lambda group: -group.teams[2].points)

third_set = set(third_place[:4])

third = []

if third_set == set([A,B,C,D]):
  third = [C,D,A,B]
elif third_set == set([A,B,C,E]): 
  third = [C,A,B,E]
elif third_set == set([A,B,C,F]):
  third = [C,A,B,F]
elif third_set == set([A,B,D,E]):
  third = [C,A,B,E]
elif third_set == set([A,B,D,F]):
  third = [D,A,B,F]
elif third_set == set([A,B,E,F]):
  third = [E,A,B,F]
elif third_set == set([A,C,D,E]):
  third = [C,D,A,E]
elif third_set == set([A,C,D,F]):
  third = [C,D,A,F]
elif third_set == set([A,C,E,F]):
  third = [C,A,F,E]
elif third_set == set([A,D,E,F]):
  third = [D,A,F,E]
elif third_set == set([B,C,D,E]):
  third = [C,D,B,E]
elif third_set == set([B,C,D,F]):
  third = [C,D,B,F]
elif third_set == set([B,C,E,F]):
  third = [E,C,B,F]
elif third_set == set([B,D,E,F]):
  third = [E,D,B,F]
elif third_set == set([C,D,E,F]):
  third = [C,D,F,E]
else:
  print "######### NO ###########"

print
print "Knockout round"
print

qf1 = play(A.teams[1], C.teams[1])
qf2 = play(D.teams[0], third[3].teams[2])
qf3 = play(B.teams[0], third[1].teams[2]) 
qf4 = play(F.teams[0], E.teams[1])
qf5 = play(C.teams[0], third[2].teams[2])
qf6 = play(E.teams[0], D.teams[1])
qf7 = play(A.teams[0], third[0].teams[2])
qf8 = play(B.teams[1], F.teams[1])

print
print "Quarter Finals"
print

sf1 = play(qf1[0], qf2[0])
sf2 = play(qf3[0], qf4[0])
sf3 = play(qf5[0], qf6[0])
sf4 = play(qf7[0], qf8[0])

print
print "Semi finals"
print

f1 = play(sf1[0], sf2[0])
f2 = play(sf3[0], sf4[0])

print
print "Finals"
print


winner = play(f1[0], f2[0])

print "seed 1"
for team in sorted(seed1, key=lambda team: team.points):
  print team.team, team.rank, team.points

print
print "seed 2"
for team in sorted(seed2, key=lambda team: team.points):
  print team.team, team.rank, team.points

print
print "seed 3"
for team in sorted(seed3, key=lambda team: team.points):
  print team.team, team.rank, team.points

print
print "seed 4"
for team in sorted(seed4, key=lambda team: team.points):
  print team.team, team.rank, team.points
