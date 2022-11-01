import matplotlib.pyplot as plt
import numpy as np
# def bissecao_pts(f, a, b, xtol=1e-8, ytol=1e-8, maxiter=100):
#     pts=[]
#     m = (a+b)/2
#     fm = f(m)
#     pts.append(m)
#     iters=1
#     while (abs(b-a) > xtol) and (iters < maxiter) and (abs(fm) > ytol):
#         if fm*f(a) < 0:
#             b = m
#             m = (a+b)/2
#             fm = f(m)
#             if a not in pts:
#                 pts.append(a)
#             if m not in pts:
#                 pts.append(m)
#         else:
#             a = m
#             m = (a+b)/2
#             fm = f(m)
#             if m not in pts:
#                 pts.append(m)
#         iters+=1
#     return pts

a = -1+1e-12
b = 1/2
f = lambda x: np.sin(x)
g = lambda x: np.cbrt(x)


def h(x):
    return np.sign(x) / np.log(np.abs(x))

def h2(y): # y = h(x)
    # Achar um x, h(x) - y = 0
    def inv(x):
        raiz = h(x) - y
        return raiz
    x2 = bissecao_pts(inv, a, -a, maxiter=350, ytol=0, xtol=0)[-1]
    return x2 # x2 é o x em h(x) = y

def bis(f,a,b):
    iters = 0
    while abs(a-b) >= 1e-8 and iters < 50:
        m = (a+b)/2
        if f(m)*f(a) < 0:
            b = m
        elif f(m)*f(b) < 0:
            a = m
        elif f(m)==0:
            return m
        iters += 1
    print((abs(a-b) >= 1e-8 and iters < 50), abs(a-b) >= 1e-8, iters < 50)
    return round((a+b)/2,8)

x = bis(lambda x: x**2, -2,1)
print(x)

# for x in np.linspace(-1+1e-8,1-1e-8,200):
#     assert abs(h2(h(x))-x) < 1e-15, (x, x - h2(h(x)))
#     assert abs(h(h2(x))-x) < 1e-15, (x, x - h(h2(x)))

# y=-0.02
# x = h2(y)
# print(y)
# print(x)
# print(h(x))
