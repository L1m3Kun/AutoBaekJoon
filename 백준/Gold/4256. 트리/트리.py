import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def main():
    N = int(input())
    preorder = tuple(map(int, input().split()))
    inorder = tuple(map(int, input().split()))

    inindex = {}

    for idx, val in enumerate(inorder):
        inindex[val] = idx

    def tree(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start > preorder_end:
            return
    
        if preorder_start == preorder_end:
            print(preorder[preorder_start], end = " ")
            return
    
        root = preorder[preorder_start]
        left = inindex[root] - inorder_start
        tree(preorder_start+1, preorder_start+left, inorder_start, inindex[root]-1)
        tree(preorder_start+1+left, preorder_end, inindex[root] + 1, inorder_end)
        print(root, end =" ")
        return


    tree(0, N-1, 0, N-1)

if __name__ == "__main__":
    for _ in range(int(input())):
        main()
        print()