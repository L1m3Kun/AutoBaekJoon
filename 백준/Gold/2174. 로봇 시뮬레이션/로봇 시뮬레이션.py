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



'''
def main():
    # input
    A, B = map(int, input().split())
    N, M = map(int, input().split())
    robots = [0]
    locations = set()
    robot_index = {}

    for i in range(N):
        robot = input().strip().split()
        robot[0] = int(robot[0])
        robot[1] = int(robot[1])
        robot_index[tuple(robot[:2])] = i+1
        locations.add(tuple([*robot[:2]]))
        robots.append(robot)
    

    def isCrash(robot_idx, candi, candj):
        if not (0 < candi <= A) or not (0 < candj <= B):
            # print(candi, candj)
            print(f'Robot {robot_idx} crashes into wall')
            return 1
        

        if (candi, candj) in locations:
            print(f'Robot {robot_idx} crashes into robot {robot_index[(candi, candj)]}')
            return 1
        else:
            locations.discard(tuple([*robots[robot_idx][:2]]))
            locations.add((candi,candj))
            robot_index.pop(tuple(robots[robot_idx][:2]))
            robot_index[(candi,candj)] = r
        

        return 0

    def turn(order, now, repeat):
        repeat %= 4
        tmp = ["E","S", "W", "N"]
        if now == "E":
            now = 0
        elif now == "S":
            now = 1
        elif now == "W":
            now = 2
        else:
            now = 3

        if order == "L":
            repeat = 4- repeat    
        now += repeat
        now %= 4

        return tmp[now]


    def walk(i,j,d):
        if d == "E":
            return (i+1, j)
        elif d == "N":
            return (i, j+1)
        elif d == "W":
            return (i-1, j)
        else:
            return (i, j-1)
            
    orders = [tuple(input().strip().split()) for _ in range(M)]
    for t in range(M):
        r, order, repeat = orders[t]
        r, repeat = map(int, [r, repeat])

        candi, candj, candd = robots[r]
        if order == "F":
            for i in range(repeat):
                candi, candj = walk(candi, candj, candd)
                if isCrash(r, candi, candj):
                    return
        else:
            candd = turn(order, candd, repeat)
        
        robots[r][0], robots[r][1], robots[r][2] = candi, candj,candd
        

    else:
        print('OK')

    return 


if __name__ == "__main__":
    main()
'''