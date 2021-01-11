a = int(input())
b = int(input())
print(1 % (a % b + 1) * "NO" + (1 % (a % b)) % 2 * "YES")
