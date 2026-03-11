import sys

nums = []

for _ in range(10):
    a = int(input())
    a %= 42
    nums.append(a)

nums = set(nums)
print(len(nums))