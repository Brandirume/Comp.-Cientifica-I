import numpy as np

def newton_solve(f, df, y, x0, xtol=1e-8, ytol=1e-8, maxiter=100):
    """Newton's algorithm for solving  f(x) = y  starting from  x0.
    Also returns the number of evaluations of f"""
    
    # YOUR CODE HERE
    nevals = 0
    x = x0
    def g(x): return f(x) - y
    print(x)
    for i in range(0,maxiter):
        g1 = g(x)
        print(f"{x}, {df(x)}, {g(x)}")
        step = g1 / df(x)
        nevals += 1
        newx = x - step
        print(f"{x}, {step}, {newx}")
        if abs(step) < xtol or abs(g1) < ytol:
            return newx,nevals
        x = newx
    return newx,nevals

def f(x):
    return np.log(x) + 1e9*x - 20
def df(x):
    return 1/x + 1e9

import matplotlib.pyplot as plt

x = np.linspace(-100,100,1000)
plt.plot(x,f(x))
plt.show()
# x = (newton_solve(f, df, 20, 0.5, xtol=1e-8, ytol=1e-8, maxiter=100))[0]
# assert np.isclose(f(x), -20, atol=1e-13, rtol=1e-13)