import sys
sys.stdin = open('testcase/input_subtree.txt')

def inorder_traverse(n):
    if n:
        return inorder_traverse(ch1[n]) + 1 + inorder_traverse(ch2[n])
    else:
        return 0

t = int(input())
for tc in range(t):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    ch1 = [0] * (E + 2)                 # 노드 번호는 1번부터 E+1번까지 존재
    ch2 = [0] * (E + 2)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:                 # 아직 자식이 없으면
            ch1[p] = c
        else:
            ch2[p] = c

    print(f'#{tc+1} {inorder_traverse(int(N))}')