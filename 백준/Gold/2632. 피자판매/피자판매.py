# 2632 피자판매
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    needs = int(input())
    m, n = map(int, input().split())
    ans = 0
    A, B = [0]*m, [0]*n
    for i in range(m):
        A[i] = int(input())
    
    for i in range(n):
        B[i] = int(input())

    candidate = {
        "A": defaultdict(int),
        "B": defaultdict(int),
    }

    def makeCandidate(cand_name:str, array:list, length:int):
        cnt = 0
        fin_num = 0
        for i in range(length):
            pieces = 0
            for j in range(i, length+i):
                if j == length+i-1:
                    fin_num = pieces+array[j%length]
                    continue
                pieces += array[j%length]
                if pieces < needs:
                    candidate[cand_name][pieces] += 1
                elif pieces == needs:
                    cnt += 1
                    break
                else:
                    break
        if fin_num < needs:
            candidate[cand_name][fin_num] += 1
        elif fin_num == needs:
            cnt += 1

        return cnt

    ans += makeCandidate("A", A, m)
    ans += makeCandidate("B", B, n)

    # print(candidate, ans)

    
    for c in candidate["A"]:
        ans += candidate["B"][needs-c] * candidate["A"][c]
        
    print(ans)

    return


if __name__ == "__main__":
    main()
