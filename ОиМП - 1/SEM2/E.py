import string
a = input()
if a[0].isdigit() or a[0] == "_":
    print("FALSE")
else:
    is_ind = 1
    i = 0
    while i < len(a):
        if not a[i].isascii() and not a[i].isdigit() and a[i] != '_':
            is_ind = 0
            break
        i += 1
    if is_ind:
        print("TRUE")
    else:
        print("FALSE")