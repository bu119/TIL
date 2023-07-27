import sys
input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    word = input().rstrip()
    words.add((len(word), word))

arr = sorted(words)

for i in arr:
    print(i[1])