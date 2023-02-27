def dfs(ss, bb, idx):
    global ans

    # 차이
    diff = abs(ss-bb)

    if ans > diff and bb > 0:
        ans = diff

    if idx == n-1:
        return

    idx += 1
    # 재료 추가
    dfs(ss * s_taste[idx], bb + b_taste[idx], idx)
    # 추가 안함
    dfs(ss, bb, idx)


n = int(input())
s_taste = []
b_taste = []
for _ in range(n):
    s, b = map(int,input().split())
    s_taste.append(s)
    b_taste.append(b)

# 최대 차이
ans = 1000000000
# 곱과 합의 항등원 1, 0
dfs(1, 0, -1)

print(ans)