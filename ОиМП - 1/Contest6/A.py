a, b = int(input()), int(input())
myRange = tuple(range(a, b + 1))
for _ in myRange:
    print(_, end=" ")
