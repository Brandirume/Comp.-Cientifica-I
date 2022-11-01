import numpy as np
import matplotlib.pyplot as plt

def biss_solve(f, y, a, b, xtol=1e-8, ytol=1e-8):
    """Bissects the interval  [a,b]  until an approximate solution to  f(x) = y  is found.
    Also returns the number of bissections"""
    eq = lambda x: f(x) - y
    m = (a+b)/2
    nbiss = 1
    if eq(a)==0:
        print(f"eq(a) = 0, a = {a}")
        return a, nbiss
    elif eq(b) == 0:
        print(f"eq(b) = 0, b = {b}")
        return b, nbiss
    while abs(b-a)>xtol and abs(eq(m))>ytol:
        eqm = eq(m)
        if eqm*eq(a) < 0:
            b = m
            m = (a+b)/2 
        elif eqm*eq(b) < 0:
            a = m
            m = (a+b)/2 
        elif eqm==0:
            print(f"eq(m) = 0, m = {m}")
            return m, nbiss
        else:
            return "Sem solução", nbiss
        nbiss+=1
    return m, nbiss


z1, n1 = biss_solve(np.sin, 0.5, 0, np.pi/2)
z2, n2 = biss_solve(np.sin, 0.5, -np.pi/2, np.pi/2)
assert 20 <= n1 <= 30
assert 20 <= n2 <= 30