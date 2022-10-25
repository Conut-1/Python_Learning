import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True

    def travel(self, level, cur):
        if 0 in cur:
            return

        cur_children = sorted(cur)

        for child in cur_children:
            print("--" * level + child)
            self.travel(level + 1, cur[child])

N = int(sys.stdin.readline().strip())
nest = Trie()
for _ in range(N):
    input_line = input().split()
    K = input_line[0]
    foods = input_line[1:]
    nest.add(foods)
nest.travel(0, nest.root)
