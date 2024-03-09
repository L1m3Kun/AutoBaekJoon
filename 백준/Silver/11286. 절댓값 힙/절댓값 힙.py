# 11286 절댓값 힙
import sys
input = sys.stdin.readline


class AbsoluteHeap:

    def __init__(self, N:int) -> None:
        self.tree = [0] * (2*N+2)
        self.length = 0


    def heap_sort(self, node:int) -> None:
        if node == 0:
            
            while node < self.length:
                left, right = 2*node+1, 2*node+2
                if node >= self.length:
                    break
                if left >= self.length and right >= self.length:
                    node += 1
                    
                elif left >= self.length:
                    if abs(self.tree[right]) < abs(self.tree[node]):
                        self.tree[right], self.tree[node] = self.tree[node], self.tree[right]
                    elif abs(self.tree[right]) == abs(self.tree[node]):
                        if self.tree[right] < self.tree[node]:
                            self.tree[right], self.tree[node] = self.tree[node], self.tree[right]
                    node = right
                    
                elif right >= self.length:
                    if abs(self.tree[left]) < abs(self.tree[node]):
                        self.tree[left], self.tree[node] = self.tree[node], self.tree[left]
                    elif abs(self.tree[left]) == abs(self.tree[node]):
                        if self.tree[left] < self.tree[node]:
                            self.tree[left], self.tree[node] = self.tree[node], self.tree[left]
                    node = left
                else:
                    if abs(self.tree[left]) > abs(self.tree[right]):
                        if abs(self.tree[node]) > abs(self.tree[right]) or (abs(self.tree[node]) ==  abs(self.tree[right]) and self.tree[node] > self.tree[right]):
                            self.tree[node], self.tree[right] = self.tree[right], self.tree[node]
                            node = right
                    elif abs(self.tree[left]) == abs(self.tree[right]):
                        if self.tree[left] > self.tree[right]:
                            if abs(self.tree[node]) > abs(self.tree[right]) or (abs(self.tree[node]) ==  abs(self.tree[right]) and self.tree[node] > self.tree[right]):
                                self.tree[node], self.tree[right] = self.tree[right], self.tree[node]
                                node = right
                        else:
                            if abs(self.tree[node]) > abs(self.tree[left]) or (abs(self.tree[node]) ==  abs(self.tree[left]) and self.tree[node] > self.tree[left]):
                                self.tree[node], self.tree[left] = self.tree[left], self.tree[node]
                                node = left

                    else:
                        if abs(self.tree[node]) > abs(self.tree[left]) or (abs(self.tree[node]) ==  abs(self.tree[left]) and self.tree[node] > self.tree[left]):
                            self.tree[node], self.tree[left] = self.tree[left], self.tree[node]
                            node = left
                if node != left and node != right:
                    break
                
        else:
            while node > 0:
                if node % 2:
                    root = node // 2
                else:
                    root = node // 2 - 1
                
                if abs(self.tree[root]) > abs(self.tree[node]) or (abs(self.tree[root]) == abs(self.tree[node]) and self.tree[root] > self.tree[node]):
                    self.tree[root], self.tree[node] = self.tree[node], self.tree[root]
                    node = root
                else:
                    break
                    
        return
        

    def push_num(self, num:int) -> None:
        self.tree[self.length] = num
        self.heap_sort(self.length)
        self.length += 1
        return
        
        
    def pop_num(self) -> int:
        if self.length == 0:
            return 0
        root = self.tree[0]
        self.tree[0], self.tree[self.length-1] = self.tree[self.length-1], 0
        self.length -= 1
        self.heap_sort(0)
        return root


def solution():
    N = int(input())
    AH = AbsoluteHeap(N)
    for _ in range(N):
        x = int(input())
        if x == 0:
            print(AH.pop_num())
        else:
            AH.push_num(x)
    return


if __name__ == "__main__":
    solution()