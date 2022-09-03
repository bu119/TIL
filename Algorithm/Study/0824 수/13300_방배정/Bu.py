n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
boy = [0] * 7                  # 학년 별 인덱스
girl = [0] * 7
for i in range(n):
    if arr[i][0]:              # 남
        boy[arr[i][1]] += 1
    else:                      # 여
        girl[arr[i][1]] += 1
cnt = 0
for j in range(7):
    if boy[j] % m:             # 나머지 있으면
        cnt += boy[j]//m + 1   # 몫에 +1
    else:
        cnt += boy[j] // m

    if girl[j] % m:
        cnt += girl[j]//m + 1
    else:
        cnt += girl[j] // m

print(cnt)