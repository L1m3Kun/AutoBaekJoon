# Check 배열
import sys

def check(start, j, end):
    if col[j] or di[start + j] or dj[end - j + start -1]:
        return 0
    else:
        return 1

def queen(start, end):
    if start == end:
        global count
        count += 1
        return
    else:
        for j in range(end):
            if check(start, j, end):
                col[j] = 1
                di[start + j] = 1
                dj[end-1+start-j] = 1
                queen(start+1, end)
                col[j] = 0
                di[start + j] = 0
                dj[end - 1 + start - j] = 0
        return


N = int(sys.stdin.readline().strip())
count = 0
col = [0] * N
di = [0] * (2*N -1)
dj = [0] * (2*N -1)
queen(0,N)
print(count)