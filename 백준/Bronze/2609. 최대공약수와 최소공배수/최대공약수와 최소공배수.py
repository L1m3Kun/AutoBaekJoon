# 2609 최대공약수와 최소공배수
input = __import__("sys").stdin.readline


def GCD(num1: int, num2: int) -> int:
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def solution(num1: int, num2: int) -> None:
    gcd = GCD(num1, num2)
    lcm = (num1 * num2) // gcd
    print(gcd, lcm, sep="\n")


if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    solution(num1, num2)
