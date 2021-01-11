n = int(input())
min = (n + 1) // 2 * 110 - (n % 2) * 60 - (n % 2)\
      * 5 - 1 % ((n + 1) % 2 + 1) * 15
print(9 + min // 60, min % 60)
