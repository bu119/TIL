from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

last_arr = sorted(arr, reverse=True)

if arr == last_arr:                         # 전체가 내림차 순이면 (사전 순으로 마지막에 오는 순열)
    print(-1)
else:
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:               # 내림차 순이면 pass
            pass
        else:                               # 내림차 순이 아닌 자리가 나오면 (바로 앞 자리 수가 작으면)
            for j in range(n-1, 0, -1):
                if arr[i-1] < arr[j]:                       # 뒤에 자리 수들 중 큰 수와 자리 바꿈
                    arr[i - 1], arr[j] = arr[j], arr[i-1]
                    arr = arr[:i] + sorted(arr[i:])         # 바뀐 자리 뒤는 오름차 순으로 정렬
                    print(' '.join(map(str, arr)))
                    exit(0)
