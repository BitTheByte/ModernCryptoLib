from utilities import convergents_from_contfrac
from utilities import is_perfect_square
from utilities import rational_to_contfrac
from sympy.solvers import solve
from sympy import Symbol
import sys

def wiener(n,e):
    d = None
    p = None
    q = None
    sys.setrecursionlimit(100000)
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    for (k,d) in convergents:
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            discr = s*s - 4*n
            if(discr>=0):
                t = is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    x = Symbol('x')
                    roots = solve(x**2 - s*x + n, x)
                    if len(roots) == 2:
                        p = roots[0]
                        q = roots[1]
                    break
    return {'p':p,'q':q,'d':d}