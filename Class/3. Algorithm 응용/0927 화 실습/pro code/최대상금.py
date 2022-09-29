import sys; sys.stdin = open('최대상금_input.txt')
def swap(prize, i, j):
    # itoa
    prize_arr = [0] * prize_len
    for k in range(prize_len-1, -1, -1):
        prize_arr[k] = prize % 10
        prize //= 10
    # swap
    prize_arr[i], prize_arr[j] = prize_arr[j], prize_arr[i]
    # atoi
    prize = 0
    for k in range(prize_len):
        prize = prize * 10 + prize_arr[k]
    return prize


def find_max(n, k, prize):
    global ans
    # cnt += 1
    ###  가지치기
    for i in range(MAX_SIZE):
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return

    if n == k:
        if ans < prize:
            ans = prize
    else:
        for i in range(0, prize_len - 1):
            for j in range(i+1, prize_len):
                find_max(n, k+1, swap(prize, i, j))

MAX_SIZE = 720
T = int(input())
for tc in range(1, T+1):
    prize, N = map(int, input().split()) # 숫자판, 교환횟수
    memo = [[0] * MAX_SIZE for _ in range(N + 1)]
    # 숫자판 길이 구하기
    prize_len = 0
    t = prize
    while t:
        t //= 10
        prize_len += 1

    # cnt = 0
    ans = 0
    find_max(N, 0, prize)
    print(f'#{tc} {ans}')