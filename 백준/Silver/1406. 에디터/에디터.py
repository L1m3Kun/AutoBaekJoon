# 1406 에디터
import sys
input = sys.stdin.readline

str_stack = list(input().strip())
# print("string is", str_stack)
stack = []
def L():
    global str_stack
    # print("L", place)
    stack.append(str_stack.pop())
    return

def D():
    global str_stack, stack
    # print("D", place)
    str_stack.append(stack.pop())
    return

def B():
    global str_stack
    # print("B", place)
    if not str_stack:
        return
    # string.pop(place-1)
    str_stack.pop()
    return

def P(character):
    global str_stack
    # print("P, character = ", character, place)
    str_stack.append(character)
    return 


# print("Place is ", place)
for _ in range(int(input())):
    order = list(input().strip().split())
    if order[0] == "L" and str_stack:
        L()
    elif order[0] == "D" and stack:
        D()
    elif order[0] == "B" and str_stack:
        B()
    elif order[0] == "P":
        P(order[1])
    # print("String is", str_stack, "\nstack is", stack)
# print("".join(string))
print("".join(str_stack)+"".join(stack[::-1]))
        