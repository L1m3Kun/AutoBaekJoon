# 2775 부녀회장이 될테야
input = __import__("sys").stdin.readline


def dp_set() -> list[list[int]]:
    apart = [[0] * 15 for _ in range(15)]
    for i in range(15):
        apart[0][i] = i
    for i in range(1, 15):
        for j in range(1, 15):
            for k in range(j + 1):
                apart[i][j] += apart[i - 1][k]
    # [print(*apart[i]) for i in range(15)]
    return apart


def solution(k: int, n: int, apart: list[list[int]]) -> int:
    return apart[k][n]


if __name__ == "__main__":
    apart = dp_set()
    for _ in range(int(input())):
        print(solution(int(input()), int(input()), apart))
