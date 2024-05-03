# 18429 근손실
import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    w_list = list(map(int, input().split()))

    for i in range(N):
        w_list[i] -= K

    def dfs(start):
        stack = [(set([start]), w_list[start])]
        cnt = 0
        while stack:
            visited, w = stack.pop()
            if len(visited) == N:
                if w >= 0:
                    cnt += 1
                continue
            if w < 0:
                continue
            for i in range(N):
                if not i in visited:
                    stack.append((visited.union(set([i])), w+w_list[i]))

        return cnt
    ans = 0
    for i in range(N):
        ans += dfs(i)

    print(ans)
    return 


if __name__ == "__main__":
    main()