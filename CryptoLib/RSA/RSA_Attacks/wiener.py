from utilities import SquareAndMultiply
from utilities import powinv
from utilities import DevContinuedFraction
from utilities import DivergentsComputation


def __helper(N,E,c):
    phi = (E*c[1]-1)//c[0]
    a = 1
    b = -(N-phi+1)
    c = N
    delta =b*b - 4*a*c
    if delta > 0:
        x1 = (-b + powinv((b*b - 4*a*c), 2))/(2*a)
        x2 = (-b - powinv((b*b - 4*a*c), 2))/(2*a)
        return {'q':x1,'p':x2} if x1*x2 == N else {'q':None,'p':None}
    else:
        return {'q':None,'p':None}
            
def wiener(N,E) :
	testStr = 42 
	phi = 0
	C = SquareAndMultiply(testStr, E, N)
	for c in DivergentsComputation(DevContinuedFraction(E, N)) :
		if SquareAndMultiply(C, c[1], N) == testStr :
		    pq = __helper(N,E,c)
		    pq.update({'d': c[1]})
		    return  pq
	return {'q':None,'p':None,'d':None}
