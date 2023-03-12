import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip().split()) for _ in range(N)]

def preorder(spot):
    if spot in tree.keys():
        print(spot, end='')
        preorder(tree[spot][0])
        preorder(tree[spot][1])
    return

def inorder(spot):
    if spot in tree.keys():
        inorder(tree[spot][0])
        print(spot, end='')
        inorder(tree[spot][1])
    return

def postorder(spot):
    if spot in tree.keys():
        postorder(tree[spot][0])
        postorder(tree[spot][1])
        print(spot, end='')
    return

tree = {}
for i in range(N):
    for j in range(1, 3):
        if arr[i][0] not in tree.keys():
            tree[arr[i][0]] = list(arr[i][j])
        else:
            tree[arr[i][0]].append(arr[i][j])
preorder('A')
print()
inorder('A')
print()
postorder('A')