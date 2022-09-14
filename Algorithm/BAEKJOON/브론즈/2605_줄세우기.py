n = int(input())
arr = list(map(int, input().split()))
line = [1]

for i in range(1, n):
    line.insert(i - arr[i], i+1) # insert(인덱스,값): 지정위치에 값 추가

# print(' '.join(map(str, line)))
print(*line)