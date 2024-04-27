# 20044 Project Teams
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    members = sorted(list(map(int, input().split())))

    for i in range(N):
        members[i] += members[(2*N-1-i)]

    print(min(members[:N]))
    return


if __name__ == "__main__":
    main()

