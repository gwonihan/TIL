# 빅데이터

### 빅데이터

- 너무 크고 복잡해서 기존 RDBMS(관계형 데이터베이스)에서 다루기 어려운 데이터
- RDBMS가 모든 규모에 적용 가능할 수 있다고..



### 데이터 과학

- 대량의 데이터를 분석해서 지식을 추출하는 방법

- 통계의 확장판 -> computer science가 주축

  

### 데이터 과학에서 파이썬의 장점

- 큰 성능 저하 없이 프로토타입을 빨리 수행



### 빅데이터 특징

- Volume(데이터의 양)
  - Tera -> Peta byte
  - 기존 파일시스템의 한계
  - Transaction
- Velocity(수집 속도)
  - 배치 처리(Batch)
  - 실시간 처리(Real Time)
  - 스트리밍(Streaming)
- Value
  - 데이터를 통한 가치 창출
- Veracity
  - 데이터의 정확도
- Variety(데이터 종류의 다양성)
  - 정형(Structured)
  - 반정형(Seimi-Structured)
  - 비정형(Unstructured)



### Scale Up  VS Scale Out

1. Scale Up

   - 서버의 Spec을 높이는 방식 

     ex)CPU 및 메모리 증설

   - 비용 문제

   - 데이터 크기 문제

   - 데이터 처리 문제

2. Scale out

   - 서버의 대수를 늘려서 처리하는 방식

     ex) 서버 및 노드 추가



### 데이터 종류

- 정형 데이터
  - 데이터모델에 의존적이며, 레코드 내의 고정된 필드가 존재
  - DB 테이블, 엑셀 파일, CSV
- 비정형 데이터
  - 데이터모델에 잘 맞지 않는 데이터
  - 이메일
- 자연어 데이터
  - 비구조적 데이터의 특수한 형태
  - 특수한 데이터과학 기법과 언어학의 지식이 필요
  - 이메일은 비구조적 데이터와 자연어 데이터 모든 특징 포함
- 기계 생성 데이터
  - 비구조적 데이터로 기계(log, loT)가 생성해 낸 데이터
- 그래프 기반 데이터
  - 수학의 그래프이론(graph theory)에 기반한 데이터
  - 꼭지점(node)과 변(edge), 속성(property)을 가지고 표현
  - 소셜 네트워크를 표현하는데 적합
  - 사람의 영향력이나 사람들 사이의 최단 경로를 수치화 하는데 이용
  - 링크드인, 트위터 팔로워 목록, 페이스북 친구, 넷플릭스 영화취향
- 오디오, 비디오, 이미지
  - 그림의 사물을 분석 - 딥러닝 이용
  - 딥마인드의 비디오 게임 플레이 학습
- 스트리밍 데이터
  - 데이터가 일괄처리 및 저장되는 것이 아니라 이벤트에 의해 들어감
  - 트위터의 실시간 트랜드, 주식시장의 스트리밍 데이터



### 빅데이터 프로세스

1. 문제 정의

   - 무엇을 분석할 것인가?

     -> 객관적이고 구체적인 분석 대상의 정의

2. 데이터 수집, 가공

   - 필요한 데이터가 무엇이고 어디서 수집할 것인가?
     - 데이터 구조 및 특성 변경
     - 데이터 오류 확인 및 수정

3. 데이터 모델링

   - 상관분석을 위한 데이터간 관계를 설정

4. 데이터 시각화 및 분석

   - 데이터 분석을 위한 시각화
   - 데이터에 대한 통찰력 확보



### 데이터 사이언스 프로세스

Data Science = OSEMN (어썸*)한 프로세스

| 구분                        | 내용                                                |
| --------------------------- | --------------------------------------------------- |
| **<u>O</u>**btain(획득)     | 내/외부 데이터 수집                                 |
| **<u>S</u>**crub(정제)      | 결측치 처리, 데이터 변환 등을 통해 분석 용이화      |
| **<u>E</u>**xplore(탐색)    | 데이터의 속성을 파악하기 위해 기술통계, 시각화 적용 |
| **<u>M</u>**odeling(모형화) | 회귀분석 등을 통해 데이터를 잘 설명하는 모형 구축   |
| i**<u>N</u>**terpret(해석)  | 분석 결과 평가, 결론 도출 및 의미 획득              |





## Numpy

특징

- 수학 계산을 위한 라이브러리
  - 선형 대수
  - 벡터 및 행렬 연산에 특화
  - Array(2차원 이상 배열)단위로 데이터를 관리하고 연산
  - 백터(1차원 배열)



넘파이 문법

lst = ([

​          [1,2,3],

​          [4,5,6],

​          [7,8,9]

​         ])

