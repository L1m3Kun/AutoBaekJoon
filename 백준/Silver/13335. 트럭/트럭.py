# 13335 트럭
import sys
input = sys.stdin.readline


def main():
    n, w, l = map(int, input().split())
    trucks = tuple(map(int, input().split()))

    bridge = [-1] * w
    
    weight = 0
    t = 0
    
    truck_idx = 0
    while truck_idx < n :
        if weight:
            if bridge[0] >= 0:
                weight -= trucks[bridge[0]]
                bridge[0] = -1
            for i in range( w-1):
                bridge[i] = bridge[i+1]
            bridge[-1] = -1
        
        if weight + trucks[truck_idx] <= l:
            bridge[-1] = truck_idx
            weight += trucks[truck_idx]
            truck_idx += 1
    
        t += 1
        # print(truck_idx, t)
        # print(weight)
        # print(bridge)

    additional = -1
    for i in range(w):
        if bridge[i] >= 0:
            additional = i
    
    print(t + additional+1)

    

    
        
    return


if __name__ == "__main__":
    main()