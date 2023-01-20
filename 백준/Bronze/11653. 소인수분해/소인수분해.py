N = int(input())
        
if N != 1:
    while True:
        min =0
        for num in range(2,N):      # 나눠지는 수 찾기
            if N % num == 0:
                min = num
                break
        else:
            print(N)
            break
        print(min)                  
        N = int(N / num)            # 나눈 수 저장
else:
    print("")