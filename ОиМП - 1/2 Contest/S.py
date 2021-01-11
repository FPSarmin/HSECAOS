n = int(input())
uni = n % 10
if uni >= 5 or uni == 0 or 10 <= n <= 20:
    print(n, "korov")
elif uni == 1:
    print(n, "korova")
elif uni == 2 or uni == 3 or uni == 4:
    print(n, "korovy")

