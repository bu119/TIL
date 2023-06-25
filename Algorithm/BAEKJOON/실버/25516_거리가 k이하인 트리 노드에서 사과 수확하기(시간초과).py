import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, k = map(int, input().split())
ch1 = [0] * n
ch2 = [0] * n
for _ in range(n-1):
    p, c = map(int, input().split())
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

apple = list(map(int,input().split()))
cnt = 0
# print(ch1)
# print(ch2)

def preorder(root, floor):
    global cnt

    if floor <= k:
        # print(root, apple[root])
        cnt += apple[root]
        preorder(ch1[root], floor+1)
        preorder(ch2[root], floor+1)

preorder(0, 0)
print(cnt)