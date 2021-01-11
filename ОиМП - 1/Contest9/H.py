setA = set(range(1, int(input()) + 1))
answer = setA
while True:
    temp = input()
    if temp == "HELP":
        print(*sorted(answer))
        break
    temp = set(map(int, temp.split()))
    setAB = answer & temp
    if len(setAB) > len(answer) / 2:
        print("YES")
        answer = setAB
    else:
        print("NO")
        answer -= setAB
