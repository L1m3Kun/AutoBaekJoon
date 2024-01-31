# 25192 인사성 밝은 곰곰이
import sys
input = sys.stdin.readline


def solution():
    chat = set()
    cnt = 0
    for _ in range(int(input())):
        s = input().strip()
        if s == "ENTER":
            cnt += len(chat)
            chat.clear()
            continue
        chat.add(s)
    else:
        cnt += len(chat)
    print(cnt)
        


if __name__ == "__main__":
    solution()