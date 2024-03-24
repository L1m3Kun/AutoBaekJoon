# 9576 책 나눠주기
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    books = [[0 for _ in range(N)] for _ in range(M)]
    orders = sorted(list(tuple(map(int, input().split())) for _ in range(M)), key=lambda x:(x[1], x[0]))
    for i in range(M):
        start, end = orders[i]
        for j in range(start-1, end):
            books[i][j] = 1
    visited = set()
    # [print(books[i]) for i in range(M)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if j in visited:    # 이미 책을 받은 사람은 패스
                continue
        
            if books[j][i]:     # 희망 범위에 있으면 책 주고 다음 책 탐색
                visited.add(j)
                cnt += 1
                break
    print(cnt)
    
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        main()