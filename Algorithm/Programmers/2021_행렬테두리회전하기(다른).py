def solution(rows, columns, queries):
    answer = []
    arr = []
    num = 0
    for row in range(rows):
        tmp = []
        for col in range(columns):
            num += 1
            tmp.append(num)
        arr.append(tmp)

    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        minV = arr[x1][y1]
        topleft = arr[x1][y1]

        for left in range(x1, x2):
            arr[left][y1] = arr[left+1][y1]
            if arr[left][y1] < minV:
                minV = arr[left][y1]

        for bot in range(y1, y2):
            arr[x2][bot] = arr[x2][bot+1]
            if arr[x2][bot] < minV:
                minV = arr[x2][bot]

        for right in range(x2, x1, -1):
            arr[right][y2] = arr[right-1][y2]
            if arr[right][y2] < minV:
                minV = arr[right][y2]

        for top in range(y2, y1, -1):
            arr[x1][top] = arr[x1][top-1]
            if arr[x1][top] < minV:
                minV = arr[x1][top]

        arr[x1][y1+1] = topleft
        answer.append(minV)

    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))