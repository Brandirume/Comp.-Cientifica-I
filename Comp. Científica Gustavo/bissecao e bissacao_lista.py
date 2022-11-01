
import numpy as np

def bissect_list(l, v):
    na = 0 
    n = len(l)
    b = n-1
    a= 0
    while True:
        if n == 0 :
            return None, 0
        else:
            if n == 1:
                if l[a] == v:
                    na+=1
                    return a, na
                else:
                    na+=1
                    return None, na
            elif n == 2:
                if l[a] == v:
                    na+=1
                    return a, na
                elif l[b] == v:
                    na+=2
                    return b, na
                else:
                    na+=1
                    return None, na
            else:
                m = a + ((b-a)/2).__round__()
                lm = l[m]
                na += 1
                if lm>v:
                    b = m - 1
                    n = b - a + 1
                else:
                    if lm == v:
                        return m, na
                    else: 
                        a = m +1 
                        n = b - a + 1

def bissect(l, v, decr=False):
    na = 0 
    n = len(l)
    b = n-1
    a= 0
    while True:
        if n == 0 :
            return None, 0
        else:
            if n == 1:
                if l[a] == v:
                    na+=1
                    return a, na
                else:
                    na+=1
                    return None, na
            elif n == 2:
                if l[a] == v:
                    na+=1
                    return a, na
                elif l[b] == v:
                    na+=2
                    return b, na
                else:
                    na+=1
                    return None, na
            else:
                m = a + ((b-a)/2).__round__()
                lm = l[m]
                na += 1
                if lm>v:
                    if not decr:
                        b = m - 1
                    else:
                        a = m + 1
                    n = b - a + 1
                else:
                    if lm == v:
                        return m, na
                    else: 
                        if not decr:
                            a = m + 1
                        else :
                            b = m - 1
                        n = b - a + 1

# l = np.arange(-4000000, 6000000)
# np.random.seed(1)
# count = 0
# nt= 0
# valores_testes = np.random.randint(low=-4000000, high=6000000, size=1)
# for v in valores_testes:
#     idx, n = bissect_list(l, v)
#     nt += n
#     count += 1

# print(nt/count)