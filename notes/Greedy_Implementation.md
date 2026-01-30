# ![Tag](https://img.shields.io/badge/Tag-Greedy-2ea44f) 그리디 알고리즘 (Greedy)

## 정의
- 매 단계에서 **현재 상황에서 최선이라고 판단되는 선택**을 반복하는 방식
- 해를 빠르게 만들 수 있지만, **항상 최적해를 보장하지는 않음**

## 핵심 포인트
- 그리디 적용 여부는 **정당성 분석**으로 결정됨
- “매번 최선의 선택”이 전체 최적해로 이어지는지 **검증 필요**
- 보장 조건이 없는 문제에 무작정 적용하면 **최적해를 놓칠 수 있음**

## 정당성 분석 (필수 체크)
- 선택 규칙이 최적해를 보장하려면 보통 아래 중 일부가 성립해야 함
  - **Greedy-choice property**: 지금의 최선 선택이 전체 최적해의 일부가 될 수 있음
  - **Optimal substructure**: 부분 문제의 최적해를 조합해 전체 최적해 구성 가능
- **반례가 존재하는지**(작은 입력에서 깨지는지) 반드시 확인

## 시간 복잡도 관점
- 그리디는 보통 다음 단계로 구성됨
  - 정렬이 필요한 경우: `O(n log n)`
  - 1회 스캔/선택 반복: `O(n)`
- 실제 시간복잡도는 **정렬 유무**가 크게 좌우함

---

# ![Tag](https://img.shields.io/badge/Tag-Implementation-2ea44f) 구현 (Simulation / Brute Force)

## 구현이란?
- 문제에서 요구하는 과정을 **그대로 코드로 옮겨** 해결하는 유형
- 보통 아래와 같이 분류됨
  - **시뮬레이션**: 규칙/동작을 그대로 따라가며 상태 갱신
  - **완전 탐색(Brute Force)**: 가능한 경우를 전부 검사

## 2차원 공간 기본 인식
- 알고리즘 문제에서 2차원 공간은 보통 **행렬(matrix)**로 다룸
- 좌표 체계는 대개 다음처럼 사용됨
  - `(0,0)` 또는 `(1,1)`을 좌상단으로 두는 경우가 많음 (문제 조건 확인 필수)
  - `행(row)` / `열(col)`과 `x/y`를 혼동하지 않도록 주의

## itertools (순열/조합)
- 순열: `itertools.permutations(iterable, r)`
- 조합: `itertools.combinations(iterable, r)`
- 중복 조합: `itertools.combinations_with_replacement(iterable, r)`
- 데카르트 곱: `itertools.product(*iterables, repeat=...)`

## 방향 벡터 (Grid 이동 템플릿)
- 상/하/좌/우 등 이동을 “벡터”로 표현해서 구현 단순화
- 보통 다음 형태로 사용
  - `dx`, `dy`를 같은 인덱스로 묶어 이동 처리
- 좌표 범위 체크는 항상 포함
  - 예: `0 <= nx < n`, `0 <= ny < m` 또는 `1 <= nx <= n` 등 문제 기준

## 완전 탐색 가능 여부 판단
- 모든 경우의 수가 충분히 작으면(예: 수만~수십만 수준) 브루트 포스가 가능
- “3중 for문” 자체가 문제가 아니라, **반복 횟수 총합**이 핵심

---

# 시간 복잡도 (Big-O) 간단 정리

## Big-O 의미
- 입력 크기 증가에 따라 **연산량이 얼마나 증가하는지**를 나타내는 표기

## 자주 쓰는 표기
| 표기 | 의미 | 대표 예시 |
| --- | --- | --- |
| `O(1)` | 상수 시간 | 인덱스 접근 |
| `O(log n)` | 로그 시간 | 이진 탐색 |
| `O(n)` | 선형 | 한 번 순회 |
| `O(n log n)` | 정렬 기반 | merge sort, sort 후 스캔 |
| `O(n^2)` | 이차 | 이중 루프 |

---

## More details
[![Notion](https://img.shields.io/badge/Notion-Study%20Note-808080?logo=notion&logoColor=000000&labelColor=FFD700)](https://daily-archduke-be2.notion.site/2f45e249d44e80808760edcbdc08e9bd?source=copy_link)

## References
[![YouTube](https://img.shields.io/badge/YouTube-%EC%9D%B4%EC%BD%94%ED%85%8C%20%EA%B0%95%EC%9D%98-808080?logo=youtube&logoColor=FFFFFF&labelColor=FF0000)]()

