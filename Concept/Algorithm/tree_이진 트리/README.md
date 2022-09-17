# 이진트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드
  - 오른쪽 자식 노드

- 레벨 i에서의 노드의 최대 개수는 2^i 개

- 높이가 h인 이진 트리가 가질수 있는 노드의 **최소 개수는 `h + 1` 개**, **최대 개수는 `2 ^ (h + 1) - 1 개`** 가 된다.

  

  <img width="825" alt="이진트리(1)" src="https://user-images.githubusercontent.com/109335452/190841228-10881153-c1b4-4e8f-954f-d1aae7e3b6fe.png">

## 1. 포화 이진 트리

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리

- 높이가 h일 때, 최대의 노드 개수인  `2 ^ (h + 1) - 1`의 노드를 가진 이진 트리

- 루트를 1번으로 하여 `2 ^ (h + 1) - 1` 까지 정해진 위치에 대한 노드 번호를 가짐

  

  <img width="873" alt="포화이진트리(1)" src="https://user-images.githubusercontent.com/109335452/190841342-e31032d3-a667-40fe-8395-00629d622865.png">

## 2. 완전 이진 트리

- 높이가 h이고 노드의 수가 n개일 때, 1번 부터 n 번까지 빈 자리가 없는 이진 트리

  

  <img width="762" alt="완전이진트리(1)" src="https://user-images.githubusercontent.com/109335452/190841343-1bd4c120-ae57-4157-8a0f-c0fcf31db34a.png">

## 3. 순회

- 트리의 각 노드를 중복되지 않게 전부 방문하는 것을  말한다.
- 트리의 노드들을 체계적으로 방문하는 것



### 3가지 순회 방법

1. 전위순회 : `VLR`

   - 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.

2. 중위순회 : `LVR`

   - 왼쪽 자식노드 , 부모노드, 오른쪽 자식노드 순으로 방문한다.

3. 후위순화 : `LRV`

   - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.

   

   <img width="352" alt="이진트리 순회" src="https://user-images.githubusercontent.com/109335452/190841472-bb018897-07a1-4c05-ae4b-300039d42431.png">
   90841343-1bd4c120-ae57-4157-8a0f-c0fcf31db34a.png">

## 4. 이진트리의 표현

- 이진 트리에 각 노드 번호를 다음과 같이 부여한다.

  - 루트의 번호는 1로 한다.
  - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 `2 ^ n` 부터 `2 ^ (n + 1) - 1` 까지 번호를 차례로 부여한다.

  <img width="746" alt="이진트리의 표현(1)" src="https://user-images.githubusercontent.com/109335452/190841595-5052d6ab-a65f-4412-879e-c6938ed15ad7.png">

### 노드 번호의 성질

- 노드 번호가 i 인 노드의 부모노드 번호 : `i / 2`

- 노드 번호가 i 인 노드의 왼쪽 자식 노드 번호 : `2 * i`

- 노드 번호가 i 인 노드의 오른쪽 자식 노드 번호 : `2 * i + 1`

- 레벨 n의 노드 번호 시작 번호 : `2 ^ n`

  

  <img width="632" alt="이진트리의 표현(2)" src="https://user-images.githubusercontent.com/109335452/190841824-654c12f8-6a9b-4c0f-a060-42d9934fe0b8.png">



## 5. 이진 트리의 저장

### 1. 부모 번호를 인덱스로 자식 번호를 저장

1. 왼쪽 자식과 오른쪽 자식이 들어갈 수 있는 배열 2개를 만든다.
2. 왼쪽 자식이 값이 없으면 왼쪽 자식에 값을 넣는다.
3. 왼쪽 자식에 값이 있으면 오른쪽 자식에 넣는다. 

<img width="1212" alt="이진트리 저장방법(1)" src="https://user-images.githubusercontent.com/109335452/190841944-c9bc6300-a7ff-4a56-b17e-9ec5eb20ab89.png">

### 2. 자식 번호를 인덱스로 부모 번호를 저장

1. 자식의 번호 인덱스 만큼 배열을 만든다.

2. 자식 번호의 인덱스 값에 해당하는 부모 번호를 저장한다.

   <img width="858" alt="이진트리 저장방법(2)" src="https://user-images.githubusercontent.com/109335452/190842088-9ce74ffe-f01a-4790-b06f-5d7a74bce1bb.png">

- 루트 찾기
- 조상 찾기

---

# Code

1. 전위 순회

   ```python
   '''
   정점번호 1 ~ (V)
   정점수
   부모-자식순
   5
   1 2 1 3 3 4 3 5
   '''
   
   def preorder(n):            			# 전위 순회
       if n:
           print(n, end=' ')  				# visit(n)
           preorder(ch1[n])
           preorder(ch2[n])
   
   V = int(input())
   arr = list(map(int, input().split()))
   E = V - 1
   root = 1                                # 루트 번호 1
   
   # 부모를 인덱스로 자식번호 저장
   ch1 = [0] * (V+1)
   ch2 = [0] * (V+1)
   
   for i in range(E):
       p, c = arr[i*2], arr[i*2+1]         # 부모, 자식 번호
       if ch1[p] == 0:                     # 아직 자식이 없으면
           ch1[p] = c                      # 자식 1에 저장
       else:                               # 자식 1에 자식이 있으면
           ch2[p] = c                      # 자식 2에 저장
   
   preorder(root)                          # 1 2 3 4 5
   ```

2. 중위 순회

   ```python
   '''
   정점번호 1 ~ (V)
   정점수
   부모-자식순
   5
   1 2 1 3 3 4 3 5
   '''
   
   def inorder(n):             			# 중위 순회
       if n:
           inorder(ch1[n])
           print(n, end=' ')   			# visit(n)
           inorder(ch2[n])
   
   V = int(input())
   arr = list(map(int, input().split()))
   E = V - 1
   root = 1                                # 루트 번호 1
   
   # 부모를 인덱스로 자식번호 저장
   ch1 = [0] * (V+1)
   ch2 = [0] * (V+1)
   
   for i in range(E):
       p, c = arr[i*2], arr[i*2+1]         # 부모, 자식 번호
       if ch1[p] == 0:                     # 아직 자식이 없으면
           ch1[p] = c                      # 자식 1에 저장
       else:                               # 자식 1에 자식이 있으면
           ch2[p] = c                      # 자식 2에 저장
   
   inorder(root)                           # 2 1 4 3 5
   ```

3. 휘위 순회

   ```python
   '''
   정점번호 1 ~ (V)
   정점수
   부모-자식순
   5
   1 2 1 3 3 4 3 5
   '''
   
   def postorder(n):           # 후위 순회
       if n:
           postorder(ch1[n])
           postorder(ch2[n])
           print(n, end=' ')   # visit(n)
   
   V = int(input())
   arr = list(map(int, input().split()))
   E = V - 1
   root = 1                                # 루트 번호 1
   
   # 부모를 인덱스로 자식번호 저장
   ch1 = [0] * (V+1)
   ch2 = [0] * (V+1)
   
   for i in range(E):
       p, c = arr[i*2], arr[i*2+1]         # 부모, 자식 번호
       if ch1[p] == 0:                     # 아직 자식이 없으면
           ch1[p] = c                      # 자식 1에 저장
       else:                               # 자식 1에 자식이 있으면
           ch2[p] = c                      # 자식 2에 저장
   
   postorder(root)                         # 2 4 5 3 1
   ```

   