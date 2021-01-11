from sys import stdin


def check(students, i, S):
    if S < 0 or (S > 0 and i == len(students)):
        return False
    if S == 0:
        return True
    return check(students, i + 1, S - students[i]) \
        or check(students, i + 1, S)


n = int(stdin.readline())
students = list(map(int, stdin.readline().split()))
S = sum(students)
answer = 0
for i in range(S // 2, -1, -1):
    if check(students, 0, i):
        answer = S // 2 - i
        break
print(answer * 2 + S % 2)
