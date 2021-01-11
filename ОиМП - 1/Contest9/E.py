n, m = map(int, input().split())
setA = set({})
setB = set({})
for _ in range(n):
    setA.add(int(input()))
for _ in range(m):
    setB.add(int(input()))
setAB = setA & setB
print(len(setAB))
print(*(sorted(setAB)))
print(len(setA - setAB))
print(*sorted((setA - setAB)))
print(len(setB - setAB))
print(*sorted((setB - setAB)))
