l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
if l1 > w1:
    (l1, w1) = (w1, l1)
if l2 > w2:
    (l2, w2) = (w2, l2)
if lc < wc:
    (lc, wc) = (wc, lc)
if h1 <= hc and h2 <= hc:
    if (l1 + l2 <= lc and w1 <= wc and w2 <= wc) or \
            (l1 + l2 <= wc and w1 <= lc and w2 <= lc) \
            or (h1 + h2 <= hc and w1 <= lc and
                w2 <= lc and l1 <= wc and l2 <= wc):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
