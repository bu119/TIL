# 1983. 조교의 성적 매기기
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    scores = [] 
    for j in range(1, n + 1):
        me, fe, hw = map(int, input().split())
        score =[me * 0.35 + fe * 0.45 + hw * 0.2, j]     # [성적, 번호] 리스트 형태
        scores.append(score)                             # 리스트에 리스트 형태로 추가
    scores.sort(reverse=True)                            # 리스트안에 리스트 성적 높은 순으로 정렬
    for num in scores:
        if num[1] == k:                                  # 요구하는 번호와 같은
            number = scores.index(num)                   # scores의 인덱스 찾기
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    print(f'#{i + 1} {grade[number // (n // 10)]}')      
    
    # n명의 학생은 n을 10으로 나눈 몫 만큼 중복된 학점의 수를 가짐
    # 따라서 점수 높은 순으로 나열 된 리스트의 요구하는 번호와 일치하는 인덱스를 찾아
    # 중복되는 수로 나누면 그 몫은 A+부터 D0까지 학점 리스트의 인덱스로 잡힘
    # 예를 들어)
    # 20명의 학생 중 4번째 학생이 3등이면
    # 20/10 = 2 로 중복되는 학점이 2개씩임을 인지하고 
    # 3//2 = 1 등수를 중복되는 수로 나누면 1이므로 grade[1]인 A0에 해당하게 된다.
    # 7번째 학생이 7등이면 7//2 = 3 이므로 grade[3]인 B+의 학점을 받게 됨.