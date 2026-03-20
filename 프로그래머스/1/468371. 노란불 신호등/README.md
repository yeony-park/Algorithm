# [level 1] 노란불 신호등 - 468371 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/468371) 

### 성능 요약

메모리: 13 MB, 시간: 583.12 ms

### 구분

코딩테스트 연습 > 2025 카카오 하반기 1차

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 03월 19일 18:58:34

### 문제 설명

<p>어떤 도로에 차량 신호등이 <code>n</code>개 있습니다. 모든 신호등은 항상 초록불 → 노란불 → 빨간불 순서로 반복되며, 각 신호의 지속 시간은 신호등마다 다릅니다. 시간은 1초부터 시작하며, 각 신호등은 처음에는 초록불 상태로 시작합니다.</p>

<p>이 도로에서는 가끔 정전이 일어나는데, 모든 신호등이 모두 노란불이 되면 정전이 발생한다는 사실이 밝혀졌습니다.</p>

<p>예를 들어 신호등이 2개이고, 각 신호등의 주기가 다음과 같다고 가정해 보겠습니다.</p>
<table class="table">
        <thead><tr>
<th>신호등</th>
<th>초록불</th>
<th>노란불</th>
<th>빨간불</th>
</tr>
</thead>
        <tbody><tr>
<td>1번</td>
<td>2초</td>
<td>1초</td>
<td>2초</td>
</tr>
<tr>
<td>2번</td>
<td>5초</td>
<td>1초</td>
<td>1초</td>
</tr>
</tbody>
      </table>
<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/production/presigned_urls/69bc0131-0c4f-4609-9c47-4b649c40f860/%E1%84%89%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A9%E1%84%83%E1%85%B3%E1%86%BC-1.drawio.png" title="" alt="신호등-1.drawio.png"></p>

<p>위 그림과 같이 13초에 처음으로 두 신호등이 모두 노란불이 됩니다. </p>

<p>신호등 <code>n</code>개의 신호 주기를 담은 2차원 정수 배열 <code>signals</code>가 매개변수로 주어집니다. 모든 신호등이 노란불이 되는 가장 빠른 시각(초)을 return 하도록 solution 함수를 완성해 주세요. 만약 모든 신호등이 노란불이 되는 경우가 존재하지 않는다면 -1을 return 해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>signals</code>의 길이 = <code>n</code> ≤ 5

<ul>
<li><code>signals</code>의 원소는 <code>[G, Y, R]</code> 형태의 길이가 3인 정수 배열입니다. 순서대로 초록불, 노란불, 빨간불의 지속 시간을 의미합니다.</li>
<li>1 ≤ <code>G</code>, <code>Y</code>, <code>R</code> ≤ 18</li>
<li>3 ≤ <code>G + Y + R</code> ≤ 20</li>
</ul></li>
</ul>

<hr>

<h5>테스트 케이스 구성 안내</h5>

<p>아래는 테스트 케이스 구성을 나타냅니다. 각 그룹은 하나 이상의 하위 그룹으로 이루어져 있으며, 하위 그룹의 모든 테스트 케이스를 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.</p>
<table class="table">
        <thead><tr>
<th>그룹</th>
<th>총점</th>
<th>추가 제한 사항</th>
</tr>
</thead>
        <tbody><tr>
