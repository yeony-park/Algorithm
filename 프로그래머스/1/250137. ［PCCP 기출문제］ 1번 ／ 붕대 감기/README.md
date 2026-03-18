# [level 1] [PCCP 기출문제] 1번 / 붕대 감기 - 250137 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/250137?language=python3) 

### 성능 요약

메모리: 9.23 MB, 시간: 0.31 ms

### 구분

코딩테스트 연습 > PCCP 기출문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2026년 03월 18일 20:53:07

### 문제 설명

<p>어떤 게임에는 <code>붕대 감기</code>라는 기술이 있습니다.</p>

<p><code>붕대 감기</code>는 <code>t</code>초 동안 붕대를 감으면서 1초마다 <code>x</code>만큼의 체력을 회복합니다. <code>t</code>초 연속으로 붕대를 감는 데 성공한다면 <code>y</code>만큼의 체력을 추가로 회복합니다. 게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능합니다.</p>

<p>기술을 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력을 회복할 수 없습니다. 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 <code>붕대 감기</code>를 다시 사용하며, 연속 성공 시간이 0으로 초기화됩니다.</p>

<p>몬스터의 공격을 받으면 정해진 피해량만큼 현재 체력이 줄어듭니다. 이때, 현재 체력이 0 이하가 되면 캐릭터가 죽으며 더 이상 체력을 회복할 수 없습니다.</p>

<p>당신은 <code>붕대감기</code> 기술의 정보, 캐릭터가 가진 최대 체력과 몬스터의 공격 패턴이 주어질 때 캐릭터가 끝까지 생존할 수 있는지 궁금합니다.</p>

<p><code>붕대 감기</code> 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열 <code>bandage</code>와 최대 체력을 의미하는 정수 <code>health</code>, 몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열 <code>attacks</code>가 매개변수로 주어집니다. 모든 공격이 끝난 직후 남은 체력을 return 하도록 solution 함수를 완성해 주세요. <strong>만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return 해주세요.</strong></p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>bandage</code>는 [<code>시전 시간</code>, <code>초당 회복량</code>, <code>추가 회복량</code>] 형태의 길이가 3인 정수 배열입니다.

<ul>
<li>1 ≤ <code>시전 시간</code> = <code>t</code> ≤ 50</li>
<li>1 ≤ <code>초당 회복량</code> = <code>x</code> ≤ 100</li>
<li>1 ≤ <code>추가 회복량</code> = <code>y</code> ≤ 100</li>
</ul></li>
<li>1 ≤ <code>health</code> ≤ 1,000</li>
<li>1 ≤ <code>attacks</code>의 길이 ≤ 100

<ul>
<li><code>attacks[i]</code>는 [<code>공격 시간</code>, <code>피해량</code>] 형태의 길이가 2인 정수 배열입니다.</li>
<li><code>attacks</code>는 <code>공격 시간</code>을 기준으로 오름차순 정렬된 상태입니다.</li>
<li><code>attacks</code>의 <code>공격 시간</code>은 모두 다릅니다.</li>
<li>1 ≤ <code>공격 시간</code> ≤ 1,000</li>
<li>1 ≤ <code>피해량</code> ≤ 100</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bandage</th>
<th>health</th>
<th>attacks</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[5, 1, 5]</td>
<td>30</td>
<td>[[2, 10], [9, 15], [10, 5], [11, 5]]</td>
<td>5</td>
</tr>
<tr>
<td>[3, 2, 7]</td>
<td>20</td>
<td>[[1, 15], [5, 16], [8, 6]]</td>
<td>-1</td>
</tr>
<tr>
<td>[4, 2, 7]</td>
<td>20</td>
<td>[[1, 15], [5, 16], [8, 6]]</td>
<td>-1</td>
</tr>
<tr>
<td>[1, 1, 1]</td>
<td>5</td>
<td>[[1, 2], [3, 2]]</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>몬스터의 마지막 공격은 11초에 이루어집니다. 0초부터 11초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>30</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>30(+0)</td>
<td>1</td>
<td>X</td>
<td>최대 체력 이상의 체력을 가질 수 없습니다.</td>
</tr>
<tr>
<td>2</td>
<td>20(-10)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>3</td>
<td>21(+1)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>22(+1)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>23(+1)</td>
<td>3</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>24(+1)</td>
<td>4</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>30(+6)</td>
<td>5 → 0</td>
<td>X</td>
<td>5초 연속 성공해 체력을 5만큼 추가 회복하고 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>8</td>
<td>30(+0)</td>
<td>1</td>
<td>X</td>
<td>최대 체력 이상의 체력을 가질 수 없습니다.</td>
</tr>
<tr>
<td>9</td>
<td>15(-15)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>10</td>
<td>10(-5)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>11</td>
<td>5(-5)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 마지막 공격입니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 마지막 공격 직후 캐릭터의 체력은 5입니다. 따라서 <code>5</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>몬스터의 마지막 공격은 8초에 이루어집니다. 0초부터 8초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>20</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>5(-15)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>2</td>
<td>7(+2)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>9(+2)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>18(+9)</td>
<td>3 → 0</td>
<td>X</td>
<td>3초 연속 성공해 체력을 7만큼 추가 회복하고 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>5</td>
<td>2(-16)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>6</td>
<td>4(+2)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>6(+2)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>0(-6)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 마지막 공격을 받아 캐릭터의 체력이 0 이하가 됩니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다. 따라서 <code>-1</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>몬스터의 마지막 공격은 8초에 이루어집니다. 0초부터 5초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>20</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>5(-15)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>2</td>
<td>7(+2)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>9(+2)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>11(+2)</td>
<td>3</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>-5(-16)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다. 따라서 <code>-1</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #4</strong></p>

