n, k = map(int, input().split())  # 물품 수 n, 최대 무게 k

table = [0] * (k+1)               # 무게가 인덱스인 테이블

for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        for j in range(k, -1, -1):
            if j + w <= k:                                      # 최대 무게보다 작거나 같을 때
                table[j+w] = max(table[j + w], table[j]+v)      # 기존의 값과 현재 생성된 값을 비교하여 큰값을 넣어준다.

print(max(table))