str = input()
i = 0
while i < len(str):
    if str[i].isdigit():
        print(str[i], end="")
    i += 1
