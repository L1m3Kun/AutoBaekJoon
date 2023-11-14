input = __import__("sys").stdin.readline

def solution(N:int, nums:set[int], M:int, numl:list[int]) -> None:
    for num in numl:
        if num in nums:
            print(1)
        else:
            print(0)
    return


if __name__ == "__main__":
    N = int(input())
    nums = set(map(int, input().split()))
    M = int(input())
    numl = list(map(int, input().split()))
    solution(N, nums, M, numl)