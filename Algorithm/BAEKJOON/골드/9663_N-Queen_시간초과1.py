def diagonal(idx):                  # 대각선 길 탐색
    dia = []
    for k in range(1, idx+1):            # 위쪽 대각선 탐색
        for d in [[-1, -1], [-1, 1]]:
            ni = idx + d[0] * k
            nj = arr[idx] + d[1] * k
            if 0 <= ni < n and 0 <= nj < n:
                dia.append((ni,nj))
    return dia

def judge(idx):                    # 퀸이 존재 가능한 위치인지 탐색
    for j in range(idx):
        if arr[j] == arr[idx]:      # 같은 열, 대각선 탐색
            return 0
        elif (j, arr[j]) in diagonal(idx):
            return 0
    return 1

def dfs(idx):                       # 행 번호
    global cnt
    if idx != n:                    # 마지막 행에 도착 안했을 때
        for i in range(n):          # 열 경우의 수
            arr[idx] = i
            if judge(idx):
                dfs(idx+1)
    else:
        cnt += 1
        return

n = int(input())
arr = [0] * n           # 인덱스는 행, 원소는 열번호
cnt = 0
dfs(0)
print(cnt)