a, b = int(input()), int(input())
for i in range(a, b + 1):
    if int(str(i % 10) + str(i % 100 // 10)) == i // 100:
        print(i)
