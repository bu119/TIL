import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 투 포인터
cnt = n+1
ssum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end 만큼 이동시키면서 더하기
    while ssum < s and end < n:
        ssum += arr[end]
        end += 1
    # 부분합이 s 이상일 때 비교
    if ssum >= s:
        if end - start < cnt:
            cnt = end - start
    ssum -= arr[start]

if cnt == n+1:
    cnt = 0
print(cnt)
