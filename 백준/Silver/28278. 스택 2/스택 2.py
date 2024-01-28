# 28278 스택 2
import sys
input = sys.stdin.readline


class Stack:
    stack = []
    def __init__(self) -> None:
        self.stack.clear()
    
    def add_num(self, x:int):
        self.stack.append(x)
    
    def delete_num(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)
    
    def len_stack(self):
        print(len(self.stack))
    
    def is_empty(self):
        if self.stack:
            print(0)
        else:
            print(1)

    def print_top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)


def solution():
    N = int(input())
    arr = Stack()
    for _ in range(N):
        orders = list(map(int, input().split()))
        if orders[0] == 1:
            arr.add_num(orders[1])
        elif orders[0] == 2:
            arr.delete_num()
        elif orders[0] == 3:
            arr.len_stack()
        elif orders[0] == 4:
            arr.is_empty()
        elif orders[0] == 5:
            arr.print_top()

if __name__ == "__main__":
    solution()