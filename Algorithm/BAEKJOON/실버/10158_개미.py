w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

row = p + time
col = q + time

# 벽에 부딪혀 바뀌는 방향 수
turn_r = row // w
turn_c = col // h

if turn_r % 2 == 0:                 # 짝수 번 바뀔 때 오른쪽으로 증가 (좌우 변화)
    if not turn_c % 2:              # 짝수 번 바뀔 때 위로 증가 (아래위 변화)
        print(row % w, col % h)
    else:                           # 홀수 번 바뀔 때 아래로 감소
        print(row % w, h - col % h)
else:                               # 홀수 번 바뀔 때 왼쪽으로 감소
    if not turn_c % 2:              # 짝수 번 바뀔 때 위로 증가
        print(w - row % w, col % h)
    else:                           # 홀수 번 바뀔 때 아래로 감소
        print(w - row % w,  h - col % h)