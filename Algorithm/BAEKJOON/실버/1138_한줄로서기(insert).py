n = int(input())
# 키: 4 2 1 3
# 키가 1인사람부터 왼쪽에 키큰 사람이 몇명 있는지: 2 1 1 0
arr = list(map(int,input().split()))
ans = []
for i in range(len(arr)-1, -1, -1):
    ans.insert(arr[i], i+1)
print(*ans)

# 작은 수 부터 자리를 채워나가면 된다.
# 큰 사람이 왼쪽에 몇 명이 있어야 하는지 주어진 값을 보고 그만큼의 빈자리를 비워 둔 후에 값을 채우면 된다.