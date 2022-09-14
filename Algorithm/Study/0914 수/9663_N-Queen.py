def judge(idx):                     # 퀸이 존재 가능한 위치인지 탐색
    for j in range(idx):            # 새로운 퀸의 공격 범위를 이미 존재하는 퀸의 위치와 비교
        if arr[j] == arr[idx]:      # 같은 열 탐색
            return 0
        elif idx - j == arr[idx] - arr[j] or idx - j == -(arr[idx] - arr[j]): # 대각선 탐색 (각 행과 열의 차이가 같으면 대각선에 존재)
            return 0
    return 1

def dfs(idx):                       # 행 번호
    global cnt
    if idx != n:                    # 마지막 행에 도착 안했을 때
        for i in range(n):          # 열 경우의 수
            arr[idx] = i
            if judge(idx):          # 현재 행의 가능한 열 위치가 존재하면
                dfs(idx+1)          # 다음 행의 열 위치 결정
    else:                           # 마지막 행에 도착하면
        cnt += 1                    # 카운트
        return

n = int(input())
arr = [0] * n           # 인덱스는 행, 원소는 열번호
cnt = 0
dfs(0)
print(cnt)