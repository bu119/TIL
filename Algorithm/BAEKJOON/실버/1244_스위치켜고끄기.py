def change(idx):
    global arr
    if arr[idx]:
        arr[idx] = 0
    else:
        arr[idx] = 1

n = int(input())
arr = list(map(int, input().split()))            # 켜져 있으면 1, 꺼져있으면 0
st_num = int(input())

for i in range(st_num):
    gender, num = map(int, input().split())      # 한 학생의 성별, 학생이 받은 수

    if gender == 1:                              # 남학생은 1, 여학생은 2
        boy = n//num                             # 남자 배수 개수
        for j in range(boy):
            idx_b = num * (j + 1) - 1
            change(idx_b)
    else:
        girl = min(num, n-num+1)                 # 여자 비교 개수
        idx_g = num - 1
        change(idx_g)
        for k in range(1, girl):
            if arr[idx_g-k] == arr[idx_g+k]:
                change(idx_g-k)
                change(idx_g+k)
            else:
                break

pr_num = n//20
for z in range(pr_num+1):
    print(*arr[20*z:20*(z+1)])