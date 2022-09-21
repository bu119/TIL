# 10, 11, 12, 13, 14,15
# a, b, c, d, e, f
import sys
sys.stdin = open('input_이진수1.txt')

table = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

t = int(input())
for tc in range(t):
    ans = ''
    n, arr = input().split()
    for i in range(int(n)):
        ans += table[arr[i]]

    print(f'#{tc+1} {ans}')