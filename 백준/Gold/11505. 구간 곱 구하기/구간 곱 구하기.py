# 11505 구간 곱 구하기
import sys
input = sys.stdin.readline


class SegmentTree:

    def __init__(self, sequence:list) -> None:
        self.N = len(sequence)
        self.segment_tree = [0] * (2*self.N)
        self.div = 1_000_000_007
        self.build(sequence)

    def build(self, sequence:list) -> None:
        for i in range(self.N):
            self.segment_tree[i+self.N] = sequence[i]
        
        for i in range(self.N-1, 0, -1):
            self.segment_tree[i]= (self.segment_tree[i<<1]*self.segment_tree[(i<<1)+1]) % self.div

        return

    def update(self, idx:int, val:int) -> None: 
        i = idx+self.N
        self.segment_tree[i] = val
        
        i >>= 1

        while i:
            self.segment_tree[i] = (self.segment_tree[i<<1]*self.segment_tree[(i<<1)+1]) % self.div
            i >>= 1
        return
    
    
    def search(self, start:int, end:int) -> int:
        start += self.N
        end += self.N
        result = 1

        while start < end:
            if start & 1:
                result = (result * self.segment_tree[start]) % self.div
                start += 1
            if end & 1:
                end -= 1
                result = (result * self.segment_tree[end]) % self.div

            start >>= 1
            end >>= 1

        return result        


def main():
    N, M, K = map(int, input().split())
    sequence = tuple(int(input()) for _ in range(N))

    ST = SegmentTree(sequence)

    for _ in range(M+K):
        a, b, c = map(int, input().split())
        if a & 1:
            ST.update(b-1, c)
        else:
            print(ST.search(b-1, c))
    
if __name__ == "__main__":
    main()