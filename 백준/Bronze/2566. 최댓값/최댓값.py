arr = []

for idx in range(9):
    arr.append(list(map(int, input().split())))
max = 0

for length in range(9):
    for width in range(9):
        if arr[length][width] >= max:       # 최대값 찾기
            max = arr[length][width]
            max_len = length + 1            # 열 저장
            max_wid = width + 1             # 행 저장
print(f'{max}\n{max_len} {max_wid}')
