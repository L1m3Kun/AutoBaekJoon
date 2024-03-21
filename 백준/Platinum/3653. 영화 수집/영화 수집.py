# 3653 영화 수집
import sys
input = sys.stdin.readline


class SegmentTree:

    def __init__(self, N:int, M:int) -> None:
        self.tree = [0 for _ in range((N+M) << 1)]
        self.M = M
        self.N = N
        self.index = [0 for _ in range(self.N)]
        self.build()
        return
    
    def build(self):
        for i in range(self.N):
            self.tree[i+(self.M<<1)+ self.N] = 1
            self.index[i] = i + (self.M<<1)+ self.N

        for i in range(self.N+self.M-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[(i<<1)+1]
        
        return
    
    def update(self, idx:int, val:int) -> None:
        self.tree[idx] = val
        idx >>= 1
        while idx:
            self.tree[idx] = self.tree[idx<<1] + self.tree[(idx<<1)+1]
            idx >>= 1

        return
    

    def query(self, end:int) -> int:
        start = self.N + self.M
        result = 0
        while start < end:
            if start & 1:
                result += self.tree[start]
                start += 1
            
            if end & 1:
                end -= 1
                result += self.tree[end]
            
            start >>= 1
            end >>= 1
        
        return result
    
    def set_index(self, idx:int, val:int) -> None:
        self.index[idx] = val
        return
    
    def get_index(self, idx:int) -> int:
        return self.index[idx]


def main():
    N, M = map(int, input().split())
    ST = SegmentTree(N, M)
    orders = tuple(map(int, input().split()))
    for m in range(M):
        q = orders[m]
        print(ST.query(ST.get_index(q-1)), end=" ")
        ST.update(ST.get_index(q-1), 0)
        ST.update(N+(M<<1)-1-m, 1)
        ST.set_index(q-1, N+(M<<1)-1-m)
    print()
    return



if __name__ == "__main__":
    for _ in range(int(input())):
        main()