'''
정점번호 1 ~ (V)
정점수
부모-자식순
5
1 2 1 3 3 4 3 5
'''

def preorder(n):            # 전위 순회
    if n:
        print(n, end=' ')   # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):             # 중위 순회
    if n:
        inorder(ch1[n])
        print(n, end=' ')   # visit(n)
        inorder(ch2[n])

def postorder(n):           # 후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')   # visit(n)


V = int(input())
arr = list(map(int, input().split()))
E = V - 1
root = 1                                # 루트 번호 1

# 부모를 인덱스로 자식번호 저장
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]         # 부모, 자식 번호
    if ch1[p] == 0:                     # 아직 자식이 없으면
        ch1[p] = c                      # 자식 1에 저장
    else:                               # 자식 1에 자식이 있으면
        ch2[p] = c                      # 자식 2에 저장

preorder(root)                          # 1 2 3 4 5
print()
inorder(root)                           # 2 1 4 3 5
print()
postorder(root)                         # 2 4 5 3 1