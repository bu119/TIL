import sys
sys.stdin = open("색칠_input.txt", "r")

t = int(input())
size = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [[0]*size for _ in range(size)]

    # 색칠하기
    for _ in range(n):  # 할일 없으면 밑줄로 대체간능
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color  # 누적

    # print_arr(arr)
    # print(arr)  값 확인

    # 겹쳐진 칸수 카운트
    cnt = 0
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
