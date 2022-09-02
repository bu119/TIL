c_end, r_end = map(int, input().split())
n = int(input())

row = [0] # 가로 처음 값
col = [0]
for i in range(n):
    rc, cut = map(int, input().split())
    if rc == 0:
        row.append(cut)
    else:
        col.append(cut)

row.append(r_end) # 가로 마지막 값
col.append(c_end)
row.sort()
col.sort()

maxr = 0
maxc = 0
for j in range(len(row)-1):
    if maxr < row[j+1] - row[j]:
        maxr = row[j+1] - row[j]
for k in range(len(col)-1):
    if maxc < col[k+1] - col[k]:
        maxc = col[k+1] - col[k]

print(maxr * maxc)