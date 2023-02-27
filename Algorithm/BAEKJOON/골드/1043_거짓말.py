import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 진실을 아는 사람수, 번호
cnt, *number = map(int, input().split())
number = set(number)
arr = []
if cnt:
    for _ in range(m):
        # 사람수, 사람 번호
        total, *num = map(int, input().split())
        num = set(num)
        arr.append(num)

        if num & number:
            number = num | number

    for _ in range(m-1):
        for i in arr:
            if number & i:
                number = i | number

for j in arr:
    if number & j:
        m -= 1

print(m)