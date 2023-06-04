from utilities import isqrt
def fermat(n,limit):
    a = isqrt(n)
    max = a + limit
    while a < max:
        b2 = a*a - n
        if b2 >= 0:
            b = isqrt(b2)
            if b*b == b2:
                break
        a += 1
    return {'p':a+b , 'q':a-b} if a < max else False