1. 생성

   ```python
   # array :  행렬생성
   intArray = np.array([1,2],[3,4])
   print(intArray)
   >> array([ [1, 2],
              [3, 4] ])
   
   
   # empty : 빈 행렬 생성
   np.empty((4,3))
   >>값이 정해지지 않은 4행 3열 생성
   
   
   # empty/zeros/ones...like(A) : A와 같은 형태의 행렬 생성
   np.empty_like(A)
   
   
   # zeros((행,열)) : 값이 0인 행렬 생성
   np.zeros((2,3))
   >> array([ [0., 0., 0.],
              [0., 0., 0.] ])
   
   
   # ones((행,열)) : 값이 1인 행렬 생성
   np.ones((2,3))
   >> array([ [1., 1., 1.],
              [1., 1., 1.] ])
   
   
   # identity((n)) : n x n 항등행렬
   >> array([ [1., 0.],
              [0., 1.] ])
   
   
   # eye(n k dtype=int) : n x n 정방단위행렬, k 값에 따라 달라짐
   >> array([ [1., 0., 0.],
              [0., 1., 0.],
              [0., 0., 1.] ])
   
   
   # full((행,열), 값) : 행렬에 같은 값을 채운 행렬
   np.full((2,3),10)
   >> array([ [10, 10, 10],
              [10, 10, 10] ])
   
   
   # arange(시작값, 끝값, 간격값)
   np.arange(10)
   >> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
   np.arange(1.0, 5.0, 0.5)
   >> array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
   
   
   # linspace(시작, 끝, num = 사이값 갯수)
   np.linspace(2.0, 3.0, num = 5)
   >> array( [2.  , 2.25, 2.5 , 2.75, 3.  ] 
           )
   
   
   # rand : 0~1 사이의 난수
   sample1 = np.random.rand(2,2)  # 2행 2열
   >> array([[0.62783629, 0.27069198],
            [0.1431216 , 0.5330023 ]])
   sample2 = sample1.tolist()     # 리스트로!
   >> [[0.62783629165976, 0.2706919775356931],
       [0.1431216036781483, 0.5330023007295807]]
   
   
   #!wget
   !wget -O 파일이름 [URL] 해당 URL에 접속하여 파일 다운로드
   
   
   ```

   

2. 연산

   ```python
   import numpy as np
   
   # 합산 (sum)
   np.sum(lst)
   
   
   # 평균 (mean)
   np.mean(lst)
   np.mean(lst, axis=0)  행 방향의 평균값
   >> array([4.,5.,6.])
   np.mean(lst, axis=1)  열 방향의 평균값
   >> array([2.,5.,8.])
   np.mean(range(1,11))  산술평균
   >> 5.5
   
   
   # amin, amax
   A = np.arange(4).reshape((2,2))
   >> array([ [0, 1],
              [2, 3] ])
   
   	np.amin(A,axis=0)
       >> array([0, 1])
       np.amax(A,axis=1)
       >> array([1,3])
       
       
   # ptp (최대값 - 최소값)
   	np.ptp(A, axis=0)
       >> array([2, 2])
       
       
   # median 중간값
   B = array([ [0, 1, 2],
               [3, 4, 5],
               [6, 7, 8] ])
   	np.median(B, axis=0)
       >> array([3., 4., 5.])
       
       
   # var : 분산
   	np.var(B, axis=0)
       >> array([6., 6., 6.])
       
       
   # std : 표준편차
   	np.std(B, axis=0)
       >> array([2.44948974, 2.44948974, 2.44948974])
       
       
   # 행열바꾸기 (Transpose)
   x = np.array([1,2],
                [3,4], dtype=np.int8)
   y = x.T
   >> array([[1, 3],
             [2, 4]], dtype=int8)
   
   
   # 행간, 열간 차이 (strides)
   x.strides
   >> (2,1)
   y.strides
   >> (1,2)
   
   
   # bool 타입
   boolArray = np.array([True, False, True, False, True])
   print(boolArray)
   >>array([ True, False,  True, False,  True])
   
   
   a = np.arange(1,7).reshape(3,2)
   print(a)
   >> array([ [1, 2],
              [3, 4],
              [5, 6]])
   
   bool_idx = (a>2)
   print(bool_idx)
   >> array([ [False, False],
              [ True,  True],
              [ True,  True]])
   
   a[bool_idx]
   >> array([3, 4, 5, 6])
   ```

   

