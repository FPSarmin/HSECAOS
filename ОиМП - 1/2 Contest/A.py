a = int(input())
b = int(input())
print((1 % (a // (b + 1) + 1)) * a + (1 % (b // a + 1)) * b)
# сорян, не сразу заметил, что тут нельзя пользоваться ветвлениями
