# # 28279 덱 2
# import sys
# input = sys.stdin.readline

# class CustumDeque:
    
#     def __init__(self, max_num:int) -> None:
#         self.queue = [0]* max_num
#         self.first_index = 0
#         self.last_index = 0

#     def insert_first(self, num:int) -> None:
#         if 
#         self.queue
    
#     def insert_last(self, num:int) -> None:
#         self.queue.append(num)
    
#     def pop_first(self) -> int:
#         if not self.queue:
#             return -1
#         num = self.queue[0]
#         self.queue = self.queue[1:]
#         return num
    
#     def pop_last(self) -> int:
#         if not self.queue:
#             return -1
#         return self.queue.pop()
    
#     def length(self) -> int:
#         return len(self.queue)
    
#     def is_empty(self) -> bool:
#         return 0 if self.queue else 1
    
#     def print_first(self) -> None:
#         return self.queue[0] if self.queue else -1

#     def print_last(self) -> None:
#         return self.queue[-1] if self.queue else -1
        



# def solution():
#     N = int(input())
#     cq = CustumDeque()
    
#     for _ in range(N):
#         order, *num = map(int, input().split())
#         if order == 1:
#             cq.insert_first(*num)
#         elif order == 2:
#             cq.insert_last(*num)
#         elif order == 3:
#             print(cq.pop_first())
#         elif order == 4:
#             print(cq.pop_last())
#         elif order == 5:
#             print(cq.length())
#         elif order == 6:
#             print(cq.is_empty())
#         elif order == 7:
#             print(cq.print_first())
#         else:
#             print(cq.print_last())


# if __name__ == "__main__":
#     solution()



# 28279 덱 2
import sys
from collections import deque
input = sys.stdin.readline


def solution():
    N = int(input())
    que = deque()
    for _ in range(N):
        order, *num = map(int, input().split())
        if order == 1:
            que.appendleft(*num)
        elif order == 2:
            que.append(*num)
        elif order == 3:
            print(que.popleft() if que else -1)
        elif order == 4:
            print(que.pop() if que else -1)
        elif order == 5:
            print(len(que))
        elif order == 6:
            print(0 if que else 1)
        elif order == 7:
            print(que[0] if que else -1)
        else:
            print(que[-1] if que else -1)
            


if __name__ == "__main__":
    solution()