3. 슬라이싱, 인덱싱, 함수 

   ```python
   a = np.arange(12).reshape((3,4))
   >> array([ [ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11] ])
   
   
   # 슬라이싱
   a[0:2, 0:4]
   a[:2,:]
   a[:2]
   >> array([ [0, 1, 2, 3],
              [4, 5, 6, 7] ])
   
   a[:,0:1]
   >> array([ [0],
              [4],
              [8] ])
   
   
   # 인덱싱
   a[0,0]
   a[0][0]
   >> 0
   
   a[[0,2], ]
   >> array ([ [ 0, 1, 2, 3 ],
               [8, 9, 10, 11] ])
   
   a[:, [0,1,3]]
   >> array([ [ 0,  1,  3],
              [ 4,  5,  7],
              [ 8,  9, 11] ])
   
   
   # 정수 인덱싱
   b = array([ [1, 2],
               [3, 4],
               [5, 6]])
   #b[[행에 대한 정보],[열에 대한 정보]]
   b[[0,1,2], [0,1,0]] 
   
   np.array([a[0,0], a[1,1], a[2,0]])
   >> array([1, 4, 5])
   
   
   # shape : 행렬의 형태를 알려줌
   a.shape
   >> (3,4)
   
   
   # ndim : 몇차원인지 도출
   a.ndim
   >> 2
   
   
   # Transpose(전치)
   x = np.array([ [1,2] , [3,4] ])
   print(x)
   >> array([ [1, 2],
              [3, 4]])
   
   x.T
   >> array([ [1, 3],
              [2, 4] ])
   
   v = np.array([1,2,3])
   v.T
   >>array([1, 2, 3])   : 1차원이라 행밖에 없기때문에, 바뀌지 않는다.
       
       
   # 1차원 배열 만들기 : ravel, flatten
   a = np.arange(6).reshape(3,2)
   >> array([ [0, 1],
              [2, 3],
              [4, 5]])
   
   np.ravel
   or
   a.ravel()
   or
   a.flatten
   >> array([0, 1, 2, 3, 4, 5])
    주의! numpy에는 flatten 함수가 없으므로 np.flatten()은 불가!
          그리고 ravel 은 a와 같은 메모리 주소를 갖지만,
          flatten은 a와 상관 없는 메모리 주소를 갖는다.
   
   # concatenate
   a = np.array([[1,2],[3,4]])
   b = np.array([[5,6]])
   print(a) = array ([ [1, 2],
                       [3, 4] ])
   print(b) = array ([ [5, 6] ])
   
   np.concatenate((a,b), axis=0)
   >> array([ [1, 2],
              [3, 4],
              [5, 6]])
   
   np.concatenate((a,b), axis=1) 을 하면 에러가 발생하는데 b의 shape이 a와 다르기 때문이다.
   그러므로 이를 위해서는 'b.T'를 해서 2행 1열로 만들어주면,
   np.concatenate((a,b.T), axis=1)
   >> array([ [1, 2, 5],
              [3, 4, 6]])
   로 연산이 가능하다.
   
   요소들끼리 연산을 할 때에도 shape이 같아야 가능하다.
   
   x = np.array([[1.,2.],                              
                 [3.,4.]])
   y = np.array([[5.,6.],
                 [7.,8.]])
   
   x + y
   np.add(x,y)
   >> array([ [ 6.,  8.],
              [10., 12.]])
   
   x - y
   np.subtract(x,y)
   >> array([ [-4., -4.],
              [-4., -4.]])
   
   x * y
   np.multiply(x,y)
   >> array([ [ 5., 12.],
              [21., 32.]])
   
   x / y
   np.divide(x,y)
   >> array([ [0.2       , 0.33333333],
              [0.42857143, 0.5       ] ])
   
   
   # dot 행렬의 곱
   x = np.array([[1.,2.],                               
                 [3.,4.]])
   y = np.array([[5.,6.],
                 [7.,8.]])
   v = np.array([9,10])                             
   w = np.array([11,12])
   
   v.dot(w)
   np.dot(v,w)
   >> 219
   
   x.dot(v)
   np.dot(x,v)
   >> array ([29., 67.])
   
   x.dot(y)
   np.dot(x,y)
   >> array([ [19., 22.],
              [43., 50.] ])
   
   # 브로드캐스팅
   x = np.array([
                 [1,2,3],
                 [4,5,6],
                 [7,8,9],
                 [10,11,12]
                 ])
   
   v=np.array([1,0,1])
   
   x[0, :] + v
   >> array([2,2,4])  행렬의 형태가 같으므로 연산 가능
   
   y = np.empty_like(x)
   for i in range(4):
       y[i, :] = x[i, :] + v    
   print(y)
   >>> array([ [ 2,  2,  4],
               [ 5,  5,  7],
               [ 8,  8, 10],
               [11, 11, 13] ])
   
   # 1) tile
   vv = np.tile(v, (4,1))
   >> array([ [1, 0, 1],
              [1, 0, 1],
              [1, 0, 1],
              [1, 0, 1]])
   
   y = x + vv
   >> array([ [ 2,  2,  4],
              [ 5,  5,  7],
              [ 8,  8, 10],
              [11, 11, 13]])
   ```
   
   
