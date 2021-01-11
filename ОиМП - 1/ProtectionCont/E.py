n = int(input())
i = 0
max_amount = int(input())
curr = max_amount
while i < n - 2:
    a, b = map(int, input().split())
    curr = curr + b - a
    max_amount = max(max_amount, curr)
    i += 1
curr = curr - int(input())
max_amount = max(max_amount, curr)
print(max_amount)
