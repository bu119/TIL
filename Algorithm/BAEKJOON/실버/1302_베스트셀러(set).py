n = int(input())
books = [input() for _ in range(n)]
book = sorted(set(books))
cnt = 0
for i in book:
    if books.count(i) > cnt:
        cnt = books.count(i)
        title = i

print(title)