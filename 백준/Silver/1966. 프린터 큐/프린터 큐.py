import sys

for test_case in range(1, int(sys.stdin.readline().strip())+1):
    N, M = map(int, sys.stdin.readline().strip().split())
    primary = list(map(int, sys.stdin.readline().strip().split()))

    pointer = M
    count = 0

    while True:
        if primary:
            if primary[0] == max(primary):
                count += 1
                if not pointer:
                    print(count)
                    break
                else:
                    primary.pop(0)
                    if pointer:
                        pointer -= 1
                    else:
                        pointer = len(primary) - 1
            else:
                primary.append(primary.pop(0))
                if pointer:
                    pointer -= 1
                else:
                    pointer = len(primary)-1
        else:
            break

