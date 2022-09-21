# 10, 11, 12, 13, 14,15
# a, b, c, d, e, f
import sys
sys.stdin = open('input_이진수1.txt')

ch_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# 2진수로 바꾸는 함수
def num2(num):
    result = [0] * 4
    idx = 3
    while num > 0:
        result[idx] = num % 2
        num = num//2
        idx -= 1
    return result

t = int(input())
for tc in range(t):
    ans = []
    n, arr = input().split()
    for i in range(int(n)):
        # 숫자가 아니면 영어를 숫자로 바꾸고 2진수로 바꿔준다.
        if arr[i].isdigit():
            ans += num2(int(arr[i]))
        else:
            ans += num2(ch_num[arr[i]])

    ans = "".join(map(str, ans))
    print(f'#{tc+1} {ans}')