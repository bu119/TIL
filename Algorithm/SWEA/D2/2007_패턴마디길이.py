# 2007. 패턴 마디의 길이
t = int(input())
for i in range(t):
    words = input()
    for j in range(1,10):                   # 마디 최대 길이 10이므로 인덱스 1부터 9까지 (마디 길이가 2개부터 10개까지)
        if words[:j] == words[j:j+j]:       # 패턴이 같은 지 비교 (words의 인덱스는 0부터 시작)
            print(f'#{i+1} {j}')
            break                           # for문이 더 이상 반복하지 않도록 break를 걸어