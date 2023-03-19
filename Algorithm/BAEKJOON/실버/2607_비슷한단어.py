# 두 단어가 같은 구성을 갖는 경우,
# 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어
# 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.
# 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.
n = int(input())
word = list(input())

ans = 0
for _ in range(n-1):
    other = list(input())
    cnt = 0
    for w in word:
        # 첫 단어 기준으로 다음 단어들 비교
        if w in other:
            # 같은 단어가 존재하면 비교 단어에서 제거
            other.remove(w)
        else:
            # 비교 단어에 존재하지 않는 기준 단어 개수
            cnt += 1
    # len(other) 기준 단어와 같은 단어를 제거하고 난 뒤에도 존재하는 비교 단어
    if cnt <= 1 and len(other) <= 1:
        ans += 1
print(ans)

