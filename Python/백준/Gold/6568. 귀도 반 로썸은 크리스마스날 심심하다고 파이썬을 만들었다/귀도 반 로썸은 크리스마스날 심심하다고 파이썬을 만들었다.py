# 6568 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다
import sys
input = sys.stdin.readline


while True:
    try :
        memory = list(int(input().strip(), 2) for _ in range(32))
    except: 
        break
    

    PC, adder = 0, 0


    while True:
        order, address = memory[PC] // 32, memory[PC] % 32

        PC = (PC+1) % 32

        if order == 3:
            continue

        elif order == 0:
            memory[address] = adder
            
        elif order == 1:
            adder = memory[address]
            
        elif order == 2:
            if not adder:
                PC = address
            
        elif order == 4:
            adder = (adder-1) % 256
            
        elif order == 5:
            adder = (adder+1) % 256
            
        elif order == 6:
            PC = address
            
        else:
            break

    print(bin(adder)[2:].zfill(8))