n, k = map(int, input().split())  # 물품 수 n, 최대 무게 k

table = [0] * (k+1)               # 무게가 인덱스인 테이블

for i in range(n):
    w, v = map(int, input().split())
    if w <= k:
        for j in range(k, 0, -1):
            if j + w <= k and table[j]:                         # 최대 무게보다 작거나 같고, talbe 값이 0인 경우에는 연산할 필요없다.
                table[j+w] = max(table[j + w], table[j]+v)      # 기존의 값과 현재 생성된 값을 비교하여 큰값을 넣어준다.
        table[w] = max(table[w], v)                             # 현재 물건의 무게에 기존 구해진 V값이 있다면 비교하여 큰 값을 넣는다.
print(max(table))