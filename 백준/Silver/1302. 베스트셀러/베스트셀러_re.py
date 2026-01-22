import sys
input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    book = str(input()).strip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
      
mx = max(books.values())
result = sorted(k for k, v in books.items() if v == mx)
print(result[0])
