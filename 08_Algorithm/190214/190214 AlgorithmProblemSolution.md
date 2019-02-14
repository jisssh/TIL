#  Algorithm Problem Solving

### `APS `  

* 기본 - 자료구조
* 응용 - 알고리즘 설계

### `최적화 문제 (optimization problems)`

​	: 최대 혹은 최소가 되는 경우를 찾는다.

* 최적 solution 을 찾는 문제
* 시간이 중요하다! 효율성이 중요하다!



#### `문제를 풀때 내장함수, 라이브러리 사용하지 않는다.`

*  DP (Dynamic Programming)
* 백트래킹
* 분할정보



## 1.배열 1 (Array 1)

### `알고리즘`

------

​	: 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다 .  

​	주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.

 	간단하게 다시 말하면 **어떠한 문제를 해결하기 위한 절차**라고 볼 수 있다. 



#### `알고리즘 표현 방법`

* 슈더코드 (실제 코드가 아니고 기술)

  ```python
  def CalcSum(n):
  	sum <- 0
  	for i in range(1, n+1):
  		sum <- sum + i;
  	return sum;
  ```

* 순서도

  ![1550107234511](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550107234511.png)

#### `무엇이 좋은 알고리즘인가?`

1. 정확성 : 얼마나 정확하게 동작하는가
2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
4. 단순성 : 얼마나 단순한가
5. 최적성 : 더 이상 개선할 여지없이 최적화 되었는가

=> `알고리즘의 성능 분석 필요!`

* `많은 문제에서 성능 분석의 기준으로 알고리즘의 작업량을 비교한다.`

#####    알고리즘의 작업량을 표현할 때 시간복잡도로 표현한다.



#### `시간 복잡도(Time Complexity)`

* 실제 걸리는 시간을 측정

* 실행되는 명령문의 개수를 계산

  ![1550107647046](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550107647046.png)



#### `시간 복잡도 => 빅-오 (O) 표기법`

* 빅-오 표기법 (Big-Oh Notation)

  * Big O :최악의 경우
  * Ω : 최선의 경우
  * θ : 최악의 경우 = 최선의 경우

* 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시

* **계수 (Coefficient) 는 생략하여 표시**

  ![1550107793199](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550107793199.png)

```
n개의 데이터를 입력 받아 저장한 후 각 데이터에 1씩 증가시킨 후 각 데이터를 화면에 출력하는 알고리즘의 시간 복잡도는 어떻게 되나?

=> O(n)
```



### `배열`

------

* 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

* 아래의 예는 6개의 변수를 사용해야 하는 경우, 이를 배열로 바꾸어 사용하는 것이다.

  ![1550107986092](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550107986092.png)



#### `배열의 필요성`

* 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.
* 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.
* 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

#### `1차원 배열의 선언`

* 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
* 이름 : 프로그램에서 사용할 배열의 이름

#### `1차원 배열의 접근`

* Arr[0] = 10;  // `배열 Arr의 0번째 원소에 10을 저장하라`
* Arr[idx] = 20; // `배열 Arr의 idx번째 원소에 20을 저장하라`

=> **`Index 범위 벗어나지 않게 조심하기!!`**



#### `배열 활용 예제1 : Gravity`

* 상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 낙차가 큰 상자를 구하여 그 낙차를 리턴 하는 프로그램을 작성하시오
* 중력은 회전이 완료된 후 적용된다.
* 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
* 방의 가로길이는 항상 100 이며, 세로 길이도 항상 100 이다.
* 즉, 상자는 최소 0,  최대 100 높이로 쌓을 수 있다.

`그림 설명`

* 아래 `예)` 총 26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A 상자의 낙차가 7로 가장 크므로 7을 리턴하면 된다.

* 회전 결과, B 상자의 낙차는 6,  C 상자의 낙차는 1이다.

  ![1550110487567](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550110487567.png)

* 입력

  * data[100] : 회전하기 전 상자들이 쌓여있는 모양을 나타내는 data. 앞의 예시에서는 [7, 4, 2, 0, 0, 6, 0, 7, 0] 이 된다.

* 사용 코드

  * data 배열은 랜덤하게 채워진다.
  * main 함수를 작성해보자

  ```python
  def build_data(data):
  	for i in range(0, 100): # from 0 to 99
  		data[i] <- random number
  
  if __name__=="__main__":
  	int data[100];
  	for i in range(0, 100): # from 0 to 99
  		build_data(data)
  		//이곳에 계산하는 코드 작성
  		print _result
  ```

  ```python
  arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
  maxH = 0
  for i in range(0, 100):
      height = len(arr)-1-i
      cnt = 0
      for j in range(i+1, len(arr)):
          if arr[i] <=arr[j]: cnt += 1
      height -= cnt
      maxH = max(height, maxH)
  
  print(maxH)
  ```


