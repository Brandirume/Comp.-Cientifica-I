import numpy as np
import matplotlib.pyplot as plt

def bissecao_pts(f, a, b, xtol=1e-8, ytol=1e-8, maxiter=100):
    """
    Encontra uma raiz de  f  pelo algoritmo da bissecao, retornando
    todos os pontos pelos quais o algoritmo passa.
    """
    iters = 0
    m = (a+b)/2
    pts = [m]
    fm = f(m)
    while abs(b-a)>xtol and abs(fm)>ytol and iters<maxiter:
        if f(a)*fm<0:
            if a not in pts: 
                pts.append(a)
            b = m
        elif f(b)*fm<0:
            if b not in pts: 
                pts.append(b)
            a = m
        elif fm==0:
            return m, pts
        else:
            if f(a)==0:
                if a not in pts: 
                    pts.append(a)
                return a, pts
            if f(b)==0:
                if b not in pts: 
                    pts.append(b)
                return b, pts
            else: 
                return "sem resposta", pts
        m = (a+b)/2
        fm = f(m)
        if m not in pts: 
            pts.append(m)
        iters+=1
    print(pts)
    print(f"{abs(b-a)>xtol} {abs(fm)>ytol}  {iters<maxiter}, {iters}")
    return pts

def df_central(f, x, h=1e-5):
    """Derivada central de  f  em  x, com passo  h"""
    d = (f(x + h) - f(x-h))/(2*h)
    return d

def ddf_central(f, x, h=1e-4):
    """Aproximação da segunda derivada de  f  em  x, usando a derivada central iterada com passo  h."""
    d1 = lambda x: df_central(f,x,h)
    return df_central(d1, x, h)

def newton_pts(f, df, x, xtol=1e-8, ytol=1e-8, maxiter=100):
    """
    Método de Newton para encontrar uma raiz de  f  a partir do valor inicial  x.
    Retorna todos os pontos pelos quais o algoritmo passa.
    """
    fx = f(x)
    step = fx/df(x)
    iters = 0
    pts = [x]
    # print(f"x:{x}, step:{step}, fx:{fx}, dfx:{df(x)}")
    while abs(fx)>ytol and abs(step)>xtol and iters < maxiter:
        x = x - step
        fx = f(x)
        step = fx/df(x)
        if x not in pts: pts.append(x);
        iters+=1
    print(f"x:{x}, step:{step}, fx:{fx}, dfx:{df(x)}, iter:{iters}")
    print(f"{abs(fx)>ytol} {abs(step)>xtol} {iters < maxiter}")
    return pts

def f(x):
    return np.exp(x) - 2*x

def g1(x):
    return np.exp(x) - 2

def g2(x):
    return df_central(f, x, h=1e-3)

def g3(x):
    return df_central(f, x, h=1e-5)

def h1(x):
    return np.exp(x)

def h2(x):
    return ddf_central(f, x)

iters = np.linspace(20,20,1)
a= newton_pts(g1, h1, 0.65, maxiter=4, xtol=1e-15, ytol=1e-15)[-1]
print(f"a = {a}\n\n")
b= newton_pts(g1, h2, 0.65, maxiter=4, xtol=1e-15, ytol=1e-15)[-1]
print(f"b = {b}\n\n")
print(np.log(2))


