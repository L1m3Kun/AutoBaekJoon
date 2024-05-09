# 2174 로봇 시뮬레이션
import sys
input = sys.stdin.readline


def main():
    # input
    A, B = map(int, input().split())
    N, M = map(int, input().split())

    # input settings
    robots = [0]
    lands = set()
    indexes = {}
    for i in range(N):
        x,y,d = input().strip().split()
        x, y = int(x), int(y)
        robots.append((x,y,d))
        lands.add((x,y))
        indexes[(x,y)] = i+1

    orders = []
    for _ in range(M):
        idx, order, repeat = input().strip().split()
        orders.append((int(idx), order, int(repeat)))

    

    def isCrash(robot_idx, nx, ny):
        if nx > A or nx < 1 or ny > B or ny < 1:
            print(f"Robot {robot_idx} crashes into the wall")
            return 1
        
        if (nx, ny) in lands:
            print(f"Robot {robot_idx} crashes into robot {indexes[(nx,ny)]}")
            return 1
        
        return 0
        
    def walk(r_idx, x,y,d,repeat):
        move = {
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0),
            "N": (0, 1)
        }
        nx, ny = x, y
        is_crashed = False
        for _ in range(repeat):
            nx += move[d][0]
            ny += move[d][1]
            if isCrash(r_idx, nx, ny):
                is_crashed = True
                break
                    
        return (is_crashed, nx, ny)
    
    def turn(order, d, repeat):
        repeat %= 4
        direction = ["E", "S", "W", "N"]
        if order == "L":
            repeat = 4 - repeat
        
        if d == "E":
            d = 0
        elif d == "S":
            d = 1
        elif d == "W":
            d = 2
        else:
            d = 3
        
        d += repeat

        return direction[d % 4]
    
    # test code
    # test_oder = input().strip()
    # test_d = input().strip()
    # test_repeat = int(input())
    # print(turn(test_oder, test_d, test_repeat))

    for robot_idx, order, repeat in orders:
        x, y, d = robots[robot_idx]
        if order == "F":
            is_crashed, candx, candy = walk(robot_idx,x,y,d,repeat)
            if is_crashed:
                break
            robots[robot_idx] = (candx, candy, d)
            lands.discard((x,y))
            lands.add((candx, candy))
            indexes.pop((x,y))
            indexes[(candx, candy)] = robot_idx
        else:
            cand = turn(order, d, repeat)
            robots[robot_idx] = (x, y, cand)
    else:
        print("OK")
     

    return


if __name__ == "__main__":
    main()

