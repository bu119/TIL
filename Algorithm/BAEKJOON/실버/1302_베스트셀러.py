n = int(input())
book = {}
for _ in range(n):
    title = input()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1

sell = sorted(book.items())
sell.sort(key=lambda x: x[1], reverse=True)
print(sell[0][0])
