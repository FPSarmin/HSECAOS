postfixString = input().split()
nums = []
for x in postfixString:
    if x == '*' or x == '+' or x == '-' or x == '/':
        a = nums.pop()
        b = nums.pop()
        result = 0
        if x == '*':
            result = b * a
        elif x == '+':
            result = b + a
        elif x == '-':
            result = b - a
        elif x == '/':
            if a == 0:
                if b > 0:
                    result = 1000000
                else:
                    result = -1000000
            else:
                result = b / a
        if result > 1000000:
            result = 1000000
        elif result < -1000000:
            result = -1000000
        elif abs(result) < 0.000001:
            result = 0
        nums.append(result)
    else:
        nums.append(float(x))

print('{0:.6f}'.format(nums.pop()))
