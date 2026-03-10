# [Bronze III] 삼각수의 합 - 2721 

[문제 링크](https://www.acmicpc.net/problem/2721) 

### 성능 요약

메모리: 32412 KB, 시간: 300 ms

### 분류

수학, 구현

### 제출 일자

2026년 3월 10일 21:42:26

### 문제 설명

<p>n번째 삼각수, T(n)은 1부터 n까지의 합이다. T(n) = 1 + ... + n. 이것은 삼각형 모양으로 표현할 수 있다. 아래 그림은 T(4)를 나타낸 것이다.</p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/tsum.png" style="height:90px; width:87px"></p>

<p>다음과 같은 식을 통해 가중치를 부여한 삼각수의 합을 구할 수 있다.</p>

<p>W(n) = Sum[k=1..n; k*T(k+1)]</p>

<p>n이 주어졌을 때, W(n)을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 정수 n 하나로 이루어져 있다. (1<=n<=300)</p>

### 출력 

 <p>각 테스트 케이스에 대해 W(n)을 한 줄에 하나씩 출력한다.</p>

---
### ✅ Solve log
#### 아쉬운 점 / 개선할 사안
- 처음에 Sum[k=1..n; k*T(k+1)]에 대한 이해를 잘못해서 calculate_Wn에 T(n) = 1+ ... + n값을 `tn`값으로 설정하고 인자로 넘겼다. 그래서 T(k+1)이 k마다 갱신되지 않는 문제가 있었다
- T(k+1) = (k+1)(k+2)/2 공식을 적용했다면 더 간결하게 접근이 가능했을텐데 제출 후에 생각났다.
- W(n)을 반복적으로 계산하는 구조인데, 바텀업 DP 방식으로 메모이제이션을 적용하면 O(n^2)이 O(n+T)로 개선이 가능할 것이다

#### 개선된 코드
```python
import sys
input = sys.stdin.readline

T = int(input())
cases = [int(input()) for _ in range(T)]
max_n = max(cases)

# W(n) 미리 다 계산
W = [0] * (max_n + 1)
for i in range(1, max_n + 1):
    W[i] = W[i-1] + i * ((i+1)*(i+2)//2)

for n in cases:
    print(W[n])
```

#### 복잡도

- 최초 풀이 : O(T * n²)
- 공식 적용 후 : O(T * n)
- 메모이제이션 적용 후 : O(max_n + T)
