# [Silver II] 예산 - 2512 

[문제 링크](https://www.acmicpc.net/problem/2512) 

### 성능 요약

메모리: 35500 KB, 시간: 48 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2026년 3월 8일 18:28:11

### 문제 설명

<p>국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 <strong>가능한 한 최대의</strong> 총 예산을 다음과 같은 방법으로 배정한다.</p>

<ol>
	<li>모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.</li>
	<li>모든 요청이 배정될 수 없는 경우에는 특정한 <strong>정수</strong> 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. </li>
</ol>

<p>예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. </p>

<p>여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. </p>

### 출력 

 <p>첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. </p>

---

### 🔧 Fail log

#### 접근 아이디어
- 전체 예산 합이 총 예산 이하라면 최대 요청액이 곧 상한선
- 그렇지 않다면, `budget // n` 으로 초기 상한선을 추정하고 이분탐색으로 상한선 이하 / 이상 그룹을 나눠 상한선을 계산

#### 알고리즘 판단 근거
- 상한선을 기준으로 배열을 두 구간으로 나눌 수 있으므로 `bisect` 활용 가능하다고 판단
- 정렬 후 이분탐색: `O(n log n)`

#### 시간 복잡도
- 시간복잡도: `O(n log n)`


---

### 오답

#### 오답 유형
- WA (Wrong Answer)

#### 초기 코드 (1차 시도)
```python
import sys
from bisect import bisect_right

input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
requests.sort()
budget = int(input())

total = sum(requests)
ideal = budget//n

if total <= budget:
    answer = max(requests)
else:
    idx = bisect_right(requests, ideal)
    left = requests[:idx]
    right = requests[idx:]
    answer = (budget-sum(left))//len(right)

print(answer)
```

#### 오답 원인

- 초기 상한선 추정값 `ideal = budget // n` 이 실제 정답보다 작을 수 있음.
- 예시:
```
4
1 2 3 100
budget = 10
```
- `ideal = 10 // 4 = 2`
- `bisect_right([1,2,3,100], 2)` → idx=2
- `left=[1,2]`, `right=[3,100]`
- `answer = (10-3) // 2 = 3`

실제 정답은 `4`가 나온다.

- `budget // n`은 예산을 n등분한 하한일 뿐 실제 상한선의 상한이 아니었다.  
- 작은 요청액이 많을수록 남은 예산이 커져 실제 상한선은 `budget // n` 보다 높아질 수 있다

---
### 해결 방법
- 상한선 후보 범위를 `0 ~ max(requests)`로 잡고, `total_cost(cap) <= budget`을 만족하는 최대 `cap`을 이진탐색으로 탐색
- `budget // n`으로 상한선을 고정시키는 대신, 상한선 값 자체를 탐색 대상으로 바꿔서 해결하였음
- `total_cost(cap) <= budget`이면 `answer`를 갱신하고 상한선을 더 높여볼 수 있으므로 `start = cap + 1`, 초과하면 `end = cap - 1`로 범위를 좁힘

---
### 다른 사람 풀이에서 배운 점

이진탐색 대신 **그리디**로도 동일하게 풀 수 있다.
- 정렬된 배열을 앞에서부터 순회하면서, 매 단계마다 남은 예산을 남은 지방 수로 나눠 상한선을 재계산함  
- 현재 요청액이 상한선 이하면 그대로 지급하고 예산을 차감, 초과하면 그 상한선이 정답.

```python
budgets.sort()
for i in range(total_regions):
    limit = total_budget // (total_regions - i)
    if budgets[i] <= limit:
        total_budget -= budgets[i]
    else:
        print(limit)
        exit()
print(budgets[-1])
```

- 내 첫 번째 접근과 아이디어는 동일했지만 핵심 차이는 **상한선을 매 단계마다 재계산한다는 것**이었음
- `budget // n`을 고정으로 사용하지 않고 `total_budget // (total_regions - i)`으로 계산하여 앞에서 적게 요청한 지방을 처리할수록 남은 예산이 정확히 반영되어 상한선이 올바르게 수렴할 수 있었음

**복잡도 비교**
| 풀이 | 시간복잡도 |
|------|-----------|
| 그리디 | `O(n log n)` |
| 이진탐색 | `O(n log m)`|

- 이 문제의 제약조건(n, m ≤ 10,000)에서는 사실상 동일함
