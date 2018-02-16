from utilities import mulinv,powinv

def hasted(n1,n2,n3,chipher_text_1,chipher_text_2,chipher_text_3):
    n = [n1,n2,n3]
    a = [chipher_text_1,chipher_text_2,chipher_text_3]
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mulinv(p, n_i) * p
    return powinv(sum % p)