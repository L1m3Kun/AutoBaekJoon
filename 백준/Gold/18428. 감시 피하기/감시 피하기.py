# 18428 감시 피하기
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    classroom = []
    teacher = []
    for i in range(N):
        lines = input().strip().split()
        classroom.append(lines)
        for j in range(N):
            if lines[j] == "T":
                teacher.append((i,j))
    candi = []
    for i,j in teacher:
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            blank = []
            for k in range(1, N):
                ni, nj = i+di*k, j+dj*k
                # print(ni,nj)
                if 0 <= ni < N and 0 <= nj < N:
                    # print(classroom[ni][nj])
                    if classroom[ni][nj] == "X":
                        # print(1)
                        blank.append((ni,nj))
                    elif classroom[ni][nj] == "S":
                        if k == 1:
                            print("NO")
                            return
                        for tu in blank:
                            candi.append(tu)
                        break

                    else:
                        break
                else:
                    break
            # print(blank)

    # print(candi)
    def check(visited):
        arr = []
        for i in range(N):
            arr.append(classroom[i].copy())
        for i in visited:
            arr[candi[i][0]][candi[i][1]] = "O"
        # [print(arr[c]) for c in range(N)]
        # print()
        for i,j in teacher:
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                for k in range(N):
                    ni, nj = i+di*k, j+dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj]  ==  "S":
                            return 0
                        if arr[ni][nj] == "O":
                            break
                    else:
                        break
        return 1

    def bt(cnt, i, visited):
        if cnt == 3:
            # [print(classroom[c]) for c in range(N)]
            # print()
            # print(visited)
            if check(visited):
                # [print(classroom[c]) for c in range(N)]
                # print()
                return 1
            else:
                # [print(classroom[c]) for c in range(N)]
                # print()
                return 0

        tmp = visited.copy()
        for j in range(i+1, len(candi)):    
            tmp.append((j))
            if bt(cnt+1, j, tmp):
                return 1
            tmp.pop()
        return 0
    
    if len(candi) <= 3:
        print("YES")
    else:
        for i in range(len(candi)):
            if bt(i, -1, []):
                print("YES")
                break
        else:
            print("NO")
    return


if __name__ == "__main__":
    main()  

