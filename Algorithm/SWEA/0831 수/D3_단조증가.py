import sys
sys.stdin = open('testcase/단조증가_input.txt')

t = int(input())
for tc in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    max_num = -1
    for i in range(n-1):
        for j in range(i+1, n):
            judge = 1
            number = num[i] * num[j]
            arr = str(number)
            if number >= 10:
                for k in range(len(arr) - 1):
                    if arr[k] > arr[k+1]:        # 다음 수가 작으면 judge = 0
                        judge = 0
                        break

                if judge and max_num < number:   # 단조증가를 만족하고 number이 max_num보다 크면 덮어씀
                    max_num = number
    print(f'#{tc+1} {max_num} ')




