# 1135 뉴스 전하기
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    members = tuple(map(int, input().split()))
    trees = [[] for _ in range(N)]

    for idx in range(1, N):
        trees[members[idx]].append(idx)
    
    def tree_circuit(member:int) -> int:
        calls = []
        for c in trees[member]:
            calls.append(1+tree_circuit(c))

        if calls:
            calls.sort(reverse=1)
            for i in range(len(calls)):
                calls[i] += i
            return max(calls)
        return 0
    print(tree_circuit(0))
    return 


if __name__ == "__main__":
    main()
