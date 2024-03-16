# 2042 구간 합 구하기
import sys
input = sys.stdin.readline


class SegmentTree:
    def __init__(self, arr:list) -> None:
        self.segment_tree = [0] * (2* len(arr))
        self.N = len(arr)
        self.build(arr)
        return
    
    def build(self, arr:list) -> None:
        # N ~ 2N-1 : 입력받은 array 값 삽입
        for i in range(self.N):
            self.segment_tree[i+self.N] = arr[i]
        
        # 1 ~ N-1 : 각 인덱스 i * 2(left), i*2+1(right)를 더한 값 입력
        for i in range(self.N-1, 0, -1):
            self.segment_tree[i] = self.segment_tree[i<<1]+self.segment_tree[(i<<1)+1]
                
        return
    
    def update(self, idx:int, val:int) -> None:
        # 값 변경
        self.segment_tree[idx+self.N] = val
        
        # 연결되어 있는 노드들 모두 변경
        i = (idx+self.N) >> 1
        while i:
            self.segment_tree[i] = self.segment_tree[i<<1] + self.segment_tree[(i<<1)+1]
            i >>= 1
        return
    
    def find(self, start:int, end:int) -> int:
        start, end = start+self.N-1, end+self.N
        result = 0
        while start < end:
            if start & 1:
                result += self.segment_tree[start]
                start += 1
            if end & 1:
                end -= 1
                result += self.segment_tree[end]
            start >>= 1
            end >>= 1
                
        return result

def solution():
    N, M, K = map(int, input().split())
    sequence = [int(input()) for _ in range(1, N+1)]
    ST = SegmentTree(sequence)
    for _ in range(M+K):
        a, b, c = map(int, input().split())
        if a & 1:
            # 1인 경우
            ST.update(b-1, c)
        else:
            # 2인 경우
            print(ST.find(b, c))
    return


if __name__ == "__main__":
    solution()
