# ![Tag](https://img.shields.io/badge/Tag-Sorting-2ea44f) 정렬 알고리즘

## 정의

* **정렬(Sorting)**: 데이터를 특정 기준에 따라 순서대로 나열하는 것
* 문제 상황에 따라 일반적으로 적절한 정렬 알고리즘이 공식처럼 사용됨

---

# ![Tag](https://img.shields.io/badge/Tag-Selection%20Sort-2ea44f) 선택 정렬 (Selection Sort)

## 개념

* 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택**해 맨 앞에 있는 데이터와 바꾸는 것을 반복
* 탐색 범위는 동작할 때마다 줄어들며, 매번 범위 내의 가장 작은 값을 찾기 위해 **선형 탐색** 수행

## 예시 흐름

```
[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
→ 0을 맨 앞 7과 교체 : [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
→ 1을 5와 교체        : [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]
→ 2를 9와 교체        : [0, 1, 2, 7, 3, 5, 6, 9, 4, 8]
→ ...반복...
→ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 코드

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
```

## 시간 복잡도

$$N + (N-1) + (N-2) + \cdots + 2 \approx O(N^2)$$

---

# ![Tag](https://img.shields.io/badge/Tag-Insertion%20Sort-2ea44f) 삽입 정렬 (Insertion Sort)

## 개념

* 처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입**
* 선택 정렬보다 구현 난이도는 높지만, 일반적으로 더 효율적으로 동작
* 현재 리스트가 **거의 정렬된 상태**라면 매우 빠르게 동작

## 예시 흐름

```
[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
→ 5를 적절한 위치에 삽입 : [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
→ 9는 제자리 유지        : [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
→ 0을 삽입               : [0, 5, 7, 9, 3, 1, 6, 2, 4, 8]
→ ...반복...
→ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 코드

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1씩 감소
        if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```

## 시간 복잡도

* 평균 / 최악: $O(N^2)$
* **최선 (거의 정렬된 경우)**: $O(N)$

---

# ![Tag](https://img.shields.io/badge/Tag-Quick%20Sort-2ea44f) 퀵 정렬 (Quick Sort)

## 개념

* **기준 데이터(Pivot)를 설정하고**, 그보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방식
* 일반적인 상황에서 **가장 많이 사용**되는 정렬 알고리즘
* 병합 정렬과 함께 대부분 프로그래밍 언어의 **정렬 라이브러리의 근간**이 됨
* 기본적으로 **첫 번째 데이터를 피벗**으로 설정

## 동작 방식

1. 피벗을 기준으로 왼쪽에서 피벗보다 큰 값, 오른쪽에서 피벗보다 작은 값을 탐색
2. 두 값의 위치를 교체
3. 탐색 위치가 **엇갈리면 피벗과 작은 데이터를 교체** → 분할(Partition) 완료
4. 피벗 기준으로 왼쪽/오른쪽 부분에 대해 **재귀적으로 반복**

## 코드 (기본)

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 피벗과 작은 데이터 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```

## 코드 (파이썬 간결 버전)

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

## 시간 복잡도

* 평균: $O(N \log N)$
* **최악**: $O(N^2)$ — 이미 정렬된 배열에서 첫 원소를 피벗으로 삼는 경우

---

# ![Tag](https://img.shields.io/badge/Tag-Counting%20Sort-2ea44f) 계수 정렬 (Counting Sort)

## 개념

* **데이터의 크기 범위가 제한**되어 정수로 표현할 수 있을 때만 사용 가능
* 값의 등장 횟수를 카운팅하여 정렬 → 별도의 비교 연산 없음
* **동일한 값이 여러 개 등장할 때** 매우 효과적 (e.g. 성적 정렬)

## 동작 방식

1. 데이터의 최솟값 ~ 최댓값 범위의 카운트 배열 생성
2. 각 데이터 값에 해당하는 인덱스를 1씩 증가
3. 카운트 배열을 순서대로 읽으며 인덱스를 횟수만큼 출력

## 코드

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```

## 시간 복잡도

* 시간 복잡도: $O(N + K)$ (K = 데이터 최댓값)
* 공간 복잡도: $O(N + K)$
* 단, 범위가 매우 넓을 경우 **공간 낭비**가 심할 수 있음

---

# ![Tag](https://img.shields.io/badge/Tag-Comparison-2ea44f) 정렬 알고리즘 비교

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징 |
|:-----------:|:--------------:|:---------:|:---|
| 선택 정렬 | $O(N^2)$ | $O(N)$ | 아이디어가 매우 간단 |
| 삽입 정렬 | $O(N^2)$ | $O(N)$ | 거의 정렬된 경우 가장 빠름 ($O(N)$) |
| 퀵 정렬 | $O(N \log N)$ | $O(N)$ | 대부분의 경우 가장 적합 / 최악 $O(N^2)$ 주의 |
| 계수 정렬 | $O(N + K)$ | $O(N + K)$ | 범위가 한정된 정수에만 사용 가능, 매우 빠름 |

> 대부분의 표준 정렬 라이브러리는 최악의 경우에도 $O(N \log N)$을 보장하도록 설계되어 있음

---

## More details

[![Notion](https://img.shields.io/badge/Notion-Study%20Note-808080?logo=notion&logoColor=000000&labelColor=FFD700)](https://daily-archduke-be2.notion.site/3155e249d44e8091ac90dc827dccc9c6?source=copy_link)

## References

[![YouTube](https://img.shields.io/badge/YouTube-%EC%9D%B4%EC%BD%94%ED%85%8C%20%EA%B0%95%EC%9D%98-808080?logo=youtube&logoColor=FFFFFF&labelColor=FF0000)](https://www.youtube.com/@dongbinna)
