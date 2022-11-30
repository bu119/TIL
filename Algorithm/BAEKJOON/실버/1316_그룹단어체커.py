import sys
input = sys.stdin.readline

n = int(input())
cnt = n
for _ in range(n):
    word = input()
    num = len(word)
    words = [word[0]]           # 중복 체크
    for i in range(1, num):
        if word[i-1] != word[i]:
            if word[i] in words:
                cnt -= 1
                break
            else:
                words.append(word[i])
print(cnt)
