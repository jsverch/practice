# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        v = b.score - a.score

        if v == 0:
            if a.name < b.name:
                return -1
            else:
                return 1
        return v


n = int(raw_input())
data = []
for i in range(n):
    name, score = raw_input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, cmp=Player.comparator)
for i in data:
    print i.name, i.score
