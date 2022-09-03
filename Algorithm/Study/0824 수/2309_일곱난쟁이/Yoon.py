arr = []
for i in range(9):
    arr.append(int(input()))

result = []
test = sum(arr)-100  # 9명키의 합 - 100 # 초과하는 크기를 구함
# 합이 초과하는 크기인 난쟁이 2명 찾기
print(test)
for i in range(9):
    for j in range(9):
        # i,j 가 다르고 둘이 합쳐서 초과하는 크기가 나오면
        # 두명을 뺀 나머지 인원을 result에 추가함
        if test - arr[i] == arr[j] and i != j:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    result.append(arr[k])
            break
    if len(result):
        break
# sorted로 정렬해서 프린트
for r in sorted(result):
    print(r)