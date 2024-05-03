# 1043 거짓말
import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    n, *is_know = map(int, input().split())
    
    parties = []
    for i in range(M):
        _, *members = map(int, input().split())
        parties.append(sorted(members))
    
    if n == 0:
        print(M)
    else:
        parent = [0] * (N+1)
        for i in range(1,N+1):
            parent[i] = i  
        
        def union(num1, num2):
            f1 = find(num1)
            f2 = find(num2)
            # print("union",f1, f2)
            if f1 != f2:
                parent[f2] = f1
            return


        def find(num):
            tmp = num
            while tmp != parent[tmp]:
                tmp = parent[tmp]
            return  tmp

        for party in parties:
            
            for person in party[1:]:
                union(party[0],person)
        
        known =set(is_know)
        for i in is_know:
            known.add(find(i))
        cnt = M
        for party in parties:
            for i in party:
                if find(i) in known:
                    cnt -=1
                    break
        print(cnt)

         
    
    return


if __name__ == "__main__":
    main()
