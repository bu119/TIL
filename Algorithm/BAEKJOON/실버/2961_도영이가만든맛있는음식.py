def dfs(ss, bb, idx, cnt):
    global ans

    # 차이
    diff = abs(ss-bb)

    if ans > diff and cnt > 0:
        ans = diff
        if ans == 0:
            print(0)
            exit(0)

    if idx == n-1:
        return

    idx += 1
    new_s = ss * s_taste[idx]
    new_b = bb + b_taste[idx]

    # 재료 추가
    dfs(new_s, new_b, idx, cnt+1)
    # 추가 안함
    dfs(ss, bb, idx, cnt)


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
dfs(1, 0, -1, 0)

print(ans)