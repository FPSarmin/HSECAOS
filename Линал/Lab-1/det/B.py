import numpy as np


def shrink_rotate(x, a, coef=1., angle=0.):
    x = x - a
    x *= coef
    x *= np.cos(angle) + np.sin(angle) * 1j
    return x


def shrink_rotate_conj(x, a, coef=1., angle=0.):
    shrink_rotate(x, a, coef, angle)
    x = x.counjugate()
    return x

def geometric_inverse(x, a, r):
    x = x - a
    x = x.counjugate**(-1)*r**2 + a
    return x


z = 0.5 + 0.*1j
max_iter = 100000
funcs = [
    (lambda t: shrink_rotate(t, 0. + 1.*1j, coef=0.5, angle=0.)),
    (lambda t: shrink_rotate(t, 1. + 0.*1j, coef=0.5, angle=0.)),
    (lambda t: shrink_rotate(t, -1. + 0.*1j, coef=0.5, angle=0.))
]

for n_iter in range(max_iter):
    n_func = np.random.choice(len(funcs))
    z = funcs[n_func](z)
