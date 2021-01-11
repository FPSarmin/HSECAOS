a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
v1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
v2 = (a1 // a2) * (c1 // b2) * (b1 // c2)
v3 = (b1 // a2) * (a1 // b2) * (c1 // c2)
v4 = (b1 // a2) * (c1 // b2) * (a1 // c2)
v5 = (c1 // a2) * (a1 // b2) * (b1 // c2)
v6 = (c1 // a2) * (b1 // b2) * (a1 // c2)
if v2 > v1:
    (v1, v2) = (v2, v1)
if v3 > v1:
    (v1, v3) = (v3, v1)
if v4 > v1:
    (v1, v4) = (v4, v1)
if v5 > v1:
    (v1, v5) = (v5, v1)
if v6 > v1:
    (v1, v6) = (v6, v1)
print(v1)



