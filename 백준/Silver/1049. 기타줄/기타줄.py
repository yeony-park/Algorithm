import sys

input = sys.stdin.readline
n, m = map(int, input().split())

bundle_unit = 6 # 번들 내 개수
bundle_prices = []
unit_prices = []

for _ in range(m):
    b, u = map(int, input().split())
    bundle_prices.append(b)
    unit_prices.append(u)

bundle_price = min(bundle_prices)
unit_price = min(unit_prices)
    
answer = min(
    (n//6)*bundle_price + (n%6)*unit_price,
    ((n//6)+1)*bundle_price,
    n * unit_price
)

print(answer)