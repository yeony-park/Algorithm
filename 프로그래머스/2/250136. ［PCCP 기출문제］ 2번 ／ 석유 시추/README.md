# [level 2] [PCCP 기출문제] 2번 / 석유 시추 - 250136 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/250136) 

### 성능 요약

메모리: 12.9 MB, 시간: 315.00 ms

### 구분

코딩테스트 연습 > PCCP 기출문제

### 채점결과

정확성: 60.0<br/>효율성: 40.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 03월 25일 11:49:17

### 문제 설명

<p><strong>[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]</strong></p>

<p>세로길이가 <code>n</code> 가로길이가 <code>m</code>인 격자 모양의 땅 속에서 석유가 발견되었습니다. 석유는 여러 덩어리로 나누어 묻혀있습니다. 당신이 시추관을 수직으로 <strong>단 하나만</strong> 뚫을 수 있을 때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚫을 수 없습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/beb862a9-5382-4f61-adae-bd6e9503c014/%E1%84%89%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B2%E1%84%89%E1%85%B5%E1%84%8E%E1%85%AE-1.drawio.png" title="" alt="석유시추-1.drawio.png"></p>

<p>예를 들어 가로가 8, 세로가 5인 격자 모양의 땅 속에 위 그림처럼 석유가 발견되었다고 가정하겠습니다. 상, 하, 좌, 우로 연결된 석유는 하나의 덩어리이며, 석유 덩어리의 크기는 덩어리에 포함된 칸의 수입니다. 그림에서 석유 덩어리의 크기는 왼쪽부터 8, 7, 2입니다. </p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0b10a9f6-6d98-44d6-a342-f984ea47315c/%E1%84%89%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B2%E1%84%89%E1%85%B5%E1%84%8E%E1%85%AE-2.drawio.png" title="" alt="석유시추-2.drawio.png"></p>

<p>시추관은 위 그림처럼 설치한 위치 아래로 끝까지 뻗어나갑니다. 만약 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다. 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다. 시추관을 설치한 위치에 따라 뽑을 수 있는 석유량은 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시추관의 위치</th>
<th>획득한 덩어리</th>
<th>총 석유량</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>[8]</td>
<td>8</td>
</tr>
<tr>
<td>2</td>
<td>[8]</td>
<td>8</td>
</tr>
<tr>
<td>3</td>
<td>[8]</td>
<td>8</td>
</tr>
<tr>
<td>4</td>
<td>[7]</td>
<td>7</td>
</tr>
<tr>
<td>5</td>
<td>[7]</td>
<td>7</td>
</tr>
<tr>
<td>6</td>
<td>[7]</td>
<td>7</td>
</tr>
<tr>
<td>7</td>
<td>[7, 2]</td>
<td>9</td>
</tr>
<tr>
<td>8</td>
<td>[2]</td>
<td>2</td>
</tr>
</tbody>
      </table>
<p>오른쪽 그림처럼 7번 열에 시추관을 설치하면 크기가 7, 2인 덩어리의 석유를 얻어 뽑을 수 있는 석유량이 9로 가장 많습니다.</p>

<p>석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 <code>land</code>가 매개변수로 주어집니다. 이때 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>land</code>의 길이 = 땅의 세로길이 = <code>n</code> ≤ 500

<ul>
<li>1 ≤ <code>land[i]</code>의 길이 = 땅의 가로길이 = <code>m</code> ≤ 500</li>
<li><code>land[i][j]</code>는 <code>i+1</code>행 <code>j+1</code>열 땅의 정보를 나타냅니다.</li>
<li><code>land[i][j]</code>는 0 또는 1입니다.</li>
<li><code>land[i][j]</code>가 0이면 빈 땅을, 1이면 석유가 있는 땅을 의미합니다.</li>
</ul></li>
</ul>

<h6>정확성 테스트 케이스 제한사항</h6>

<ul>
<li>1 ≤ <code>land</code>의 길이 = 땅의 세로길이 = <code>n</code> ≤ 100

<ul>
<li>1 ≤ <code>land[i]</code>의 길이 = 땅의 가로길이 = <code>m</code> ≤ 100</li>
</ul></li>
</ul>

<h6>효율성 테스트 케이스 제한사항</h6>

