n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_arr = 0
for i in range(n-1, 1, -1):           # 첫 번째 수를 선택하면   # 밑에 두 수를 선택할 수 있게 인덱스2까지 선택 가능
    for j in range(i-1, 0, -1):       # 선택한 수를 제외하고 나머지 수 중에 선택 가능 (인덱스로 표현) # 밑에 나머지 하나를 선택할 수 있게 인덱스1까지 선택 가능
        for k in range(j-1, -1, -1):
            if m >= arr[i] + arr[j] + arr[k]:
                if max_arr < arr[i] + arr[j] + arr[k]:
                    max_arr = arr[i] + arr[j] + arr[k]
print(max_arr)