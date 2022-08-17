import sys
sys.stdin = open("input.txt", "r")

def palindrome(arr, n):
    cnt = 0
    for i in range(100):  # 행 탐색
        for j in range(100 - n + 1):  # 회문 탐색 범위
            array = arr[i][j:j + n]  # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                cnt = 1  # 존재하면 1
                return cnt

for t in range(10):
    tc = input()
    arr1 = []
    for n in range(100):
        abc = list(input())
        arr1.append(abc)

    arr2 = list(zip(*arr1))

    for k in range(100, 0, -1):
        if palindrome(arr1, k) or palindrome(arr2, k):
            print(f'#{tc} {k}')
            break