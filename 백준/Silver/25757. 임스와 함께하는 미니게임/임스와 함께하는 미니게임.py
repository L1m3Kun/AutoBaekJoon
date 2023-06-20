import sys
input = sys.stdin.readline
N, GameType = input().strip().split()
players= {input().strip() for _ in range(int(N))}
player_num = len(players)
print(player_num if GameType == 'Y' else player_num//2 if GameType == 'F' else player_num//3)