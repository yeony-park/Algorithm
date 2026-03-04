# [Silver V] 단어 정렬 - 1181 

[문제 링크](https://www.acmicpc.net/problem/1181) 

### 성능 요약

메모리: 37532 KB, 시간: 76 ms

### 분류

문자열, 정렬

### 제출 일자

2026년 3월 5일 00:22:33

### 문제 설명

<p>알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.</p>

<ol>
	<li>길이가 짧은 것부터</li>
	<li>길이가 같으면 사전 순으로</li>
</ol>

<p>단, 중복된 단어는 하나만 남기고 제거해야 한다.</p>

### 입력 

 <p>첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.</p>

### 출력 

 <p>조건에 따라 정렬하여 단어들을 출력한다.</p>

---
### 🔧 Fail log

#### 접근 아이디어
- 단어를 길이별로 분류하여 리스트에 저장
- 길이별 리스트를 정렬 후 출력

#### 알고리즘 판단 근거
- 정렬 문제이므로 별도 알고리즘 불필요, 내장 sort 활용

#### 시간 복잡도
- 시간복잡도 : `O(n log n)`

---
### 오답
#### 오답 유형
- RE
- 초기 코드는 다음과 같았다
```python
import sys

input = sys.stdin.readline

n = int(input())
words = [[] for _ in range(50)]

for _ in range(n):
    w = input()
    if w not in words[len(w)]:
        words[len(w)].append(w)

for w in words:
    w.sort()

for w in words:
    if w != []:
        print("".join(w).strip())
```

#### 해결 방법
- `input().strip()` 으로 `\n` 제거
- 처음엔 이미 단어가 존재한다면 if 조건으로 처리했으나, 최종 코드에서는 `set`을 사용해 중복을 제거했다.
- 과도한 for 반복문 대신 `sorted(key=lambda x: (len(x), x))`으로 길이순, 사전순 정렬을 한 번에 처리했다.

#### 개선할 점
- `print('\n'.join(words))`로 print를 반복 호출하지 않고 한 번에 출력할 수 있다
