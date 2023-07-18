def solution(s, N):
    # 길이가 n인 s의 substring을 10진수로 읽은 숫자
    # 1부터 n까지의 숫자를 하나씩 사용하여 만든 n자리 숫자

    answer = -1
    check = list(range(1,N+1))

    for i in range(len(s)-N+1):
        num = s[i:i+N]
        if list(map(int,sorted(num))) == check:
            if int(answer) < int(num):
                answer = int(num)
    return answer


s="1451232125"
N=2

print(solution(s,N))