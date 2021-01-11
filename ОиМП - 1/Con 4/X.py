str = input()
i = 0
while i < len(str):
    if i % 3 != 0:
        print(str[i], end="")
    i += 1
