# 1961_숫자배열회전

t=int(input())
for i in range(t):          # t 개수 만큼 반복
    n = int(input())        # 행렬 모양 받기
    list_n = []
    list_90 = []
    list_180 = []
    list_270 = []
    for j in range(n):           # 행렬 만들기
        number=input().split()   # n행 = [ 숫자, 숫자, 숫자, ... ]
        list_n.append(number)    # [ [1행], [2헹], [3행], ... ]

    for k1 in range(n):                  # 행의 개수 민큼 시행
        w=''
        for n_90 in list_n[::-1]:        # n행, n-1행 순으로 시행
            w += n_90[k1]                # 90도 돌리기
        list_90.append(w)

    for n_180 in list_n[::-1]:           # 180도 돌리기
        list_180.append(''.join(n_180[::-1]))

    for k2 in reversed(range(n)):        # 인덱스 뒤에서 부터 시행
        w=''
        for n_270 in list_n:
            w += n_270[k2]               # 270도 돌리기
        list_270.append(w) 
    
    print(f'#{i+1}')
    for change in range(n):              # 행렬 위치 바꾸기
        print(f'{list_90[change]} {list_180[change]} {list_270[change]}')
