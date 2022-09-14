def snake():
    time = 0                # 시간
    posi = [(0,0)]          # 뱀 위치
    row = col = 0           # 뱀 머리 좌표
    idx = 0                 # 4방향 탐색할 인덱스
    r = di[0]               # 이동 할 행 방향
    c = dj[0]               # 이동 할 열 방향
    flag = 1
    while flag:
        if sec:
            for z in range(sec.pop(0)):
                row += r
                col += c
                time += 1
                if 0 <= row < n and 0 <= col < n and (row, col) not in posi: # 벽체크, 자신과 안만남
                    pass
                else:
                    flag = 0
                    break

                if board[row][col]:         # 사과
                    board[row][col] = 0     # 먹어서 없어짐
                    posi.append((row, col)) # 머리 넣기
                else:
                    posi.pop(0)             # 새로운 꼬리 넣기
                    posi.append((row, col))

            if flag == 0:
                break

            if dire.pop(0) == 'D':          # 방향 결정
                idx = (idx + 1) % 4
                r = di[idx]
                c = dj[idx]
            else:
                idx = (idx - 1) % 4
                r = di[idx]
                c = dj[idx]
            # print(r,c)
        else:                   # 방향 전환이 끝나고 벽 or 몸에 닿을 때 까지
            row += r
            col += c
            time += 1
            if 0 <= row < n and 0 <= col < n and (row, col) not in posi:  # 벽체크, 자신과 안만남
                pass
            else:
                flag = 0
                break

            if board[row][col]:  # 사과
                board[row][col] = 0  # 먹어서 없어짐
                posi.append((row, col))  # 머리 넣기
            else:
                posi.pop(0)  # 새로운 꼬리 넣기
                posi.append((row, col))

    return time

n = int(input())
board = [[0]*n for _ in range(n)]
apple = int(input())
for i in range(apple):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

sec = []
dire = []
num = int(input())
for j in range(num):
    s, d = input().split()
    dire.append(d)
    sec.append(int(s))

for k in range(num-1,0,-1):
    sec[k] -= sec[k-1]

# print(sec)

di = [0, 1, 0, -1]   # 우하좌상
dj = [1, 0, -1, 0]

print(snake())