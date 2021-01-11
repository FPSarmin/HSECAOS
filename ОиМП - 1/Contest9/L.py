a = input().replace('-', '').replace('(', '').replace(')', '')
if len(a) == 7:
    a = '495' + a
else:
    a = a[-10:]
numbers = set()
numbers.add(a)
currLen = len(numbers)
for i in range(3):
    temp = input().replace('-', '').replace('(', '').replace(')', '')
    if len(temp) == 7:
        temp = '495' + temp
    else:
        temp = temp[-10:]
    if temp in numbers:
        print("YES")
    else:
        print("NO")