#### `Baby-gin Game`

`설명`

* 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를  run 이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet 이라고 한다.
* 그리고, 6장의 카드가 run 과 triplet 로만 구성된 경우를 baby-gin 으로 부른다.
* 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.

`입력 예)`

* 667767은 두 개의 triplet 이므로 baby-gin 이다. (666, 777)
* 054060은 한 개의 run 과 한 개의 triplet 이므로 역시 baby-gin 이다. (456, 000)
* 101123은 한 개의 triplet 가 존재하나, 023이 run 이 아니므로 baby-gin 이 아니다. (123을 run 으로 사용하더라도 011이 run 이나 triplet 가 아님)

##### `6자리의 숫자를 입력 받아 어떻게 Baby-gin 여부를 찾을 것인가?`





### `완전검색`

------

* 완전 검색 방법은 문제의 해법으로 생각 할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법이다.

* Brute-force 혹은 generate-and-test 기법이라고도 불리운다.
* 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다.
* 일반적으로 경우의 수가 상대적으로 작을 때 유용하다.

#### `완전 검색으로 시작하라!`

* 모든 경우의 수를 생성하고 테스트 하기 때문에 **수행 속도는 느리지만, 해답을 찾아내지 못 할 확률이 작다.**
* 자격 검정 평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다.

#### `완전 검색을 활용한 Baby-gin 접근`

##### `고려할 수 있는 모든 경우의 수 생성하기`

* 6개의 숫자로 만들 수 있는 모든 숫자 나열 (중복 포함)

* `예)` 입력으로 [2, 3, 5, 7, 7, 7] 을 받았을 경우, 아래와 같이 순열을 생성할 수 있다.

  ![1550111895228](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550111895228.png)


##### `해답 테스트하기`

* 앞의 3자리와 뒤의 3자리를 잘라, run 와 triplet 여부를 테스트하고, 최종적으로 baby-gin 을 판단한다.

![1550111976041](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550111976041.png)

#### `순열을 어떻게 생성 할 것인가`

##### `순열`

* 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것

* 서로 다른 n 개중 r 개를 택하는 순열은 아래와 같이 표현한다.

  `nPr`

* 그리고 `nPr`은 다음과 같은 식이 성립한다.

  `nPr = n * (n-1) * (n-2) * ... * (n-r+1)`

* `nPn = n!` 이라고 표기하며 Factorial 이라 부른다.

  `n! = n * (n-1) * (n-2) * ... * 2 * 1`

##### `중복순열`

```python
arr = 'ABCD'

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i], arr[j])
```



##### `중복되지 않는 순열`

```
arr = 'ABCD'

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        for k in range(len(arr)):
            if k == i or k == j: continue
        print(arr[i], arr[j])
```







##### `예) {1, 2, 3} 을 포함하는 모든 순열을 생성하는 함수`

* 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop 을 이용해 아래와 같이 구현할 수 있다.

  ```python
  for i1 in range(1, 4):
      for i2 in range(1, 4):
          if i2 != i1:
              for i3 in range(1, 4):
                  if i3 != i1 anf i3 != i2:
                      print(i1, i2, i3)
  ```


### `탐욕 알고리즘(Greedy Algorithm)`

------

* 탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법

* 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
* 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없다.
* 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.

#### `탐욕 알고리즘의 동작과정`

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합 (Solution Set) 에 추가한다.
2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는지를 검사한다.
3. 해 검사: 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면, `1`의 해 선택부터 다시 시작한다.

#### `탐욕 알고리즘의 예`

##### `거스름돈 줄이기`

* 어떻게 하면 손님에게 거스름돈으로 주는 지폐와 동전의 갯수를 최소한으로 줄일 수 있을까?
  1. 해 선택 : 여기에서는 멀리 내다볼 것 없이 가장 좋은 해를 선택한다. 단위가 큰 동전으로만 거스름돈을 만들면 도전의 개수가 줄어드므로 현재 고를 수 있는 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가한다.
  2. 실행 가능성 검사 : 거스름돈이 손님에게 내드려야 할 액수를 초과하는지 확인한다. 초과한다면 마지막에 추가한 동전을 거스름돈에서 빼고, `1 `로 돌아가서 현재보다 한 단계 작은 단위의 동전을 추가한다.
  3. 해 검사 : 거스름돈 문제의 해는 당연히 거스름돈이 손님에게 내드려야 하는 액수와 일치하는 셈이다. 더 드려도, 덜 드려도 안되기 때문에 거스름돈을 확인해서 액수에 모자라면 다시 `1` 로 돌아가서 거스름돈에 추가할 동전을 고른다.                                                                                                                                             

