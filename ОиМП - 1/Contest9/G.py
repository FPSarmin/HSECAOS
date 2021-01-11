setA = set(range(1, int(input()) + 1))
while True:
    temp = input()
    if temp == "HELP":
        break
    wtd = input()
    temp = set(map(int, temp.split()))
    if wtd == "NO":
        setA -= temp
    if wtd == "YES":
        setA &= temp
print(*sorted(setA))
