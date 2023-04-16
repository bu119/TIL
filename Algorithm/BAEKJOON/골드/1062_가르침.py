from itertools import combinations

n, k = map(int, input().split())
visited = {'a','n','t','i','c'}
words = [set(input()) for _ in range(n)]
ans = 0
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    k -= 5
    # 기본 단어 제외한 input() 단어들 합집합을 담을 곳
    checkW = set()
    # 각 단어에서 기본단어 제외한 단어를 list로 구분해서 받음
    check = []
    for word in words:
        # 기본 단어 제외한 input() 단어들 합집합
        # {1,2,3} | {5,6} = {1,2,3,5,6}
        checkW |= word - visited
        check.append(word - visited)
    if len(checkW) < k:
        k = len(checkW)

    for com in combinations(checkW, k):
        cnt = 0
        c = set(com)
        for i in check:
            # c안에 i가 속해있으면 (리스트에서 if i in c:)
            # {1} - {1,2,3} = 공집합
            if not (i - c):
                cnt += 1

        if ans < cnt:
            ans = cnt
    print(ans)

