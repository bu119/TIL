import sys
sys.stdin = open("부분집합_input.txt", "r")

arr = list(range(1, 13))
size = len(arr)
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())

    ans = 0
    for i in range(1, 1 << size):  # 공집합 제외
        sum = cnt = 0
        for j in range(size):
            if i & (1 << j):
                cnt += 1
                sum += arr[j]

        if cnt == n and sum == k:
            ans += 1

    print(f'#{tc + 1} {ans}')