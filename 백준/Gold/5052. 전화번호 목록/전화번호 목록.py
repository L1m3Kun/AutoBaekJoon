# 5052 전화번호 목록
import sys
input = sys.stdin.readline


class Node:

    def __init__(self, key:int,data=False) -> None:
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, string:str) -> bool:
        current_node = self.head
        for char in string:
            if char not in current_node.children.keys():
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            if current_node.data:
                return True
        current_node.data = True
        return False


def solution():
    number_book = Trie()
    N = int(input())
    numbers = sorted([input().strip() for _ in range(N)])
    flag = 0
    for i in range(N):
        if flag:
            continue
        if number_book.insert(numbers[i]):
            print("NO")
            flag = 1
        
    else:
        if not flag:
            print("YES")
    return 


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()