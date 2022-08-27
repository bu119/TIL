height = []
for n in range(9):
    height.append(int(input()))

height.sort()
row = 0
for i in range(8):
    for j in range(i+1, 9):
        if sum(height) - height[i] - height[j] == 100:
            row = i
            col = j
            break
    if row:
        break

height.pop(row)
height.pop(col-1)
for k in height:
    print(k)