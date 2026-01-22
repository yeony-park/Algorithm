books = {}
number = int(input())

for _ in range(number):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1
print(sorted(books.items(), key= lambda x : (-x[1], x[0]))[0][0])