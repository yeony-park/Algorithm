import sys
input = sys.stdin.readline
nums =[]

for _ in range(9):
    nums.append(int(input()))

answer = max(nums)

print(answer)
print(nums.index(answer)+1)