import sys
sys.stdin = open("1215_input.txt", "r")

# 두번 쓰여서 함수로 만듬
def palindrome(arr, n):  #각 행의 회문 개수를 구함
    cnt = 0
    for i in range(8):  # 행 탐색
        for j in range(8 - n + 1):
            array = arr[i][j:j + n]   # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                cnt += 1
    return cnt

for tc in range(10):
    n = int(input())
    arr = []
    for s in range(8):
        abc = list(input())
        arr.append(abc)

    palindrome1 = palindrome(arr, n) # 행 탐색

    # 행과 열 바꾸기
    for row in range(8):
        for col in range(8):
            if row < col:
                arr[row][col], arr[col][row] = arr[col][row], arr[row][col]

    # 행렬을 바꾸는 내장함수
    # arr = list(zip(*arr))

    palindrome2 = palindrome(arr, n) # 열 탐색

    print(f"#{tc+1} {palindrome1 + palindrome2}")