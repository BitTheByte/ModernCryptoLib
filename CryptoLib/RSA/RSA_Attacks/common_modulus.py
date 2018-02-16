from utilities import modinv , egcd

def common_modulus(chipher_text_1, chipher_text_2, e1, e2, n):
    gcd,s1,s2 = egcd(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = modinv(chipher_text_1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = modinv(chipher_text_2, n)
    return (pow(c1, s1, n) * pow(c2, s2, n))