<td>#1</td>
<td>30%</td>
<td>신호등이 모두 노란불이 되는 시각이 20 이하인 정답이 존재합니다.</td>
</tr>
<tr>
<td>#2</td>
<td>30%</td>
<td>신호등이 모두 노란불이 되는 경우가 존재합니다.</td>
</tr>
<tr>
<td>#3</td>
<td>40%</td>
<td>추가 제한 사항 없음</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>signals</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[2, 1, 2], [5, 1, 1]]</td>
<td>13</td>
</tr>
<tr>
<td>[[2, 3, 2], [3, 1, 3], [2, 1, 1]]</td>
<td>11</td>
</tr>
<tr>
<td>[[3, 3, 3], [5, 4, 2], [2, 1, 2]]</td>
<td>193</td>
</tr>
<tr>
<td>[[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]</td>
<td>-1</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 설명의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>
<table class="table">
        <thead><tr>
<th>신호등</th>
<th>초록불</th>
<th>노란불</th>
<th>빨간불</th>
</tr>
</thead>
        <tbody><tr>
<td>1번</td>
<td>2초</td>
<td>3초</td>
<td>2초</td>
</tr>
<tr>
<td>2번</td>
<td>3초</td>
<td>1초</td>
<td>3초</td>
</tr>
<tr>
<td>3번</td>
<td>2초</td>
<td>1초</td>
<td>1초</td>
</tr>
</tbody>
      </table>
<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/production/presigned_urls/3011656a-b47d-40ea-baf4-15413beb7d44/%E1%84%89%E1%85%B5%E1%86%AB%E1%84%92%E1%85%A9%E1%84%83%E1%85%B3%E1%86%BC-2.drawio.png" title="" alt="신호등-2.drawio.png"></p>

<p>11초에 3개의 신호등이 모두 노란불이 됩니다.</p>

<p><strong>입출력 예 #3</strong></p>
<table class="table">
        <thead><tr>
<th>신호등</th>
<th>초록불</th>
<th>노란불</th>
<th>빨간불</th>
</tr>
</thead>
        <tbody><tr>
<td>1번</td>
<td>3초</td>
<td>3초</td>
<td>3초</td>
</tr>
<tr>
<td>2번</td>
<td>5초</td>
<td>4초</td>
<td>2초</td>
</tr>
<tr>
<td>3번</td>
<td>2초</td>
<td>1초</td>
<td>2초</td>
</tr>
</tbody>
      </table>
<p>193초에 3개의 신호등이 모두 노란불이 됩니다.</p>

<p><strong>입출력 예 #4</strong></p>

<p>모든 신호등이 노란불이 되는 경우가 존재하지 않으므로 -1을 return 해야 합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### 🔧 fail log

#### 아이디어
- 각 신호등의 상태가 초록 -> 노란 -> 빨간 순서로 반복되니까, 각 신호등의 한 주기 G+Y+R를 기준으로 노란불 구간을 문자열(1)로 표현하고 그 외는 0으로 표현
- 모든 신호등이 동시에 노란불인 시각은 각 신호등의 노란불 구간의 교집합과 같다고 생각하여 각 신호등의 상태 문자열을 만들어 AND처럼 겹치는 위치만 남기는 방식으로 풀이함
- 전체 상태는 각 신호등 주기의 최소공배수 시점 이후 반복되기 때문에 max_try = lcm까지만 탐색하도록 제한을 걸었다

#### 복잡도
- 시간: `O(n * max_try^2)`에 가깝게 동작한다
        - n은 신호등 개수, max_try는 최소공배수. ch2가 ch2 += '0'또는 '1' 문자열 누적 방식으로 작동해서 실제로는 비효율적이다
- 공간: O(max_try)

---
### 오답
#### 오답 유형
- WA 발생 (60점)

#### 오답 원인
- `max_try`를 임의로 200이라 설정해서 LCM 범위를 보장하지 못했다 -> 일부 테스트 케이스에서 오답이 발생하면서 60점이 기록됨
- 모든 신호등이 동시에 노란불이 되는 시각이 존재하는지 판단하려면 최소한 1~최소공배수(LCM) 구간을 확인해야 함

#### 해결 방법
- 각 신호등의 주기 G+Y+R을 `periods`에 넣어두고 최소공배수를 계산했다. 이를 max_try라고 정의해서 해결함

#### 아쉬웠던 점/개선할 점
- 문자열 전체를 만들어 교집합을 구하는 방식은 직관적이지만, 문자열을 한 글자씩 누적하는 방식이 비효율적이었다. G+Y+R이 20을 넘지않는다는 조건이 있어서 위와 같은 방식으로 일단 구현을 해야겠다고 생각했지만 실제로는 입력범위가 커질수록 성능상 불리해질 수 있다.
- 특정 시점 `t`에서 `t%max_try` 값을 이용해 노란불 구간인지 판별하는 방식이 더 간결하고 안정적이다

#### 다른 사람 코드에서 배운 점
- 전체 상태를 문자열로 비교하지 않고, 각 시간마다 모듈러 연산으로 상태를 판별함
- 핵심 아이디어는 각 신호등에 대해서
        - cycle = G + Y + R
        - mod = t % cycle
  형태로 현재 주기 내 위치를 계산
- 그 후 그 값이 노란불 구간에 포함되는지만 확인함
- 별도의 문자열을 만들 필요가 없어서 메모리 사용도 적고, 구현도 명확함
- `reduce(lcm, cycles)`로 여러 주기의 최소공배를 구할 수 있음
  
```python
from math import gcd
from functools import reduce

def lcm(a, b):
        return a * b // gcd(a, b)

def solution(signals):
        cycles = [g+y+r for g,y,r in signals]
        limit = reduce(lcm, cycles)

        for t in range(1, limit+1):
                ok = True
        for g, y, r in signals:
                cycle = g + y + r
                mod = t % cycle

                if not (g <= mod <= g+y-1):
                        ok = False
                        break
        if ok:
                return t+1 return -1
```

#### 추가로 배운 점
- 파이썬 버전에 따라 math 라이브러리에서 lcm 지원이 안 될 수 있으니 함수로 구현해야 함
