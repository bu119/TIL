import sys
sys.stdin = open('testcase/input_이진탐색.txt')

def inorder_traverse(v):
    global last
    global arr
    if v <= last:  # 마지막 정점번호 이내
        inorder_traverse(2 * v)  # 왼쪽 자식정점 방문
        arr.append(tree[v])
        inorder_traverse(2 * v + 1)  # 오른쪽 자식정점 방문

t = int(input())
for tc in range(t):
    n = int(input())
    tree = range(n+1)
    last = n
    arr = []
    inorder_traverse(1)
    print(arr)
    print(n//2+1, arr[n//2+1])

