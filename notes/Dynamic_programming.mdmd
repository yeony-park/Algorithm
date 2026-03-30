# ![Tag](https://img.shields.io/badge/Tag-Dynamic%20Programming-2ea44f) 다이나믹 프로그래밍 (Dynamic Programming)

## 정의

* **메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상**시키는 알고리즘 설계 기법
* 이미 계산된 결과(작은 문제)를 별도의 메모리 영역에 저장하여 중복 계산을 방지
* 구현 방식 : **탑다운(Top-Down)** 과 **바텀업(Bottom-Up)**

---

# ![Tag](https://img.shields.io/badge/Tag-Conditions-2ea44f) 사용 조건

다음 두 조건을 **모두** 만족할 때 DP 적용 가능

| 조건 | 설명 |
|:---:|:---|
| **최적 부분 구조** (Optimal Substructure) | 큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 답을 모아 큰 문제를 해결 가능 |
| **중복되는 부분 문제** (Overlapping Subproblem) | 동일한 작은 문제를 반복적으로 해결해야 함 |

---

# ![Tag](https://img.shields.io/badge/Tag-Memoization-2ea44f) 메모이제이션 (Memoization)

* 한 번 계산한 결과를 메모리 공간에 기록해두는 기법 → **캐싱(Caching)** 이라고도 함
* 같은 문제를 다시 호출하면 메모해둔 결과를 그대로 반환
* **탑다운 방식에서 사용**

> 메모이제이션은 DP에만 국한된 개념이 아님. 계산 결과를 저장하는 넓은 의미의 기법임

---

# ![Tag](https://img.shields.io/badge/Tag-Top--Down%20vs%20Bottom--Up-2ea44f) 탑다운 vs 바텀업

| 구분 | 방식 | 구현 | 저장소 명칭 |
|:---:|:---:|:---:|:---:|
| **탑다운** | 하향식, 재귀 + 메모이제이션 | 재귀 함수 | 메모이제이션 테이블 |
| **바텀업** | 상향식, 반복문으로 작은 문제부터 해결 | 반복문 | **DP 테이블** |

> DP의 전형적인 형태는 **바텀업**

---

# ![Tag](https://img.shields.io/badge/Tag-Example-2ea44f) 예시 : 피보나치 수열

$$a_n = a_{n-1} + a_{n-2}, \quad a_1 = 1,\ a_2 = 1$$

단순 재귀로 구현 시 **지수 시간 복잡도** $O(2^N)$ → DP 적용 시 $O(N)$으로 감소

## 탑다운 (메모이제이션)

```python
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))
```

## 바텀업

```python
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

---

# ![Tag](https://img.shields.io/badge/Tag-DP%20vs%20Divide%20%26%20Conquer-2ea44f) DP vs 분할 정복

| 구분 | 최적 부분 구조 | 부분 문제 중복 |
|:---:|:---:|:---:|
| **DP** | ✅ | ✅ (중복 발생) |
| **분할 정복** | ✅ | ❌ (중복 없음) |

> 퀵 정렬 : Pivot이 자리를 잡으면 해당 위치를 다시 처리하지 않음 → 부분 문제 중복 없음

---

# ![Tag](https://img.shields.io/badge/Tag-Approach-2ea44f) DP 문제 접근 방법

1. 그리디 / 구현 / 완전 탐색으로 해결 가능한지 먼저 검토
2. 풀이가 떠오르지 않으면 **DP를 고려**
3. 재귀로 완전 탐색 먼저 작성 (탑다운) → 작은 문제의 답이 큰 문제에 재사용된다면 DP로 개선

---

# ![Tag](https://img.shields.io/badge/Tag-Time%20Complexity-2ea44f) 시간 복잡도 정리

| 구현 방법 | 시간 복잡도 | 비고 |
|:---:|:---:|:---|
| 단순 재귀 (피보나치) | $O(2^N)$ | 중복 계산 발생 |
| DP (메모이제이션 / 바텀업) | $O(N)$ | 각 부분 문제를 1회만 계산 |
| LIS (가장 긴 증가하는 부분 수열) | $O(N^2)$ | 이진 탐색 적용 시 $O(N \log N)$ |

---

## More details

[![Notion](https://img.shields.io/badge/Notion-Study%20Note-808080?logo=notion&logoColor=000000&labelColor=FFD700)](https://daily-archduke-be2.notion.site/3155e249d44e8046a7a4d0f022054419?source=copy_link)

## References

[![YouTube](https://img.shields.io/badge/YouTube-%EC%9D%B4%EC%BD%94%ED%85%8C%20%EA%B0%95%EC%9D%98-808080?logo=youtube&logoColor=FFFFFF&labelColor=FF0000)](https://youtu.be/5Lu34WIx2Us?si=jejBoxrdJrmrGYYr)
