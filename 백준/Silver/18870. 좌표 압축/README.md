# [Silver II] 좌표 압축 - 18870 

[문제 링크](https://www.acmicpc.net/problem/18870) 

### 성능 요약

메모리: 149248 KB, 시간: 1448 ms

### 분류

정렬, 값 / 좌표 압축

### 제출 일자

2026년 2월 26일 23:20:41

### 문제 설명

<p>수직선 위에 N개의 좌표 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.</p>

<p>X<sub>i</sub>를 좌표 압축한 결과 X'<sub>i</sub>의 값은 X<sub>i</sub> > X<sub>j</sub>를 만족하는 서로 다른 좌표 X<sub>j</sub>의 개수와 같아야 한다.</p>

<p>X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>에 좌표 압축을 적용한 결과 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>를 출력해보자.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다.</p>

<p>둘째 줄에는 공백 한 칸으로 구분된 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>을 공백 한 칸으로 구분해서 출력한다.</p>

---

### 🔧 Fail log

### 아이디어
- `num[i]보다 작은 값의 개수를 세면 압축된 좌표가 될 것이라 가정했다`

### 오답원인
#### 오답 유형
1) `WA`발생
- 문제 조건을 잘못 이해하여 오답이 발생했다
- 문제는 `num[i]`보다 작은 값이 몇 개인지 세는 것이 아니라 몇 종류인지를 구하는 것이었다
- `set()`으로 중복을 제거하여 해결하였다

2) `TLE` 발생
```python
import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))[:n]
result = []

for i in num:
    cnt = 0
    for j in set(num):
        if i > j:
            cnt += 1
    result.append(cnt)

print(*result, sep='\n')
```
- 이중 for문 O(N²) 구조로 인해 시간 초과

#### 해결방법
- `sorted(set(num))`으로 중복을 제거하고 정렬으 한 번에 처리한 뒤
- 딕셔너리로 기존 숫자 값, 압축값을 매핑하여 O(1) 조회

### 배운 점
- `sort()`는 리스트 전용 메서드이며 반환값이 `None`이다 -> `sorted_unq = set(num).sort()` 사용이 불가능함
- `set`에는 `sort()` 메서드가 없다
- 리스트 컴프리헨션이 `for + append`보다 일반적으로 더 빠르다
