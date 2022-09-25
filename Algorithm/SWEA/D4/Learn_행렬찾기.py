import sys
sys.stdin = open('testcase/행렬찾기_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                cnt_r = 1
                cnt_c = 1
                cover = 1
                # 오른쪽 # 열 검사
                while True:
                    ri = i
                    rj = j + 1 * cover
                    cover += 1
                    if 0 <= ri < n and 0 <= rj < n:
                        if arr[ri][rj]:
                            cnt_r += 1
                        else:
                            break
                    else:
                        break
                # 아래 # 행검사
                cover = 1
                while True:
                    ci = i + 1 * cover
                    cj = j
                    cover += 1
                    if 0 <= ci < n and 0 <= cj < n:
                        if arr[ci][cj]:
                            cnt_c += 1
                        else:
                            break
                    else:
                        break

                result.append((cnt_c, cnt_r))

                for r in range(cnt_c):       # 검사한 부분행렬은 0 으로 만듬
                    for c in range(cnt_r):
                        arr[i+r][j+c] = 0

    ans = sorted(result, key = lambda x: (x[0]*x[1], x[0]))  # 곱을 기준으로 정렬
    num = len(ans)
    print(f'#{tc+1} {num}',end=' ')
    for k in range(num):
        print(*ans[k], end=' ')
        # print(ans[k][0], ans[k][1], end=' ')
    print()
