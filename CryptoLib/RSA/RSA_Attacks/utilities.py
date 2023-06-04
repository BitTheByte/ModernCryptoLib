import math


def DevContinuedFraction(num, denum):
	partialQuotients = []
	divisionRests = []
	for _ in range(int(math.log(denum, 2)/1)):
		divisionRests = num % denum
		partialQuotients.append(num / denum)
		num = denum
		denum = divisionRests
		if denum == 0 :
			break
	return partialQuotients

def DivergentsComputation(partialQuotients) :
	(p1, p2, q1, q2) = (1, 0, 0, 1)
	convergentsList = []
	for q in partialQuotients :
		pn = q * p1 + p2
		qn = q * q1 + q2
		convergentsList.append([pn, qn])
		p2 = p1
		q2 = q1
		p1 = pn
		q1 = qn
	return convergentsList    


def SquareAndMultiply(base,exponent,modulus):
	binaryExponent = []
	while exponent != 0:
		binaryExponent.append(exponent%2)
        	exponent = exponent/2
	result = 1
	binaryExponent.reverse()
	for i in binaryExponent:
		if i == 0:
			result = (result*result) % modulus
		else:
			result = (result*result*base) % modulus
	return result
def egcd(a,b):
	if a == 0:
		return (b, 0, 1)
	g, y, x = egcd(b % a, a)
	return (g, x - (b / a) * y, y)
def modinv(a,m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def mulinv(a,b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
def powinv(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1
def rational_to_contfrac( x, y):
	a = x//y
	if a * y == x:
		return [a]
	pquotients = rational_to_contfrac(y, x - a * y)
	pquotients.insert(0, a)
	return pquotients
def convergents_from_contfrac( frac):    
	return [contfrac_to_rational(frac[:i]) for i in range(len(frac))]
def contfrac_to_rational( frac):
	if len(frac) == 0:
		return (0,1)
	elif len(frac) == 1:
	    return (frac[0], 1)
	else:
		remainder = frac[1:]
		(num, denom) = contfrac_to_rational(remainder)
		return (frac[0] * num + denom, num)
def is_perfect_square( n):
	h = n & 0xF;
	if h > 9:
	    return -1
	if h not in [2, 3, 5, 6, 7, 8]:
		t = isqrt(n)
		return t if t*t == n else -1
	return -1
def isqrt( n):
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
