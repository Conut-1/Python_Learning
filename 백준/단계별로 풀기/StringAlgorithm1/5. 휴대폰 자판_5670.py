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
        count = 0

        for char in string:
            cur_node = cur_node.children[char]
            if len(cur_node.children) > 1 or cur_node.data:
                count += 1

        return count

while True:
    try:
        N = int(input())
        trie = Trie()
        words = []

        for _ in range(N):
            word = input().rstrip()
            trie.insert(word)
            words.append(word)

        press_sum = 0
        for word in words:
            press_sum += trie.search(word)

        print(f'{press_sum / len(words):.2f}')
    except:
        break
