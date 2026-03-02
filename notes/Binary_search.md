# ![Tag](https://img.shields.io/badge/Tag-Binary%20Search-2ea44f) 이진 탐색 알고리즘 (Binary Search)

## 정의

* **순차 탐색**: 리스트 안에서 특정 데이터를 찾기 위해 **앞에서부터 하나씩 확인**하는 방법
* **이진 탐색**: 정렬된 리스트에서 **탐색 범위를 절반씩 좁혀가며** 데이터를 탐색하는 방법
  * 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정 → $O(\log N)$ 시간복잡도 보장

---

# ![Tag](https://img.shields.io/badge/Tag-How%20It%20Works-2ea44f) 동작 방식

정렬된 10개의 데이터 중 값이 **4**인 원소를 찾는 예시

```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
 시작점:0  끝점:9  중간점:4 → arr[4]=8 > 4 → 끝점을 중간점 왼쪽으로 이동

[0, 2, 4, 6, 8, ...]
 시작점:0  끝점:3  중간점:1 → arr[1]=2 < 4 → 시작점을 중간점 오른쪽으로 이동

[0, 2, 4, 6, ...]
 시작점:2  끝점:3  중간점:2 → arr[2]=4 == 4 → 탐색 완료!
```

---

# ![Tag](https://img.shields.io/badge/Tag-Time%20Complexity-2ea44f) 시간 복잡도

* 단계마다 탐색 범위를 **절반으로** 나누므로 연산 횟수는 $\log_{2} N$에 비례

| 초기 데이터 수 | 1단계 후 | 2단계 후 | 3단계 후 |
|:---:|:---:|:---:|:---:|
| 32개 | 16개 | 8개 | 4개 |

$$O(\log N)$$

---

# ![Tag](https://img.shields.io/badge/Tag-Implementation-2ea44f) 구현

## 재귀적 구현

```python
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

## 반복문 구현

```python
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

---

# ![Tag](https://img.shields.io/badge/Tag-bisect-2ea44f) 파이썬 이진 탐색 라이브러리 `bisect`

* `bisect_left(a, x)` : 정렬된 순서를 유지하면서 배열 `a`에 `x`를 삽입할 **가장 왼쪽 인덱스** 반환
* `bisect_right(a, x)` : 정렬된 순서를 유지하면서 배열 `a`에 `x`를 삽입할 **가장 오른쪽 인덱스** 반환

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))   # 2
print(bisect_right(a, x))  # 4
```

## 값이 특정 범위에 속하는 데이터 개수 구하기

```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))   # 2  → 값이 4인 데이터 개수
print(count_by_range(a, -1, 3))  # 6  → 값이 [-1, 3] 범위인 데이터 개수
```

---

# ![Tag](https://img.shields.io/badge/Tag-Parametric%20Search-2ea44f) 파라메트릭 서치 (Parametric Search)

* 최적화 문제를 **결정 문제**('예' 혹은 '아니오')로 바꾸어 해결하는 기법
* 탐색 범위를 좁혀가며 특정 조건을 만족하는 **가장 알맞은 값**을 빠르게 탐색
* 코딩 테스트에서 파라메트릭 서치 문제는 **이진 탐색으로 해결**하는 경우가 많음

> 💡 탐색 범위가 **0 ~ 10억**처럼 매우 크다면 → 이진 탐색을 가장 먼저 떠올릴 것

---

# ![Tag](https://img.shields.io/badge/Tag-Time%20Complexity-2ea44f) 정리

| 방법 | 시간 복잡도 | 비고 |
|:---:|:---:|:---|
| 순차 탐색 | $O(N)$ | 정렬 불필요 |
| 이진 탐색 | $O(\log N)$ | **정렬된 배열** 필수 |
| bisect 라이브러리 | $O(\log N)$ | 파이썬 내장, 범위 탐색에 유용 |

---

## More details

[![Notion](https://img.shields.io/badge/Notion-Study%20Note-808080?logo=notion&logoColor=000000&labelColor=FFD700)](https://www.notion.so/3155e249d44e8017adfad89591dd12b1)

## References

[![YouTube](https://img.shields.io/badge/YouTube-%EC%9D%B4%EC%BD%94%ED%85%8C%20%EA%B0%95%EC%9D%98-808080?logo=youtube&logoColor=FFFFFF&labelColor=FF0000)](https://youtu.be/94RC-DsGMLo?si=U8E46H3tZgF9VWSb)
