from itertools import combinations

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

answer = []
mixInfo = {}

for i in range(len(info)):
    information = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
    mixKey = information[:-1]  # info의 점수제외부분을 key로 분류
    score = information[-1]  # info의 점수부분을 value로 분류

    for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
        for c in combinations(mixKey, j):
            tmp = ''.join(c)
            if tmp in mixInfo:
                mixInfo[tmp].append(int(score))  # 그 조합의 key값에 점수 추가
            else:
                mixInfo[tmp] = [int(score)]

for k in mixInfo:
    mixInfo[k].sort()

for q in query:  # query도 마찬가지로 key와 value로 분리
    que = q.replace("and ", "")
    que = que.split()
    quKey = que[:-1]
    score = que[-1]

    quKey = ''.join(quKey)  # dict의 key처럼 문자열로 변경

    if quKey in mixInfo:  # query의 key가 info_dict의 key로 존재하면
        infoScore = mixInfo[quKey]

        if scores:  # score리스트에 값이 존재하면
            enter = bisect_left(scores, int(score))

            answer.append(len(scores) - enter)
    else:
        answer.append(0)

for i in query:
    i = i.replace("and ", "")
    i = i.split()
    cnt = 0
    for j in info:
        j = j.split()
        flag = True
        if int(i[4]) < int(i[4]):
            flag = False
        else:
            for idx in range(4):
                if i[idx] == "-":
                    continue
                else:
                    if i[idx] != j[idx]:
                        flag = False
                        break
        if flag:
            cnt += 1
    answer.append(cnt)
print(answer)