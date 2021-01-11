a = input()
i = 0
ispal = 1
while i < (len(a) + 1) // 2:
    if a[i] != a[-i - 1]:
        ispal = 0
        break
    i += 1
if ispal:
    print("YES")
else:
    print("NO")