<p>몬스터의 마지막 공격은 3초에 이루어집니다. 0초부터 3초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>5</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>3(-2)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>2</td>
<td>5(+2)</td>
<td>1 → 0</td>
<td>X</td>
<td>1초 연속 성공해 체력을 1만큼 추가 회복하고 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>3</td>
<td>3(-2)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 마지막 공격입니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 마지막 공격 직후 캐릭터의 체력은 3입니다. 따라서 <code>3</code>을 return 해야 합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---
### 🔧 fail log

#### 아이디어
- 시간을 1초씩 증가시키며 캐릭터의 체력을 시뮬레이션한다.
- `success` 변수로 붕대 감기 연속 성공 시간을 관리한다.
- 공격 시간이 되면 체력을 감소시키고, 붕대 감기 연속 성공 시간을 0으로 초기화한다.
- 공격 시간이 아니면 초당 회복량 `x`만큼 회복하고, `t`초 연속 성공 시 추가 회복량 `y`를 더한다.
- 체력은 항상 최대 체력 `health`를 넘지 않도록 제한한다.

#### 알고리즘 판단 근거
- 이 문제는 특정 규칙에 따라 시간 순서대로 상태가 변하는 시뮬레이션 문제이다.
- 각 초마다 해야 할 일은 다음 둘 중 하나뿐이다.
  - 공격을 받는다.
  - 공격을 받지 않으면 회복한다.
- 공격 정보는 공격 시간을 기준으로 오름차순 정렬되어 있으므로, 현재 처리해야 할 공격 하나만 가리키는 인덱스를 두고 순차적으로 처리하면 된다.
- 따라서 시간을 1초부터 마지막 공격 시간까지 순회하면서 상태를 갱신하는 방식이 적절하다.

#### 복잡도
- 시간: `O(last_attack_time)`
- 공간: `O(1)`

### 오답

#### 오답 유형
- WA 발생
  - WA : wrong answer
  - 시뮬레이션 과정에서 상태 갱신 조건을 잘못 처리하여 발생한 오답

#### 오답 원인
- 처음에는 현재 시간마다 `attacks` 전체를 순회하는 방식으로 구현했다.
- 이 경우 특정 초에 공격이 없는 상황에서도 `attacks`의 모든 원소에 대해 공격을 받지 않는 `else` 조건이 반복 실행되어, 한 초에 회복이 여러 번 적용되는 문제가 발생했다.
- 이후 공격 배열을 순차적으로 처리하기 위해 `idx`를 도입했지만, `idx += 1`을 매 초마다 수행하는 실수를 했다.
- `idx`는 시간 인덱스가 아니라 현재 처리 중인 공격 인덱스이므로, 실제 공격을 처리한 경우에만 증가해야 한다.
- 공격이 없는 시간에도 `idx`를 증가시키면 아직 처리하지 않은 공격을 건너뛰게 되어 시뮬레이션 결과가 잘못된다.
- 추가로, 죽는 조건을 `h < 0`으로 처리하면 체력이 정확히 0이 되는 경우를 놓칠 수 있다.
- 문제에서는 체력이 `0 이하`가 되면 죽는다고 했으므로 `h <= 0`으로 판단해야 한다.

#### 해결 방법
- 시간을 1초씩 순회하면서, 현재 시간이 다음 공격 시간과 같은지만 확인하도록 구조를 단순화했다.
- `idx`를 사용해 현재 확인해야 하는 공격 하나만 추적했다.
- 공격 시간과 현재 시간이 같으면 공격을 처리하고, 그때만 `idx`를 증가시켰다.
- 공격이 없는 시간에는 회복만 수행하도록 분리했다.
- 죽는 조건도 `h <= 0`으로 수정해 문제 조건에 맞게 처리했다.
