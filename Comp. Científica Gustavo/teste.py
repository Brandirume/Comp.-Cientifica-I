import numpy as np
A = np.array([[0, 1],[-4, -4/3]])
B = np.array([1,-16/3])
C = np.array([1, 0])

t =0.000001
tb = t*B
x1 = tb
print(C@x1)
x2 = tb + t*(A@tb) + tb
print(C@x2)
x3 = x2 + t*(A@x2) + tb
print(C@x3)
x4 = x3 + t*(A@x3) + tb
print(C@x4)
x5 = x4 + t*(A@x4) + tb
print(C@x5)
x6 = x5 + t*(A@x5) + tb
print(C@x6)
x7 = x6 + t*(A@x6) + tb
print(C@x7)
x8 = x7 + t*(A@x7) + tb
print(C@x8)
x9 = x8 + t*(A@x8) + tb
print(C@x9)
x10 = x9 + t*(A@x9) + tb
print(C@x10)
x11 = x10 + t*(A@x10) + tb
print(C@x11)
x12 = x11 + t*(A@x11) + tb
print(C@x12)
x13 = x12 + t*(A@x12) + tb
print(C@x13)