##### `완전 검색이 아닌 방법으로 풀어보자.`

* 6개의 숫자는 6자리의 정수 값으로 입력된다.

* counts 배열의 각 원소를 체크하여 run 과 triplet 및 baby-gin 여부를 판단한다.

  ![1550118781664](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550118781664.png)

* 구현 예

  ```python
  num = 456789 # Baby Gin 확인할 6자리 수
  c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
  
  for i in range(6):
      c[num % 10] += 1
      num //= 10
      
  i = 0
  tri = run = 0
  while i < 10:
      if c[i] >= 3: # triplet 조사 후 데이터 삭제
          c[i] -=3
          tri += 1
          continue
      if c[i] >= 1 and c[i+1] >=1 and c[i+2] >=1: # run 조사 후 데이터 삭제
          c[i] -= 1
          c[i+1] -= 1
          c[i+2] -= 1
          run += 1
          continue
      i += 1
  
  if run + tri == 2 : print("Baby Gin")
  else : print("Lose")
  ```


## `정렬의 종류`

### `대표적인 정렬 방식의 종류`

* 버블 정렬
* 카운팅 정렬
* 선택 정렬
* 퀵 정렬
* 삽입 정렬
* 병합 정렬



### `버블 정렬 (Bubble Sort)`

​	: 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

#### `정렬 과정` 

* 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
* 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
* 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.

#### `시간 복잡도`

* `O(n**2)`

#### `버블 정렬 과정`

![1550121875878](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550121875878.png)

![1550121890004](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550121890004.png)



![1550121906627](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550121906627.png)

![1550121922213](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550121922213.png)

#### `배열을 활용한 버블 정렬`

* 앞서 살펴 본 정렬 과정을 코드로 구현하면 아래와 같다.

  ```python
  arr = [55, 7, 78, 12, 42]
  
  def Bubble_sort(arr):
      for i in range(len(arr)-1, 0, -1):
          for j in range(i):
              if arr[j]>arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
      return arr
  print(Bubble_sort(arr))
  ```





### `카운팅 정렬 (Count Sort)`

​	: 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

#### `제한 사항`

* 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
* 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.

#### `시간 복잡도`

* `O(n+k)` : n 은 리스트 길이, k 는 정수의 최대값



#### `카운팅 정렬 과정`

![1550122452371](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122452371.png)

![1550122475771](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122475771.png)

![1550122486687](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122486687.png)

![1550122498442](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122498442.png)

![1550122508501](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122508501.png)

![1550122518146](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122518146.png)

![1550122529564](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122529564.png)

![1550122539389](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122539389.png)

![1550122549339](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122549339.png)

![1550122600517](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1550122600517.png)

* 앞서 살펴 본 정렬 과정을 코드로 구현하면 아래와 같다.

  ```python
  K = 4
  arr = [0, 4, 1, 3, 1, 2, 4, 1] 
  cnt = [0] * (K + 1)
  
  # 빈도수 계산
  for val in arr:
      cnt[val] += 1
  print(cnt)
  
  idx = 0
  for i in range(K + 1):
      for j in range(cnt[i]):
          arr[idx] = i
          idx += 1
  print(arr)
  ```

  ```python
  K = 4
  arr = [0, 4, 1, 3, 1, 2, 4, 1] 
  cnt = [0] * (K + 1)
  
  # 빈도수 계산
  for val in arr:
      cnt[val] += 1
  print(cnt)
  
  # 누적 빈도수
  for i in range(1, K + 1):
      cnt[i] = cnt[i-1] + cnt[i]
  print(cnt)
  ```

  ```python
  K = 4
  arr = [0, 4, 1, 3, 1, 2, 4, 1] 
  cnt = [0] * (K + 1)
  sorted = [0] * len(arr)
  
  # 빈도수 계산
  for val in arr:
      cnt[val] += 1
  
  # 누적 빈도수
  for i in range(1, K + 1):
      cnt[i] = cnt[i-1] + cnt[i]
      
  # 정렬
  for i in range(len(arr)-1, -1, -1):
      cnt[arr[i]] -= 1
      sorted[cnt[arr[i]]] = arr[i]
  
  print(sorted)
  ```
