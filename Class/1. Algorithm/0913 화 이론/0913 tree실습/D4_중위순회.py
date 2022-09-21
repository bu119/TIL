import sys
sys.stdin = open('testcase/input_중위.txt')

def inorder_traverse(v):
    global last
    if v <= last:  # 마지막 정점번호 이내
        inorder_traverse(2 * v)  # 왼쪽 자식정점 방문
        print(tree[v], end='')
        inorder_traverse(2 * v + 1)  # 오른쪽 자식정점 방문

for tc in range(10):
    n = int(input())
    last = n
    tree = [0] * (n+1)  # 완전이진트리
    for i in range(n):
        idx, *tmp = input().split()
        tree[int(idx)] = tmp[0]
    print(f'#{tc+1}', end=' ')
    inorder_traverse(1)
    print()