<ul>
<li>주어진 조건 외 추가 제한사항 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>land</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]</td>
<td>9</td>
</tr>
<tr>
<td>[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제의 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/5e619c77-c940-46e6-9520-e5769e49194c/%E1%84%89%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B2%E1%84%89%E1%85%B5%E1%84%8E%E1%85%AE-3.drawio.png" title="" alt="석유시추-3.drawio.png"></p>

<p>시추관을 설치한 위치에 따라 뽑을 수 있는 석유는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시추관의 위치</th>
<th>획득한 덩어리</th>
<th>총 석유량</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>[12]</td>
<td>12</td>
</tr>
<tr>
<td>2</td>
<td>[12]</td>
<td>12</td>
</tr>
<tr>
<td>3</td>
<td>[3, 12]</td>
<td>15</td>
</tr>
<tr>
<td>4</td>
<td>[2, 12]</td>
<td>14</td>
</tr>
<tr>
<td>5</td>
<td>[2, 12]</td>
<td>14</td>
</tr>
<tr>
<td>6</td>
<td>[2, 1, 1, 12]</td>
<td>16</td>
</tr>
</tbody>
      </table>
<p>6번 열에 시추관을 설치하면 크기가 2, 1, 1, 12인 덩어리의 석유를 얻어 뽑을 수 있는 석유량이 16으로 가장 많습니다. 따라서 <code>16</code>을 return 해야 합니다.</p>

<hr>

<p><strong>제한시간 안내</strong></p>

<ul>
<li>정확성 테스트 : 10초</li>
<li>효율성 테스트 : 언어별로 작성된 정답 코드의 실행 시간의 적정 배수</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
---
### 🔧 fail log
#### 아이디어
- 처음에 틀린 코드는 실패.py 참고
- 각 열마다 시추를 시도한다고 가정하고 해당 열의 모든 행에서 DFS를 수행해 석유량을 계산하려고 했음
- 한 열 탐색이 끝날 때마다 원본 `land`를 유지하기 위해 `deepcopy`로 그래프를 복원했음
- DFS 중 방문한 석유 칸은 `0`으로 바꾸어 중복 탐색을 막으려 했음

#### 알고리즘 판단 근거
- 시추는 열 단위로 이루어지므로, 열마다 직접 탐색해서 얻을 수 있는 석유량을 구하면 된다고 판단함
- 연결된 석유 칸의 개수는 DFS로 구할 수 있다고 생각하여 DFS 사용

#### 복잡도
- 시간: O(m × n × m) 이상
- 공간: O(n × m)

### 오답
#### 오답 유형
- TLE
    - TLE : time limit exceed
    - 문제의 조건을 충분히 고려하지 않아 발생한 오답

#### 오답 원인
- 매 열마다 `deepcopy`를 수행해서 배열 전체를 반복 복사하고 DFS를 반복하다보니 같은 석유 덩어리를 여러 번 중복 탐색하는 문제가 있었다
- 재귀 DFS를 사용해서 깊이가 깊어질 경우 런타임 에러가 나기도 했다

#### 해결 방법
- 런타임에러는 `sys.recursionlimit`으로 해결했지만 시간 초과가 발생해 BFS로 재구성했다
- 열마다 탐색하지 않고, 전체 땅을 한 번만 순회하며 연결된 석유 덩어리를 BFS로 탐색함
- 각 덩어리에 고유 id를 붙이고 덩어리별 크기를 저장하여 마지막에 각 열에서 만나는 덩어리 id만 합산하는 방식으로 변경

#### 다른 사람의 코드에서 배운 점
- `visited`를 단순 방문 체크가 아니라 덩어리 id 저장 배열로 활용할 수 있다는 점을 배움
- 먼저 덩어리를 라벨링한 뒤, 이후 열 기준으로 필요한 덩어리만 합산하는 식으로 탐색과 집계를 분리할 수 있음
- 재귀 DFS보다 BFS가 깊이 제한 없이 더 안정적으로 동작

#### 아쉬웠던 점
- 처음부터 열 기준으로만 접근해서, 같은 덩어리를 여러 번 세고 있다는 점을 빨리 파악하지 못했다
- `deepcopy` 비용이 크다는 점을 간과했다
- 런타임 에러를 `setrecursionlimit`으로만 해결하려 했고, 시간복잡도 자체를 먼저 의심하지 못했다
