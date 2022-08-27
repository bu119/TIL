height = []
for n in range(9):
    height.append(int(input()))
# height에 키를 list로 추가
# 미리 정렬
height.sort()
# 밑에서 for문 돌리는 횟수를 줄이려고 만듬
first = 0
# for문을 활용하여 9명의 키를 다 더한 값에서 두명을 빼고
# 100이 나오면 그때 2명의 인덱스를 first, second에 넣어줌
for i in range(8):
    for j in range(i+1, 9):
        if sum(height) - height[i] - height[j] == 100:
            first = i
            second = j
            break
    # first에 값이 있으면 포문 나옴
    if first:
        break
# pop(인덱스)를 활용하여 제거
height.pop(first)
# second 인덱스가 first인덱스 보다 뒤에 있어서
# 앞에 pop으로 뒤에 인덱스가 감소 했기 때문에 -1 해줌
height.pop(second-1)
for k in height:
    print(k)