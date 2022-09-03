import sys
sys.stdin = open("1215_input.txt", "r")

# 각 칸의 들어가는 글자는 a, b, c 중 하나
for tc in range(10):
    n = int(input())
    arr = []
    for s in range(8):
        abc = list(input())
        arr.append(abc)

    cnt = 0
    for i in range(8):  # 행 탐색
        for j in range(8-n+1):
            array = arr[i][j:j+n]    # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                cnt += 1

    # 행과 열 바꾸기
    for row in range(8):
        for col in range(8):
            if row < col:
                arr[row][col], arr[col][row] = arr[col][row], arr[row][col]

    for i in range(8):  # 열 탐색
        for j in range(8-n+1):
            if j == 0:
                if arr[i][:n] == arr[i][n-1::-1]:
                    cnt += 1
            else:
                if arr[i][j:j+n] == arr[i][j+n-1:j-1:-1]:  # ex) 0에서 3 까지 == 3에서 0 까지
                    cnt += 1

    print(f"#{tc+1} {cnt}")