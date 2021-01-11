str = input()
i = 1
print(str[0], end="")
while i < len(str):
    print('*', end="")
    print(str[i], end="")
    i += 1
