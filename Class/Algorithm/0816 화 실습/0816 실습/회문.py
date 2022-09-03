import sys
sys.stdin = open("sample_input.txt", "r")

def palindrome(arr, n, m):
    result = 0
    for i in range(n):  # 행 탐색
        for j in range(n - m + 1):
            array = arr[i][j:j + m]  # i행 리스트를 n칸씩 자름
            if array == array[::-1]:
                return array

t = int(input())
for tc in range(t):
    n, m = map(int, input().split()) # n크기, m회문길이
    arr = []
    for i in range(n):
        arr.append(input())

    if palindrome(arr, n, m):  # 행 탐색
        print(f'#{tc + 1} {palindrome(arr, n, m)}')
    else:
        arr = list(zip(*arr))  # 열 탐색
        result = ''.join(palindrome(arr, n, m))
        print(f'#{tc + 1} {result}')




