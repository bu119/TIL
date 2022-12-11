'''
정점번호 1 ~ (V)
정점수
부모-자식순
5
1 2 1 3 3 4 3 5
'''

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i


V = int(input())
arr = list(map(int, input().split()))
E = V - 1

# 자식을 인덱스로 부모 번호 저장
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]         # 부모, 자식 번호
    par[c] = p


root = find_root(V)
print(root)