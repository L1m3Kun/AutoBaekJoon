import sys
input = sys.stdin.readline

def solution(cut_line):
  if cut_line == 1:
    return 1
  cnt = 1
  for i in range(1, N):
    if score[i] < cut_line:
      cnt += 1
      cut_line = score[i]
    if cut_line == 1:
      break
  return cnt



for test_case in range(int(input())):
  N = int(input())
  score = [0] * N
  for _ in range(N):
    idx, val = map(int, input().strip().split())
    score[idx-1] = val

  print(solution(score[0]))
  