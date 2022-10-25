import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        cur_node.data = string

    def search(self, string):
        cur_node = self.head

        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False

        if cur_node.data:
            return True
        else:
            return False

N, M = map(int, input().split())

trie = Trie()
for _ in range(N):
    trie.insert(input().rstrip())

count = 0
for _ in range(M):
    if trie.search(input().rstrip()):
        count += 1

print(count)
